from extrator.base import Base
from settings import stop_file_path
import pandas as pd
import jieba
import jieba.analyse
import json
import re

jieba.analyse.set_stop_words(stop_file_path)


class 清洗京东商品评论分词(Base):

    def __init__(self):
        super(清洗京东商品评论分词, self).__init__()

    def jieba_cut_article(self, article):
            # 清除特殊字符串
            article = re.sub(r"\[([^\[\]]*)\]", "", article)
            if article:
                clear_not_china_word = str(re.sub(r"[^a-zA-Z\u4e00-\u9fa5]", "", article))
                if clear_not_china_word:
                    data_cut_list = [str(i).lower() for i in jieba.cut(str(clear_not_china_word).strip()) if len(i) > 1]
                    cut_words = pd.Series(data_cut_list)
                    return cut_words.values
                else:
                    return []
            else:
                return []

    def clean(self, project_id):
        offset = 0
        while True:
            list_res = []
            sql = f"""
                select project_id, keyword, product_id, page, data from jd_comment_product_page_comments_action where
                 project_id = '{project_id}' LIMIT 200 OFFSET {offset};
            """
            self.log(f"执行的sql{sql}")
            res = self.eb_supports.query(sql)

            if not res:
                break

            for project_id, keyword, product_id, page, data in res:
                data_json = json.loads(data)
                comments = data_json.get('comments')
                for comment in comments:
                    content = comment.get('content')
                    keywords = self.jieba_cut_article(content)
                    for keyword in keywords:
                        item = {
                            "project_id": project_id,
                            "comments_id": comment.get('id'),
                            "cut": keyword
                        }
                        list_res.append(item)

            db_res = self.eb_supports.insert_many('clean_jd_comment_cuts', list_res)
            if db_res >= 0:
                self.log(f"入库成功 {db_res}")
            offset += 200

    def run(self, project_id):
        self.clean(project_id)


if __name__ == '__main__':
    project_id = 'dzx-110000'
    qc = 清洗京东商品评论分词()
    qc.run(project_id)
