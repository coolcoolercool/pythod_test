# -*- coding: utf-8 -*

# 导入请求包
import requests

from utils.print_utils import print_response_content, \
    print_request_content

# 设置要访问的地址

# 请求访问hello service
url = 'http://localhost:7111'
r = requests.get(url)
print(r.text)   # 返回请求的内容
print("\n")

# 请求访问hello client
url = 'http://localhost:7211'
r = requests.get(url)
print(r.text)   # 返回请求的内容