# -*- coding: utf-8 -*

# 导入请求包
import requests
# 导入json包
import json
# 导出美化Json的包
import pprint

from utils.print_utils import print_json, print_request_and_response, print_json_with_name, print_response_content, \
    print_request_content

# 设置要访问的地址
url = 'http://localhost:8080/testPython'

# 定一个字典类型
mapA = {"name": "name", "gender": "gender"}

print_request_content(mapA)

# 直接请求
#r = requests.post(url, data=mapA, hooks={'response': print_request_and_response})
r = requests.post(url, data=mapA)

# 这里是输出了一个字符串
# pprint.pprint(r.json())

url = 'http://localhost:8080/testGetPython'
# 直接请求
#r = requests.get(url, hooks={'response': print_request_and_response})
r = requests.get(url)
# print_json(r.json(), "data")
#
# print(r.status_code)  # 返回状态码
# print(r.reason)  # 正常返回OK，异常返回对应的Http响应状态描述
# print(r.headers)  # 获取响应头
# print(r.text)  # 返回请求的内容

print_response_content(r)

