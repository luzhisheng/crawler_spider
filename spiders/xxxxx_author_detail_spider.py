from requests.exceptions import SSLError, ProxyError, ChunkedEncodingError, ConnectionError
from spiders.spider_base import SpiderBase
from settings import xxxxx_AY_SIGN
import requests
import json


class xxxxxDyAuthorDetailSpider(SpiderBase):
    name = 'xxxxx_dy_author_detail'

    def __init__(self):
        super(xxxxxDyAuthorDetailSpider, self).__init__()
        self.table = self.name
        self.project_table = 'project_' + self.table

    def init_requests(self, payload_get, payload_post):
        try:
            url = payload_get
            authtoken = self.get_xxxxx_dy_sign('table', xxxxx_AY_SIGN)
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

        msg = content.get('msg')
        if msg == '达人不存在':
            sql = f"update {self.project_table} set status = -2 WHERE task_id='{task_id}'" \
                  f" and deduplication = '{deduplication}';"
            self.eb_supports.do(sql)
            return None, self.table, deduplication

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
            self.close_spider(self.table, task_id, 1)
            return True, self.table, deduplication
        else:
            return False, self.table, deduplication

    def run(self, req):
        try:
            import time
            time.sleep(0.3)
            exists, self.table, deduplication = self.get_html(req[0])
            return exists, self.table, deduplication
        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError, ValueError) as e:
            raise ValueError(e)


if __name__ == '__main__':
    a = xxxxxDyAuthorDetailSpider()
    sql = f"""
        select task_id, payload_get, payload_post, deduplication from project_xxxxx_dy_author_detail where 
        task_id='project_xxxxx_dy_live-16914038810963438' and deduplication='authorId=3817982232635758' and status=2;
    """
    raw = a.eb_supports.query(sql)
    a.run(raw)
