import redis
from random import choice
import json
from pyquery import PyQuery as pq

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

#存储模块
class RedisClient(object):
    def __init__(self, host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        #初始化
        #:param host:Redis 地址
        #:param port:Redis 端口
        #:param password:Redis 密码
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        #添加代理，设置分数为最高
        #:param:proxy 代理
        #:param:score 分数
        #:return:结果
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        #随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        #:return:有效代理
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                return PoolEmptyError
    def decrease(self,proxy):
        #代理值减1分，分数小于最小值，则删除代理
        #:param proxy:代理
        #:return :修改后的代理分数
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减一')
            return self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        #判断是否存在
        #:param peoxy:代理
        #:return:是否存在
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def max(self,proxy):
        #将代理设为MAX_SCORE
        #:param proxy:代理
        #:return :设置结果
        print('代理',proxy,'可用，设置为',MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        #获取数量
        #:return:数量
        return self.db.zcard(REDIS_KEY)

    def all(self):
        #获取全部代理
        #:return: 全部代理列表
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)



#获取模块
