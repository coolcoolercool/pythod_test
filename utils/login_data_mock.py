# -*- coding: utf-8 -*
import uuid

from utils.jwt_utils import create_jwt_str
from utils.redis_utils import redis_insert_user_info


# 模拟登录的时候
def mock_login():
    uuid_str = str(uuid.uuid4())
    jwt_str = create_jwt_str(uuid_str)

    redis_insert_user_info(uuid_str)
    return uuid_str, jwt_str

