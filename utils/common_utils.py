import json
import time
import hashlib


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


if __name__ == '__main__':
    encodeBySM3()
