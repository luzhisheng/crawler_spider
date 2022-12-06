from requests.exceptions import SSLError, ProxyError, ChunkedEncodingError, ConnectionError
from multiprocessing import Queue
from lxml import etree
from spider.base import Base
import requests
import time
import random


class 京东搜索列表页面爬虫(Base):

    def __init__(self):
        super(京东搜索列表页面爬虫, self).__init__()
        self.project_list = Queue()
        self.table = "jd_search_keyword"
        self.project_table = "project_jd_search_keyword"
        self.flag = 0

    def put_item(self):
        try:
            sql = f"SELECT project_id, keyword FROM {self.project_table} WHERE status = 0"
            msg = self.eb_supports.query(sql)
            if msg:
                for i in msg:
                    sql = f'update {self.project_table} set status = 1 ' \
                          f'where project_id="{i[0]}" and keyword = "{i[1]}";'
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

    def init_requests(self, keyword, page):

        try:
            url = f"https://search.jd.com/s_new.php?keyword={keyword}&page={page}"
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/108.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
            }
            response = requests.request("GET", url=url, headers=headers)
            content = response.text

        except (SSLError, ProxyError, ChunkedEncodingError, ConnectionError):
            self.log(f"init_requests 握手失败")
            return -2
        return content

    def get_html(self, project_item):
        project_id = project_item[0]
        keyword = project_item[1]

        for page in range(1, 88):
            content = self.init_requests(keyword, page)
            if content == -2:
                raise ValueError(f"init_requests 握手失败")
            selector = etree.HTML(content)
            etree_data = selector.xpath('//*[@class="gl-i-wrap"]')
            list_dicts = []
            for item in etree_data:
                item_str = etree.tostring(item)
                selector = etree.HTML(etree.tostring(item))
                url_list = selector.xpath('//div[@class="p-img"]/a/@href')
                for url in url_list:
                    item = {
                        "project_id": project_id,
                        "keyword": keyword,
                        "url": url,
                        "data": item_str
                    }
                    list_dicts.append(item)
            db_res = self.eb_supports.insert_many(self.table, list_dicts)

            if db_res >= 0:
                sql = f"update {self.project_table} set status = 2 WHERE project_id = '{project_id}';"
                self.eb_supports.do(sql)
                self.log(f"入库成功 {db_res}")

            time.sleep(10)

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
    a = 京东搜索列表页面爬虫()
    a.run()
