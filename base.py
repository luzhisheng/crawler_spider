from dao.mysql_dao import StoreMysqlPool
from dao.redis_dao import MyRedis
from datetime import datetime
import settings
import json


class Base(object):

    def __init__(self):
        self.producer = MyRedis()
        self.eb_supports = StoreMysqlPool(**settings.mysql_server_xxxxx)

    def log(self, s):
        print('【%s】 %s' % (datetime.now(), s), flush=True)

    def start_spider(self, table, retry_cnt, **kwargs):
        # 将蜘蛛消息推送到队列
        data = kwargs
        data['table'] = table
        data['retry_cnt'] = retry_cnt
        content = {'type': 'raw', 'data': data}
        self.producer.push(settings.REDIS_SPIDER_QUEUE, json.dumps(content))


if __name__ == '__main__':
    sb = Base()
    my_dict = {
        "task_id": "project_xxxxx_dy_author_detail-2023_08_08_10_51_21",
        "deduplication": "authorId=100000092952"
    }
    sb.start_spider('xxxxx_dy_author_detail', 1, **my_dict)
