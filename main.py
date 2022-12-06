from spider.京东搜索列表页面爬虫 import 京东搜索列表页面爬虫
from spider.京东商品评论爬虫 import 京东商品评论爬虫
from tool.创建京东商品评论爬虫任务 import 创建京东商品评论爬虫任务


def jop():
    a = 京东搜索列表页面爬虫()
    a.run()

    d = 创建京东商品评论爬虫任务()
    list_dict = []
    task_id = 'dzx-110000'
    sql = f"SELECT project_id, keyword, url FROM jd_search_keyword where project_id = '{task_id}'"
    res = d.eb_supports.query(sql)
    for project_id, keyword, url in res:
        item = {"project_id": project_id, "keyword": keyword, "url": url}
        list_dict.append(item)
    d.project(list_dict)

    b = 京东商品评论爬虫()
    b.run()


if __name__ == '__main__':
    jop()
