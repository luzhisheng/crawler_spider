import json
import time

from requests.exceptions import SSLError, ProxyError, ChunkedEncodingError, ConnectionError
from multiprocessing import Queue
from spiders.spider_base import SpiderBase
import requests


class DaduoduoDyAuthorDetailSpider(SpiderBase):
    name = 'daduoduo_dy_author_detail'

    def __init__(self):
        super(DaduoduoDyAuthorDetailSpider, self).__init__()
        queue = Queue()
        self.project_list = queue
        self.table = self.name
        self.project_table = 'project_' + self.table
        self.flag = 0

    def put_item(self):
        try:
            sql = f"SELECT task_id, payload_get, payload_post, deduplication FROM {self.project_table} " \
                  f"WHERE status = 0 ORDER BY weight DESC limit 10"
            msg = self.eb_supports.query(sql)
            if msg:
                for i in msg:
                    sql = f'update {self.project_table} set status = 1 ' \
                          f'where task_id="{i[0]}" and deduplication = "{i[3]}";'
                    self.eb_supports.do(sql)
                    self.project_list.put(i)
            elif not msg:
                sql = f"update {self.project_table} set status = 0 where status = 1;"
                row_cnt = self.eb_supports.do(sql)
                self.log(f"重置任务-{self.project_table}-{row_cnt}个")
                return '找不到资源'
        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError):
            return "put_item 握手失败"

    def init_requests(self, payload_get, payload_post):
        try:
            url = payload_get
            authtoken = self.get_sign(table='daduoduo_dy_sign', task_id='daduoduo_dy_sign_1')
            headers = {'authtoken': authtoken[0][0]}
            response = requests.request("GET", url=url, headers=headers)
            response_json = response.json()
        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError):
            return -1
        return response_json

    def get_html(self, project_item):
        # task_id, payload_get, payload_post, deduplication
        task_id = project_item[0]
        payload_get = project_item[1]
        payload_post = project_item[2]
        deduplication = project_item[3]

        content = self.init_requests(payload_get, payload_post)
        if content == -1:
            raise ValueError(f"init_requests 握手失败")

        list_dicts = []
        data = content.get('data')
        item = {
            "task_id": task_id,
            "data": json.dumps(data),
            "deduplication": deduplication,
        }
        list_dicts.append(item)
        db_res = self.eb_supports.insert_many(self.table, list_dicts)

        if db_res >= 0:
            sql = f"update {self.project_table} set status = 2 WHERE task_id='{task_id}'" \
                  f" and deduplication = '{deduplication}';"
            self.eb_supports.do(sql)
            self.log(f"入库成功 {task_id}-{deduplication}")
            self.close_spider(self.table, task_id, 1)

    def run(self):
        while True:
            time.sleep(0.2)
            if self.project_list.qsize() > 0:
                try:
                    self.get_html(self.project_list.get())
                    self.flag = 0
                except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError, ValueError) as e:
                    raise ValueError(e)
            else:
                res = self.put_item()
                if "找不到资源" == res:
                    self.flag += 1
                    self.log(f"找不到资源-{self.flag}")
                    if self.flag == 2:
                        break
                elif "put_item 握手失败" == res:
                    raise ValueError(f"init_requests 握手失败")


if __name__ == '__main__':
    a = DaduoduoDyAuthorDetailSpider()
    a.run()
