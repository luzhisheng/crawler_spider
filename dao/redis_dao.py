import settings
import redis
import threading


class MyRedis(object):
    _instance_lock = threading.Lock()

    def __new__(cls):
        """调用redis数据库 使用单列模式避免创建多个对象,导致内存泄露"""
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        pool = redis.ConnectionPool(host=settings.REDIS_HOST,
                                    port=settings.REDIS_PORT,
                                    db=settings.REDIS_DB,
                                    password=settings.REDIS_PWD)
        self.redis_conn = redis.Redis(connection_pool=pool)

    def push(self, queue_name, item):
        self.redis_conn.rpush(queue_name, item)

    def find_conf_by_source(self, source):
        """根据source 获取相应的配置"""
        data_json = eval(self.redis_conn.hget(settings.NEWS_SCORE_CONF_HASH, source) or '{}')
        return data_json

    def update_conf_by_source(self, source, para_json):
        """更新动态计算产生的数据"""
        self.redis_conn.hset(settings.NEWS_SCORE_CONF_HASH, source, str(para_json))

    def get_initial_conf(self):
        """程序启动 redis 中获取初始化配置文件"""
        result = eval(self.redis_conn.get(settings.NEWS_SCORE_INITIAL_CONF) or '{}')
        return result if result else False

    def set_initial_conf(self, initial_conf_json):
        """设置初始化配置"""
        self.redis_conn.set(settings.NEWS_SCORE_INITIAL_CONF, str(initial_conf_json))


if __name__ == '__main__':
    pass
