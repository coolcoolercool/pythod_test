# -*- coding: utf-8 -*

import time
import uuid

import jwt

from utils.common_utils import get_now_unix_time


def create_jwt_str(uuid_str):
    # payload
    token_dict = {
        'iat': time.time(),  # 时间戳
        'exp': get_now_unix_time() + 60 * 60 * 10,
        'uuid': uuid_str
    }

    """payload 中一些固定参数名称的意义, 同时可以在payload中自定义参数"""
    # iss  【issuer】发布者的url地址
    # sub 【subject】该JWT所面向的用户，用于处理特定应用，不是常用的字段
    # aud 【audience】接受者的url地址
    # exp 【expiration】 该jwt销毁的时间；unix时间戳
    # nbf  【not before】 该jwt的使用时间不能早于该时间；unix时间戳
    # iat   【issued at】 该jwt的发布时间；unix 时间戳
    # jti    【JWT ID】 该jwt的唯一ID编号

    # headers
    headers = {
        'alg': "HS256",  # 声明所使用的算法
    }

    """headers 中一些固定参数名称的意义"""
    # jku: 发送JWK的地址；最好用HTTPS来传输
    # jwk: 就是之前说的JWK
    # kid: jwk的ID编号
    # x5u: 指向一组X509公共证书的URL
    # x5c: X509证书链
    # x5t：X509证书的SHA-1指纹
    # x5t#S256: X509证书的SHA-256指纹
    # typ: 在原本未加密的JWT的基础上增加了 JOSE 和 JOSE+ JSON。JOSE序列化后文会说及。适用于JOSE标头的对象与此JWT混合的情况。
    # crit: 字符串数组，包含声明的名称，用作实现定义的扩展，必须由 this->JWT的解析器处理。不常见。

    secret_key = 'zhananbudanchou1234678'
    # 调用jwt库,生成json web token
    jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                           secret_key,  # 进行加密签名的密钥
                           algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                           headers=headers  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                           )

    print(jwt_token)
    return jwt_token


def parse_jwt():
    secret_key = 'zhananbudanchou1234678'
    jwt_str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTUyNDE5ODAuNzcyMjUwMiwiZXhwIjoxNzE1Mjc3OTgwLCJ1dWlkIjoiOWZhZWRlNmMtY2I0Ny00NmI1LWI3ODQtNmJjYmY4YmZlNGEzIn0.UafFnjq7fC9fFeeIsTYS5B67-ErMyBBfVOjgJ0MtNSo'
    data = None
    try:
        #需要解析的 jwt密钥   使用和加密时相同的算法
        data = jwt.decode(jwt_str, secret_key, algorithms=['HS256'])
    except Exception as e:
        # 如果 jwt 被篡改过; 或者算法不正确; 如果设置有效时间, 过了有效期; 或者密钥不相同; 都会抛出相应的异常
        print(e)
    print(data)


if __name__ == '__main__':
    parse_jwt()
