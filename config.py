# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'whatever2077'
TOKEN = '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'

# The repository to add this issue to
REPO_OWNER = 'whatever2077'
REPO_NAME = 'super-resolution-and-RL'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["image super-resolution", "reinforcement learning"]
OPENAI_API_KEYS = ["sk-nG2b2a92a6ad1c499d24d5c93436a6d5a61ce779e1885ZQ9"]
OPENAI_API_BASE = "https://api.gptsapi.net/v1"
LANGUAGE = "zh" 
OPENAI_MODEL = "gpt-5"

# 只保留计算机领域 arXiv 分类，例如 cs.CV / cs.LG / cs.AI。
ARXIV_CATEGORY_PREFIXES = ["cs."]

# 每日推送上限，推荐 1-3 篇。
DAILY_MAX_PAPERS = 3

# 输出 markdown 文件名时使用的时区。
OUTPUT_TIMEZONE = "Asia/Shanghai"
