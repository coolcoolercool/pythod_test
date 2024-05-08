# -*- coding: utf-8 -*

# 导入请求包
import requests

from utils.print_utils import print_response_content, \
    print_request_content

# 设置要访问的地址
url = 'http://localhost:7111'
r = requests.get(url)
print(r.text)  # 返回请求的内容

