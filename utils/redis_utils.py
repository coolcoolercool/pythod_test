# -*- coding: utf-8 -*
import redis


def redis_insert_user_info(uuid_str):
    host = 'localhost'
    pool = redis.ConnectionPool(host=host, port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    # r.set('food', 'mutton', ex=1 * 1000 * 60 * 2)
    # print(r.get('food'))  # mutton 取出键food对应的值

    hash_key = uuid_str
    user_info_dict = {
        'username': 'sscc1103',
        'functionIds': [
            'function_id_0', 'function_id_1'
        ]
    }
    functionIds = ['function_id_0', 'function_id_1']
    r.hset(hash_key, 'username', 'sscc1103')
    r.hset(hash_key, 'functionIds', str(functionIds))
    r.expire(hash_key, 60 * 2) # 设置过期时间为60s
    print(r.hkeys(hash_key)) # 取hash中所有的key


if __name__ == '__main__':
    redis_insert_user_info()