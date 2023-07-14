from datetime import datetime
import os


def log(s):
    print('【%s】 %s' % (datetime.now(), s), flush=True)


if os.environ.get('ENV_REPLACE_API') == 'prod':
    log('生产环境')
    mysql_server_daduoduo = {
        "host": '127.0.0.1',
        "user": 'root',
        "password": os.environ.get('DB_PASSWORD_DADUODUO'),
        "db": 'eb_supports_daduoduo',
        "port": 3306,
        "charset": 'utf8mb4'
    }

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    REDIS_PWD = os.environ.get('REDIS_PWD')
    REDIS_DB = 0
    NEWS_SCORE_CONF_HASH = 'news_score_conf_hash'
    NEWS_SCORE_INITIAL_CONF = 'news_score_initial_conf'
    REDIS_EXTRACTOR_QUEUE = 'queue:raw_data'
    REDIS_SPIDER_QUEUE = 'queue:spider_data'
else:
    log('测试环境')
    mysql_server_daduoduo = {
        "host": '127.0.0.1',
        "user": 'root',
        "password": '123456',
        "db": 'eb_supports_daduoduo',
        "port": 3306,
        "charset": 'utf8mb4'
    }

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    REDIS_PWD = 'ayf@ddwfc'
    REDIS_DB = 0
    NEWS_SCORE_CONF_HASH = 'news_score_conf_hash'
    NEWS_SCORE_INITIAL_CONF = 'news_score_initial_conf'
    REDIS_EXTRACTOR_QUEUE = 'queue:raw_data'
    REDIS_SPIDER_QUEUE = 'queue:spider_data'
