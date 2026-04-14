import os
import re
import arxiv
import openai, tenacity
import base64, requests
import argparse
import tiktoken
from get_paper_from_pdf import Paper

from github_issue import make_github_issue


# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"

from config import (
    OPENAI_API_KEYS,
    KEYWORD_LIST,
    LANGUAGE,
    OPENAI_API_BASE,
    OPENAI_MODEL,
    ARXIV_CATEGORY_PREFIXES,
    DAILY_MAX_PAPERS,
    OUTPUT_TIMEZONE,
)

from datetime import datetime, timedelta
import pytz

now = datetime.now(pytz.utc)
yesterday = now - timedelta(days=1.1)


# 定义Reader类
class Reader:
    # 初始化方法，设置属性
    def __init__(self,  filter_keys, filter_times_span=(yesterday, now), key_word=None,      
                 query=None,  root_path='./',
                 sort=arxiv.SortCriterion.LastUpdatedDate, 
                 user_name='defualt', args=None):
        self.user_name = user_name # 读者姓名
        self.key_word = key_word # 读者感兴趣的关键词
        self.query = query # 读者输入的搜索查询
        self.sort = sort # 读者选择的排序方式
        if args.language == 'en':
            self.language = 'English'
        elif args.language == 'zh':
            self.language = 'Chinese'
        else:
            self.language = 'Chinese'        
        self.filter_keys = filter_keys # 用于在摘要中筛选的关键词
        self.filter_times_span = filter_times_span  # 用于选定某区间更新的arxiv paper
        self.category_prefixes = args.category_prefixes
        self.openai_model = args.openai_model

        self.root_path = root_path

        # 获取某个键对应的值        
        self.chat_api_list = OPENAI_API_KEYS

        self.cur_api = 0
        self.file_format = args.file_format        
        self.max_token_num = 4096
        self.encoding = tiktoken.get_encoding("gpt2")

    def _rotate_api_key(self):
        if not self.chat_api_list:
            raise ValueError("OPENAI_API_KEYS 为空，请先在 config.py 或环境变量中配置可用的 API Key。")
        openai.api_key = self.chat_api_list[self.cur_api]
        openai.api_base = OPENAI_API_BASE
        self.cur_api = (self.cur_api + 1) % len(self.chat_api_list)
                
    def get_arxiv(self, max_results=30):
        # https://info.arxiv.org/help/api/user-manual.html#query_details
        search = arxiv.Search(query=self.query,
                              max_results=max_results,                              
                              sort_by=self.sort,
                              sort_order=arxiv.SortOrder.Descending,
                              )       
        return search
     
    def filter_arxiv(self, max_results=30):
        search = self.get_arxiv(max_results=max_results)
        search_results = list(search.results())
        print("all search:")
        for index, result in enumerate(search_results):
            print(index, result.title, result.updated)
            
        filter_results = []   
        filter_keys = self.filter_keys
        
        print("filter_keys:", self.filter_keys)
        # 确保每个关键词都能在摘要中找到，才算是目标论文
        for index, result in enumerate(search_results):
            # 过滤不在时间范围内的论文
            if result.updated < self.filter_times_span[0] or result.updated > self.filter_times_span[1]:
                continue
            if not self.is_target_category(result):
                continue
            abs_text = result.summary.replace('-\n', '-').replace('\n', ' ')
            corpus_text = f"{result.title} {abs_text}"
            meet_num = 0
            for f_key in filter_keys.split(" "):
                if self.contains_keyword(corpus_text, f_key):
                    meet_num += 1
            if meet_num == len(filter_keys.split(" ")):
                filter_results.append(result)
                # break
        print("筛选后剩下的论文数量：")
        print("filter_results:", len(filter_results))
        print("filter_papers:")
        for index, result in enumerate(filter_results):
            print(index, result.title, result.updated)
        return filter_results

    def is_target_category(self, result):
        if not self.category_prefixes:
            return True
        categories = set(getattr(result, "categories", []) or [])
        primary_category = getattr(result, "primary_category", "")
        if primary_category:
            categories.add(primary_category)
        return any(
            category.startswith(prefix)
            for category in categories
            for prefix in self.category_prefixes
        )

    def contains_keyword(self, text, keyword):
        normalized_keyword = keyword.strip()
        if not normalized_keyword:
            return False
        if len(normalized_keyword) <= 4 and normalized_keyword.replace("-", "").isalnum():
            return re.search(r"\b{}\b".format(re.escape(normalized_keyword)), text, re.IGNORECASE) is not None
        return normalized_keyword.lower() in text.lower()

    def deduplicate_results(self, results, seen_entry_ids):
        unique_results = []
        for result in results:
            entry_id = getattr(result, "entry_id", None) or getattr(result, "pdf_url", None) or result.title
            if entry_id in seen_entry_ids:
                continue
            seen_entry_ids.add(entry_id)
            unique_results.append(result)
        print("去重后剩下的论文数量：")
        print("unique_results:", len(unique_results))
        return unique_results
    
    def validateTitle(self, title):
        # 将论文的乱七八糟的路径格式修正
        rstr = r"[\/\\\:\*\?\"\<\>\|]" # '/ \ : * ? " < > |'
        new_title = re.sub(rstr, "_", title) # 替换为下划线
        return new_title

    def download_pdf(self, filter_results):
        # 先创建文件夹
        date_str = str(datetime.now())[:13].replace(' ', '-')        
        key_word = str(self.key_word.replace(':', ' '))        
        path = self.root_path  + 'pdf_files/' + self.query.replace('au: ', '').replace('title: ', '').replace('ti: ', '').replace(':', ' ')[:25] + '-' + date_str
        try:
            os.makedirs(path)
        except:
            pass
        print("All_paper:", len(filter_results))
        # 开始下载：
        paper_list = []
        for r_index, result in enumerate(filter_results):
            try:
                title_str = self.validateTitle(result.title)
                pdf_name = title_str+'.pdf'
                # result.download_pdf(path, filename=pdf_name)
                self.try_download_pdf(result, path, pdf_name)
                paper_path = os.path.join(path, pdf_name)
                print("paper_path:", paper_path)
                paper = Paper(path=paper_path,
                              url=result.entry_id,
                              title=result.title,
                              abs=result.summary.replace('-\n', '-').replace('\n', ' '),
                              authers=[str(aut) for aut in result.authors],
                              )
                # 下载完毕，开始解析：
                paper.parse_pdf()
                paper_list.append(paper)
            except Exception as e:
                print("download_error:", e)
                pass
        return paper_list
    
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def try_download_pdf(self, result, path, pdf_name):
        result.download_pdf(path, filename=pdf_name)
    
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def upload_gitee(self, image_path, image_name='', ext='png'):
        """
        上传到码云
        :return:
        """ 
        with open(image_path, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            base64_content = base64_data.decode()
        
        date_str = str(datetime.now())[:19].replace(':', '-').replace(' ', '-') + '.' + ext
        path = image_name+ '-' +date_str
        
        payload = {
            "access_token": self.gitee_key,
            "owner": self.config.get('Gitee', 'owner'),
            "repo": self.config.get('Gitee', 'repo'),
            "path": self.config.get('Gitee', 'path'),
            "content": base64_content,
            "message": "upload image"
        }
        # 这里需要修改成你的gitee的账户和仓库名，以及文件夹的名字：
        url = f'https://gitee.com/api/v5/repos/'+self.config.get('Gitee', 'owner')+'/'+self.config.get('Gitee', 'repo')+'/contents/'+self.config.get('Gitee', 'path')+'/'+path
        rep = requests.post(url, json=payload).json()
        print("rep:", rep)
        if 'content' in rep.keys():
            image_url = rep['content']['download_url']
        else:
            image_url = r"https://gitee.com/api/v5/repos/"+self.config.get('Gitee', 'owner')+'/'+self.config.get('Gitee', 'repo')+'/contents/'+self.config.get('Gitee', 'path')+'/' + path
            
        return image_url
        
    def summary_with_chat(self, paper_list, htmls=None):
        if htmls is None:
            htmls = []
        for paper_index, paper in enumerate(paper_list):
            text = self.build_summary_source_text(paper)
            chat_summary_text = ""
            try:
                chat_summary_text = self.chat_summary(text=text)
            except Exception as e:
                print("summary_error:", e)
                if "maximum context" in str(e):
                    current_tokens_index = str(e).find("your messages resulted in") + len("your messages resulted in")+1
                    offset = int(str(e)[current_tokens_index:current_tokens_index+4])
                    summary_prompt_token = offset+1000+150
                    chat_summary_text = self.chat_summary(text=text, summary_prompt_token=summary_prompt_token)

            htmls.append(f'## {paper.title}')
            htmls.append(f'- **论文链接**: {paper.url}')
            htmls.append(f'- **作者**: {", ".join(paper.authers)}')
            htmls.append(f'- **原始摘要**: {paper.abs}')
            htmls.append('')
            htmls.append(chat_summary_text)
            htmls.append('')

    def build_summary_source_text(self, paper):
        section_dict = getattr(paper, "section_text_dict", {})
        sections = [
            ("Title", paper.title),
            ("Url", paper.url),
            ("Abstract", paper.abs),
            ("PaperInfo", section_dict.get("paper_info", "")),
            ("Introduction", self.pick_section_text(section_dict, ["Introduction", "Background", "Related Work"])),
            ("Method", self.pick_section_text(section_dict, ["Methods", "Methodology", "Method", "Approach", "Approaches", "Problem Formulation"])),
            ("Experiment", self.pick_section_text(section_dict, ["Experiments", "Experiment", "Experimental Results", "Evaluation", "Results"])),
            ("Conclusion", self.pick_section_text(section_dict, ["Conclusion", "Discussion", "Results and Discussion"])),
        ]
        return "\n\n".join(
            f"{section_name}: {section_text}"
            for section_name, section_text in sections
            if section_text
        )

    def pick_section_text(self, section_dict, candidate_names):
        for section_name in candidate_names:
            section_text = section_dict.get(section_name, "")
            if section_text:
                return section_text
        return ""

    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def chat_conclusion(self, text, conclusion_prompt_token = 800):
        self._rotate_api_key()
        text_token = len(self.encoding.encode(text))
        clip_text_index = int(len(text)*(self.max_token_num-conclusion_prompt_token)/text_token)
        clip_text = text[:clip_text_index]   
        
        messages=[
                {"role": "system", "content": "You are a reviewer in the field of ["+self.key_word+"] and you need to critically review this article"},  # chatgpt 角色
                {"role": "assistant", "content": "This is the <summary> and <conclusion> part of an English literature, where <summary> you have already summarized, but <conclusion> part, I need your help to summarize the following questions:"+clip_text},  # 背景知识，可以参考OpenReview的审稿流程
                {"role": "user", "content": """                 
                 8. Make the following summary.Be sure to use {} answers (proper nouns need to be marked in English).
                    - (1):What is the significance of this piece of work?
                    - (2):Summarize the strengths and weaknesses of this article in three dimensions: innovation point, performance, and workload.                   
                    .......
                 Follow the format of the output later: 
                 8. Conclusion: \n\n
                    - (1):xxx;\n                     
                    - (2):Innovation point: xxx; Performance: xxx; Workload: xxx;\n                      
                 
                 Be sure to use {} answers (proper nouns need to be marked in English), statements as concise and academic as possible, do not repeat the content of the previous <summary>, the value of the use of the original numbers, be sure to strictly follow the format, the corresponding content output to xxx, in accordance with \n line feed, ....... means fill in according to the actual requirements, if not, you can not write.                 
                 """.format(self.language, self.language)},
            ]
        response = openai.ChatCompletion.create(
            model=self.openai_model,
            # prompt需要用英语替换，少占用token。
            messages=messages,
            request_timeout=120,
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        print("conclusion_result:\n", result)
        print("prompt_token_used:", response.usage.prompt_tokens,
              "completion_token_used:", response.usage.completion_tokens,
              "total_token_used:", response.usage.total_tokens)
        print("response_time:", response.response_ms/1000.0, 's')             
        return result            
    
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def chat_method(self, text, method_prompt_token = 800):
        self._rotate_api_key()
        text_token = len(self.encoding.encode(text))
        clip_text_index = int(len(text)*(self.max_token_num-method_prompt_token)/text_token)
        clip_text = text[:clip_text_index]        
        messages=[
                {"role": "system", "content": "You are a researcher in the field of ["+self.key_word+"] who is good at summarizing papers using concise statements"},  # chatgpt 角色
                {"role": "assistant", "content": "This is the <summary> and <Method> part of an English document, where <summary> you have summarized, but the <Methods> part, I need your help to read and summarize the following questions."+clip_text},  # 背景知识
                {"role": "user", "content": """                 
                 7. Describe in detail the methodological idea of this article. Be sure to use {} answers (proper nouns need to be marked in English). For example, its steps are.
                    - (1):...
                    - (2):...
                    - (3):...
                    - .......
                 Follow the format of the output that follows: 
                 7. Methods: \n\n
                    - (1):xxx;\n 
                    - (2):xxx;\n 
                    - (3):xxx;\n  
                    ....... \n\n     
                 
                 Be sure to use {} answers (proper nouns need to be marked in English), statements as concise and academic as possible, do not repeat the content of the previous <summary>, the value of the use of the original numbers, be sure to strictly follow the format, the corresponding content output to xxx, in accordance with \n line feed, ....... means fill in according to the actual requirements, if not, you can not write.                 
                 """.format(self.language, self.language)},
            ]
        response = openai.ChatCompletion.create(
            model=self.openai_model,
            messages=messages,
            request_timeout=120,
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        print("method_result:\n", result)
        print("prompt_token_used:", response.usage.prompt_tokens,
              "completion_token_used:", response.usage.completion_tokens,
              "total_token_used:", response.usage.total_tokens)
        print("response_time:", response.response_ms/1000.0, 's') 
        return result
    
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def chat_summary(self, text, summary_prompt_token = 1100):
        self._rotate_api_key()
        text_token = len(self.encoding.encode(text))
        clip_text_index = int(len(text)*(self.max_token_num-summary_prompt_token)/text_token)
        clip_text = text[:clip_text_index]
        messages=[
                {"role": "system", "content": "You are a researcher in the field of ["+self.key_word+"] who is good at summarizing papers using concise statements"},
                {"role": "assistant", "content": "This is the title, author, link, abstract, introduction, method, experiment and conclusion extracted from an English paper. I need your help to summarize it into a daily reading note: "+clip_text},
                {"role": "user", "content": """                 
                 Please answer in {} and strictly use the following Markdown format.
                 If some information is missing in the source text, say "文中未明确说明" instead of guessing.

                 ### GPT总结
                 #### 文章内容
                 用2-4句话概括这篇论文要解决什么问题、核心思路是什么、主要结论是什么。

                 #### 方法
                 用3-5条要点概括方法流程、关键模块、训练/推理方式或决策机制。

                 #### 创新点
                 用2-4条要点概括相对已有工作的主要创新，强调结构设计、任务建模、优化目标或实验设置上的新意。

                 #### 实验结论
                 用2-3条要点概括任务、数据集、核心结果和作者结论。

                 Keep the statements concise, academic, and faithful to the paper. Preserve original numbers and proper nouns in English when they appear.
                 """.format(self.language, self.language, self.language)},
            ]
                
        response = openai.ChatCompletion.create(
            model=self.openai_model,
            messages=messages,
            request_timeout=120,
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        print("summary_result:\n", result)
        print("prompt_token_used:", response.usage.prompt_tokens,
              "completion_token_used:", response.usage.completion_tokens,
              "total_token_used:", response.usage.total_tokens)
        print("response_time:", response.response_ms/1000.0, 's')                    
        return result      

    # 定义一个方法，打印出读者信息
    def show_info(self):        
        print(f"Key word: {self.key_word}")
        print(f"Query: {self.query}")
        print(f"Sort: {self.sort}")     

def save_to_file(htmls, root_path='./', date_str=None, file_format='md'):
    # # 整合成一个文件，打包保存下来。
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    try:
        export_path = os.path.join(root_path, 'export')
        os.makedirs(export_path, exist_ok=True)
    except:
        pass                             
    mode = 'w'
    file_name = os.path.join(export_path, date_str+"."+file_format)
    export_to_markdown("\n".join(htmls), file_name=file_name, mode=mode)

def export_to_markdown(text, file_name, mode='w'):
    # 使用markdown模块的convert方法，将文本转换为html格式
    # html = markdown.markdown(text)
    # 打开一个文件，以写入模式
    with open(file_name, mode, encoding="utf-8") as f:
        # 将html格式的内容写入文件
        f.write(text)

def main(args):       
    # 创建一个Reader对象，并调用show_info方法
    if args.sort == 'Relevance':
        sort = arxiv.SortCriterion.Relevance
    elif args.sort == 'LastUpdatedDate':
        sort = arxiv.SortCriterion.LastUpdatedDate
    else:
        sort = arxiv.SortCriterion.Relevance
    
    if args.pdf_path:
        reader1 = Reader(key_word=args.key_word, 
                         query=args.query, 
                         filter_keys=args.filter_keys,                                    
                         sort=sort, 
                         args=args
                         )
        reader1.show_info()
        # 开始判断是路径还是文件：   
        paper_list = []     
        if args.pdf_path.endswith(".pdf"):
            paper_list.append(Paper(path=args.pdf_path))            
        else:
            for root, dirs, files in os.walk(args.pdf_path):
                print("root:", root, "dirs:", dirs, 'files:', files) #当前目录路径
                for filename in files:
                    # 如果找到PDF文件，则将其复制到目标文件夹中
                    if filename.endswith(".pdf"):
                        paper_list.append(Paper(path=os.path.join(root, filename)))        
        print("------------------paper_num: {}------------------".format(len(paper_list)))        
        [print(paper_index, paper_name.path.split('\\')[-1]) for paper_index, paper_name in enumerate(paper_list)]
        reader1.summary_with_chat(paper_list=paper_list)
    else:
        filter_times_span = (now-timedelta(days=args.filter_times_span), now)
        report_date = datetime.now(pytz.timezone(args.output_timezone)).strftime("%Y-%m-%d")
        title = f"{report_date}-cs-daily-papers"
        htmls_body = [
            f"# {report_date} 计算机领域论文日报",
            "",
            f"> 更新时间范围：最近 {args.filter_times_span} 天",
            f"> 分类限制：{', '.join(args.category_prefixes)}",
            f"> 单次最多输出：{args.max_total_papers} 篇",
            "",
        ]
        seen_entry_ids = set()
        processed_paper_count = 0
        for filter_key in args.filter_keys:
            if args.max_total_papers and processed_paper_count >= args.max_total_papers:
                print("已达到本次运行的总论文上限，提前结束。")
                break
            # 对于每一个主题做一遍
            # filter_key: remote sensing
            # query: all:remote AND all:sensing
            key_word = filter_key
            query = ''
            for item in filter_key.split(" "):
                if query != '':
                    query += ' AND '
                query += f'all:{item}'
            htmls = []
            reader1 = Reader(key_word=key_word, 
                            query=query, 
                            filter_keys=filter_key,
                            filter_times_span=filter_times_span,                           
                            sort=sort,
                            args=args
                            )
            reader1.show_info()
            filter_results = reader1.filter_arxiv(max_results=args.max_results)
            filter_results = reader1.deduplicate_results(filter_results, seen_entry_ids)
            if args.max_papers_per_keyword:
                filter_results = filter_results[:args.max_papers_per_keyword]
            if args.max_total_papers:
                remaining_quota = args.max_total_papers - processed_paper_count
                if remaining_quota <= 0:
                    print("已没有剩余论文配额，结束本次运行。")
                    break
                filter_results = filter_results[:remaining_quota]
            if not filter_results:
                continue
            paper_list = reader1.download_pdf(filter_results)
            if not paper_list:
                continue
            processed_paper_count += len(paper_list)
            htmls.append(f'## 关键词：{filter_key}')
            htmls.append('')
            reader1.summary_with_chat(paper_list=paper_list, htmls=htmls)
            htmls_body += htmls
            if args.max_total_papers and processed_paper_count >= args.max_total_papers:
                break
        if processed_paper_count == 0:
            htmls_body.extend([
                "## 今日结果",
                "",
                "今天没有筛选到同时满足关键词、时间窗口和 `cs.*` 分类限制的新论文。",
            ])
        save_to_file(htmls_body, date_str=title, root_path='./')
        make_github_issue(title=title, body="\n".join(htmls_body), labels=args.filter_keys)

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_path", type=str, default='', help="if none, the bot will download from arxiv with query")
    parser.add_argument("--query", type=str, default='all:remote AND all:sensing', help="the query string, ti: xx, au: xx, all: xx,") 
    parser.add_argument("--key_word", type=str, default='remote sensing', help="the key word of user research fields")
    parser.add_argument("--filter_keys", nargs='*', default=KEYWORD_LIST, help="the filter key words, 摘要和标题中每个单词都得有，才会被筛选为目标论文")
    parser.add_argument("--filter_times_span", type=float, default=1.5, help='how many days of files to be filtered.')
    parser.add_argument("--max_results", type=int, default=10, help="the maximum number of results")
    parser.add_argument("--max_papers_per_keyword", type=int, default=1, help="maximum papers to process for each keyword, 0 means unlimited")
    parser.add_argument("--max_total_papers", type=int, default=DAILY_MAX_PAPERS, help="maximum papers to process in one run, 0 means unlimited")
    # arxiv.SortCriterion.Relevance
    parser.add_argument("--sort", type=str, default="LastUpdatedDate", help="another is LastUpdatedDate | Relevance")
    parser.add_argument("--file_format", type=str, default='md', help="导出的文件格式，如果存图片的话，最好是md，如果不是的话，txt的不会乱")
    parser.add_argument("--language", type=str, default=LANGUAGE, help="The other output lauguage is English, is en")
    parser.add_argument("--openai_model", type=str, default=OPENAI_MODEL, help="model name used for paper summarization")
    parser.add_argument("--category_prefixes", nargs='*', default=ARXIV_CATEGORY_PREFIXES, help="arXiv category prefixes to keep, for example: cs.")
    parser.add_argument("--output_timezone", type=str, default=OUTPUT_TIMEZONE, help="timezone used in report titles and markdown filenames")
    
    args = parser.parse_args()
    import time
    start_time = time.time()
    main(args=args)    
    print("summary time:", time.time() - start_time)
    
