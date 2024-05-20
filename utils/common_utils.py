# -*- coding: utf-8 -*
import json
import random
import string
import time
import hashlib
import uuid


# 获取当前时间
def get_now_time():
    return int(time.time())


def encodeBySM3():
    # 创建SM3对象
    sm3 = hashlib.new('sm3')

    # 输入待加密数据
    data_map = {
        "username": "username",
        "password": "password",
        "success": False
    }
    # 保留双引号，并且去除dumps自带空格
    data_str = json.dumps(data_map, separators=(',', ':'))
    now_time = 1714981901
    plain_str = data_str + str(now_time)
    print(plain_str)
    sm3.update(plain_str.encode('utf-8'))

    # 计算哈希值
    hash_value = sm3.hexdigest()

    # 输出加密结果
    print("SM3 Hash Value:", hash_value)


def get_now_unix_time_str():
    return str(int(time.time()))


def get_now_unix_time():
    return int(time.time())


def get_uuid_str():
    return str(uuid.uuid4())


# 生成指定长度的随机字符串
def get_target_str(length):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
    random_str = ''.join(str_list)
    return random_str


# [a,b,c] -> a,b,c
def change_list_2_str(change_list):
    return ', '.join(change_list)


if __name__ == '__main__':
    encodeBySM3()
