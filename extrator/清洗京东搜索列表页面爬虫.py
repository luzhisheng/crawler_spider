from extrator.base import Base
from urllib.parse import urlparse
from lxml import etree


class 清洗京东搜索列表页面爬虫(Base):

    def __init__(self):
        super(清洗京东搜索列表页面爬虫, self).__init__()

    def clean(self, project_id):
        offset = 0
        while True:
            list_res = []
            sql = f"""
            select project_id, keyword, url, data from jd_search_keyword where project_id = '{project_id}'
             and status = 0 LIMIT 200 OFFSET {offset};
            """
            self.log(f"执行的sql{sql}")
            res = self.eb_supports.query(sql)
            if not res:
                break

            for project_id, keyword, url, data in res:
                selector = etree.HTML(data)
                title = selector.xpath('//div[contains(@class,"p-name")]/a/@title')[0]
                data_price = selector.xpath('//div[contains(@class,"p-price")]/strong/i/text()')[0]
                goods_icons = selector.xpath('//div[contains(@class,"p-icons")]/i/text()')
                shop_name = selector.xpath('//span[contains(@class,"J_im_icon")]/a/text()')

                url_path = urlparse(url).path
                product_id = url_path.split("/")[1].replace('.html', '')

                if shop_name:
                    shop_name = shop_name[0]
                else:
                    shop_name = ''

                item = {
                    "project_id": project_id,
                    "keyword": keyword,
                    "url": url,
                    "product_id": str(product_id),
                    "title": title,
                    "data_price": data_price,
                    "goods_icons": "/".join(goods_icons),
                    "shop_name": shop_name
                }
                list_res.append(item)
            db_res = self.eb_supports.insert_many('clean_jd_search_keyword', list_res)
            if db_res >= 0:
                self.log(f"入库成功 {db_res}")
            offset += 200

        sql = f"""
        update jd_search_keyword set status = 2
        """
        self.log(f"执行的sql{sql}")
        res = self.eb_supports.query(sql)

    def run(self, project_id):
        self.clean(project_id)


if __name__ == '__main__':
    project_id = 'dzx-110000'
    qc = 清洗京东搜索列表页面爬虫()
    qc.run(project_id)
