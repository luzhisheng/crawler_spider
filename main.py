from spider.京东搜索列表页面爬虫 import 京东搜索列表页面爬虫
from spider.京东商品评论爬虫 import 京东商品评论爬虫
from tool.创建京东商品评论爬虫任务 import 创建京东商品评论爬虫任务
from extrator.清洗京东商品评论分词 import 清洗京东商品评论分词
from extrator.清洗京东商品评论爬虫 import 清洗京东商品评论爬虫
from extrator.清洗京东搜索列表页面爬虫 import 清洗京东搜索列表页面爬虫
from datetime import datetime


def log(s):
    print('【%s】 %s' % (datetime.now(), s), flush=True)


def jop():
    log('京东搜索列表页面爬虫-开始')
    a = 京东搜索列表页面爬虫()
    a.run()
    log('京东搜索列表页面爬虫-结束')

    log('创建京东商品评论爬虫任务-开始')
    d = 创建京东商品评论爬虫任务()
    list_dict = []
    task_id = 'dzx-110000'
    sql = f"SELECT project_id, keyword, url FROM jd_search_keyword where project_id = '{task_id}'"
    res = d.eb_supports.query(sql)
    for project_id, keyword, url in res:
        item = {"project_id": project_id, "keyword": keyword, "url": url}
        list_dict.append(item)
    d.project(list_dict)
    log('创建京东商品评论爬虫任务-结束')

    log('京东商品评论爬虫-开始')
    b = 京东商品评论爬虫()
    b.run()
    log('京东商品评论爬虫-结束')

    log('清洗京东搜索列表页面爬虫-开始')
    a = 清洗京东搜索列表页面爬虫()
    a.run()
    log('清洗京东搜索列表页面爬虫-结束')

    log('清洗京东商品评论分词-开始')
    a = 清洗京东商品评论分词()
    a.run()
    log('清洗京东商品评论分词-结束')

    log('清洗京东商品评论爬虫-开始')
    a = 清洗京东商品评论爬虫()
    a.run()
    log('清洗京东商品评论爬虫-结束')


if __name__ == '__main__':
    jop()
