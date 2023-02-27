from requests.exceptions import SSLError, ProxyError, ChunkedEncodingError, ConnectionError
from multiprocessing import Queue
from spider.base import Base
import requests
import time
import random
import json
import re


class 京东商品评论爬虫(Base):

    def __init__(self):
        super(京东商品评论爬虫, self).__init__()
        self.project_list = Queue()
        self.table = "jd_comment_product_page_comments_action"
        self.project_table = "project_jd_comment_product_page_comments_action"
        self.flag = 0

    def put_item(self):
        try:
            sql = f"SELECT project_id, keyword, productId, payload FROM {self.project_table} WHERE status = 0 limit 10"
            msg = self.eb_supports.query(sql)
            if msg:
                for i in msg:
                    sql = f'update {self.project_table} set status = 1 ' \
                          f'where project_id="{i[0]}" and productId = "{i[2]}";'
                    self.eb_supports.do(sql)
                    self.project_list.put(i)
            elif not msg:
                sql = f"update {self.project_table} set status = 0 where status = 1;"
                row_cnt = self.eb_supports.do(sql)
                self.log(f"重置任务-{self.project_table}-{row_cnt}个")
                return '找不到资源'
        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError):
            self.log(f"put_item 握手失败")
            return -2

    def init_requests(self, payload, page):
        try:
            payload = payload.replace('page_num', str(page))
            url = f"https://club.jd.com/comment/productPageComments.action?" + payload
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/108.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
                'referer': 'https://item.jd.com/',
                'Cookie': f'__jdu={round(time.time() * 1000)}1922069937'
            }
            response = requests.request("GET", url=url, headers=headers)
            response_text = response.text
            response_text = re.findall(r'fetchJSON_comment98\((.*)\)', response_text)[0]
            content = json.loads(response_text)
            if not content.get('comments'):
                self.log(f"comments 空")
                return -1

        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError):
            self.log(f"init_requests 握手失败")
            return -2
        return response_text

    def get_html(self, project_item):
        project_id = project_item[0]
        keyword = project_item[1]
        productId = project_item[2]
        payload = project_item[3]

        for page in range(1, 99):
            content = self.init_requests(payload, page)
            if content == -1:
                sql = f"update {self.project_table} set status = -2 WHERE project_id='{project_id}'" \
                      f" and productId = '{productId}';"
                self.eb_supports.do(sql)
                self.log(f"更新 {productId}")
                break
            if content == -2:
                raise ValueError(f"init_requests 握手失败")
            list_dicts = []
            item = {
                "project_id": project_id,
                "keyword": keyword,
                "product_id": productId,
                "page": page,
                "data": content
            }
            list_dicts.append(item)
            db_res = self.eb_supports.insert_many(self.table, list_dicts)

            if db_res >= 0:
                sql = f"update {self.project_table} set status = 2 WHERE project_id='{project_id}'" \
                      f" and productId = '{productId}';"
                self.eb_supports.do(sql)
                self.log(f"入库成功 {productId}")
            time.sleep(random.randint(3, 6))

    def run(self):
        while True:
            time.sleep(random.randint(3, 6))
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
                    if self.flag == 5:
                        break


if __name__ == '__main__':
    a = 京东商品评论爬虫()
    a.run()
