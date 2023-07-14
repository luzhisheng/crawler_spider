from base import Base
import datetime


class 创建达多多达人主播简介任务爬虫(Base):

    def __init__(self):
        super(创建达多多达人主播简介任务爬虫, self).__init__()
        self.project_table = 'project_daduoduo_dy_author_detail'

    def project(self, tasks: list):
        """
        :param tasks:[{brand_code:, search_keyword:}]
        :return:
        search_keyword: 多组关键词用空格分隔
        """
        list_dict = []
        for task in tasks:
            task_id = task.get("task_id")
            userId = task.get("userId")
            payload = f"https://www.daduoduo.com/ajax/dyPeopleDetailAjax.ashx?action=GetPeopleDetail&authorId={userId}"
            item = {
                "task_id": task_id,
                "payload_get": payload,
                "payload_post": '',
                'deduplication': f"authorId={userId}"
            }
            list_dict.append(item)
        cnt = self.eb_supports.insert_many(self.project_table, list_dict)
        if cnt >= 0:
            self.log(f"成功插入{self.project_table}任务-{cnt}")


if __name__ == '__main__':
    now = datetime.datetime.now()
    date = now.strftime('%Y_%m_%d_%H_%M_%S')
    task_id = f'project_daduoduo_dy_author_detail-{date}'
    d = 创建达多多达人主播简介任务爬虫()
    weight = 1
    offset = 0
    while True:
        sql = f"""
            SELECT
                distinct UserId 
            FROM
                clean_daduoduo_dy_author_search_list 
            WHERE
                UserId NOT IN (
                SELECT
                    UserId 
                FROM
                clean_daduoduo_dy_author_detail 
                )
            LIMIT 1000 OFFSET {offset}
        """
        msg = d.eb_supports.query(sql)
        list_dict = []
        for data in msg:
            userId = data[0]
            item = {"task_id": task_id, "userId": userId, "weight": weight}
            list_dict.append(item)
        if list_dict:
            d.project(list_dict)
        else:
            break
        offset += 1000
