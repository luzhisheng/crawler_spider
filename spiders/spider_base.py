from base import Base
from dao.redis_dao import MyRedis
from settings import REDIS_EXTRACTOR_QUEUE, REDIS_SPIDER_QUEUE
import json


class SpiderBase(Base):

    def __init__(self):
        super(SpiderBase, self).__init__()
        self.producer = MyRedis()

    def get_sign(self, table, task_id):
        sql = f"SELECT data FROM {table} WHERE task_id = '{task_id}' limit 1"
        msg = self.eb_supports.query(sql)
        return msg

    def close_spider(self, table, task_id, retry_cnt):
        # 将蜘蛛消息推送到队列
        data = {'table': table, 'task_id': task_id, 'retry_cnt': retry_cnt}
        content = {'type': 'raw', 'data': data}
        self.producer.push(REDIS_EXTRACTOR_QUEUE, json.dumps(content))


if __name__ == '__main__':
    sb = SpiderBase()
    sb.close_spider('xxxxx_dy_live_room_goods', 'project_xxxxx_dy_live-2023_06_19_11_49_22', 1)
    # sb.start_spider('xxxxx_dy_live_room_flow_info', 1)
