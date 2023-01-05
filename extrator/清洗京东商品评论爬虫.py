from extrator.base import Base
import json


class 清洗京东商品评论爬虫(Base):

    def __init__(self):
        super(清洗京东商品评论爬虫, self).__init__()

    def clean(self, project_id):
        offset = 0
        while True:
            list_res = []
            sql = f"""
                select project_id, keyword, product_id, page, data from jd_comment_product_page_comments_action where
                 project_id = '{project_id}' and status = 0 LIMIT 200 OFFSET {offset};
            """
            self.log(f"执行的sql{sql}")
            res = self.eb_supports.query(sql)

            if not res:
                break

            for project_id, keyword, product_id, page, data in res:
                data_json = json.loads(data)
                comments = data_json.get('comments')
                for comment in comments:
                    current_month = comment.get('creationTime')
                    month = str(current_month).split('-')[1]

                    item = {
                        "project_id": project_id,
                        "keyword": keyword,
                        "product_id": product_id,
                        "comments_id": comment.get('id'),
                        "content": comment.get('content'),
                        "score": comment.get('score'),
                        "nick_name": comment.get('nickname'),
                        "reply_count": comment.get('replyCount'),
                        "useful_vote_count": comment.get('usefulVoteCount'),
                        "creation_time": comment.get('creationTime'),
                        "month": month,
                        "product_color": comment.get('productColor')
                    }
                    list_res.append(item)
            db_res = self.eb_supports.insert_many('clean_jd_comment_product_page_comments_action', list_res)
            if db_res >= 0:
                self.log(f"入库成功 {db_res}")
            offset += 200

        sql = f"""
        update jd_comment_product_page_comments_action set status = 2
        """
        self.log(f"执行的sql{sql}")
        self.eb_supports.query(sql)

    def run(self, project_id):
        self.clean(project_id)


if __name__ == '__main__':
    project_id = 'dzx-110000'
    qc = 清洗京东商品评论爬虫()
    qc.run(project_id)
