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

#�洢ģ��
class RedisClient(object):
    def __init__(self, host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        #��ʼ��
        #:param host:Redis ��ַ
        #:param port:Redis �˿�
        #:param password:Redis ����
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        #��Ӵ������÷���Ϊ���
        #:param:proxy ����
        #:param:score ����
        #:return:���
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        #�����ȡ��Ч�������ȳ��Ի�ȡ��߷������������߷��������ڣ�����������ȡ�������쳣
        #:return:��Ч����
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
        #����ֵ��1�֣�����С����Сֵ����ɾ������
        #:param proxy:����
        #:return :�޸ĺ�Ĵ������
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score > MIN_SCORE:
            print('����',proxy,'��ǰ����',score,'��һ')
            return self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            print('����',proxy,'��ǰ����',score,'�Ƴ�')
            return self.db.zrem(REDIS_KEY,proxy)

    def exists(self,proxy):
        #�ж��Ƿ����
        #:param peoxy:����
        #:return:�Ƿ����
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def max(self,proxy):
        #��������ΪMAX_SCORE
        #:param proxy:����
        #:return :���ý��
        print('����',proxy,'���ã�����Ϊ',MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def count(self):
        #��ȡ����
        #:return:����
        return self.db.zcard(REDIS_KEY)

    def all(self):
        #��ȡȫ������
        #:return: ȫ�������б�
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)



#��ȡģ��
