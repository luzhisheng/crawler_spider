from receivers.base_receiver import BaseReceiver
from settings import REDIS_EXTRACTOR_QUEUE, REDIS_SPIDER_QUEUE
from dao.redis_dao import MyRedis
import traceback
import json

QUIT = False


class RedisReceiver(BaseReceiver):

    def __init__(self):
        super(RedisReceiver, self).__init__()
        self.conn = MyRedis().redis_conn

    def retry_proccess(self, res):
        retry_cnt = res.get('retry_cnt')
        table = res.get('table')
        task_id = res.get('task_id')
        retry_cnt += 1
        data = {'table': table, 'task_id': task_id, 'retry_cnt': retry_cnt}
        content = {'type': 'raw', 'data': data}
        self.conn.rpush(REDIS_EXTRACTOR_QUEUE, json.dumps(content))
        self.log("重试消息已发送. {}: {} , count: {}".format(table, task_id, retry_cnt))

    def retry_proccess_spider(self, res):
        retry_cnt = res.get('retry_cnt')
        table = res.get('table')
        retry_cnt += 1
        data = {'table': table, 'retry_cnt': retry_cnt}
        content = {'type': 'raw', 'data': data}
        self.conn.rpush(REDIS_SPIDER_QUEUE, json.dumps(content))
        self.log("重试消息已发送. {} , count: {}".format(table, retry_cnt))

    def get_process_list(self, msgs):
        msg = json.loads(msgs[1])
        table = msg.get('data').get('table')
        task_id = msg.get('data').get('task_id')
        retry_cnt = msg.get('data').get('retry_cnt')
        if task_id and self.extractors.get(table, ''):
            yield table, task_id, self.extractors[table](), retry_cnt
        else:
            yield

    def get_process_list_spider(self, msgs):
        msg = json.loads(msgs[1])
        table = msg.get('data').get('table')
        retry_cnt = msg.get('data').get('retry_cnt')
        if self.spiders.get(table, ''):
            yield table, self.spiders[table](), retry_cnt
        else:
            yield

    def receive_extrator(self):
        self.log('开始接收...')
        self.log('--------- redis清洗消费者正在运行 --------')
        while not QUIT:
            packed = self.conn.blpop([REDIS_EXTRACTOR_QUEUE], 5)
            if not packed:
                continue
            try:
                process_list = self.get_process_list(packed)
                results = self.item_handler.process_items(process_list)
                for res in results:
                    status = res.get('status')
                    if status == 'error':
                        self.retry_proccess(res)
            except Exception as err:
                traceback.print_exc(err)

    def receive_spider(self):
        self.log('开始接收...')
        self.log('--------- redis爬虫消费者正在运行 --------')
        while not QUIT:
            packed = self.conn.blpop([REDIS_SPIDER_QUEUE], 5)
            if not packed:
                continue
            try:
                process_list = self.get_process_list_spider(packed)
                results = self.item_handler.process_items_spider(process_list)
                for res in results:
                    status = res.get('status')
                    if status == 'error':
                        self.retry_proccess_spider(res)
            except Exception as err:
                traceback.print_exc(err)
