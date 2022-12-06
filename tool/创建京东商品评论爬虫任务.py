from tool.base import Base
from urllib.parse import urlparse


class 创建京东商品评论爬虫任务(Base):

    def __init__(self):
        super(创建京东商品评论爬虫任务, self).__init__()

    def project(self, tasks: list):
        """
        :param tasks:[{project_name:, aweme_id:}]
        :return:
        chanmama_aweme_id: 蝉妈妈视频的ID
        新建任务
        """
        list_dict = []
        for task in tasks:
            project_id = task.get("project_id")
            keyword = task.get("keyword")
            url = task.get("url")
            url_path = urlparse(url).path
            product_id = url_path.split("/")[1].replace('.html', '')
            payload = f"callback=fetchJSON_comment98&productId={product_id}&score=0&sortType=5&page=page_num" \
                      f"&pageSize=10&isShadowSku=0&rid=0&fold=1"
            item = {
                "project_id": project_id,
                "keyword": keyword,
                "productId": product_id,
                "payload": payload,
            }
            list_dict.append(item)
        cnt = self.eb_supports.insert_many("project_jd_comment_product_page_comments_action", list_dict)
        print(cnt)


if __name__ == '__main__':
    d = 创建京东商品评论爬虫任务()
    list_dict = []
    task_id = 'dzx-110000'
    sql = f"SELECT project_id, keyword, url FROM jd_search_keyword where project_id = '{task_id}'"
    res = d.eb_supports.query(sql)
    for project_id, keyword, url in res:
        item = {"project_id": project_id, "keyword": keyword, "url": url}
        list_dict.append(item)
    d.project(list_dict)
