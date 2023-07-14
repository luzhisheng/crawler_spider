from base import Base
import json


class CleanDaduoduoDyAuthorDetailExtractor(Base):
    name = 'daduoduo_dy_author_detail'

    def __init__(self):
        super(CleanDaduoduoDyAuthorDetailExtractor, self).__init__()
        self.table = self.name
        self.clean_table = "clean_" + self.table

    def process_item(self, resp):
        list_res = []
        if not resp:
            self.log(f'清洗{self.table}数据-达多多数据-不存在')
            return ''

        for task_id, data, deduplication, update_time in resp:
            data_json = json.loads(data)
            item = {
                "task_id": task_id,
                "updateTime": data_json.get('updateTime'),
                "Name": data_json.get('Name'),
                "HeaderImg": data_json.get('HeaderImg'),
                "DouYinId": data_json.get('DouYinId'),
                "SubDetail": data_json.get('SubDetail'),
                "FansCnt": data_json.get('FansCnt'),
                "FavCnt": data_json.get('FavCnt'),
                "Sex": data_json.get('Sex'),
                "IsShow": data_json.get('IsShow'),
                "Reputation": data_json.get('Reputation'),
                "City": data_json.get('City'),
                "CustomVerify": data_json.get('CustomVerify'),
                "McnName": data_json.get('McnName'),
                "EnterpriseVerify": data_json.get('EnterpriseVerify'),
                "WorksType": json.dumps(data_json.get('WorksType')),
                "MainSaleType": data_json.get('MainSaleType'),
                "SaleType": data_json.get('SaleType'),
                "UserId": data_json.get('UserId'),
                "McnId": data_json.get('McnId'),
                "SecUserId": data_json.get('SecUserId'),
                "HasGoodWindow": data_json.get('HasGoodWindow'),
                "HasLiveHistory": data_json.get('HasLiveHistory'),
                "ShopId": data_json.get('ShopId'),
                "ShopName": data_json.get('ShopName'),
                "ProductType": json.dumps(data_json.get('ProductType')),
                "isFav": data_json.get('isFav'),
                "RoomId": data_json.get('RoomId'),
                "UserLevel": data_json.get('UserLevel'),
                "roomGoodsFlag": data_json.get('roomGoodsFlag'),
                "awemeGoodsFlag": data_json.get('awemeGoodsFlag'),
                "fansMilestone": json.dumps(data_json.get('fansMilestone')),
                "deduplication": deduplication,
                "spider_time": update_time
            }
            list_res.append(item)
        db_res = self.eb_supports.insert_many(self.clean_table,
                                              list_res,
                                              conflict=["task_id", "updateTime", "Name", "HeaderImg",
                                                        "DouYinId", "SubDetail", "FansCnt", "FavCnt",
                                                        "Sex", "IsShow", "Reputation", "City",
                                                        "CustomVerify", "McnName", "EnterpriseVerify",
                                                        "WorksType", "MainSaleType", "SaleType", "UserId",
                                                        "McnId", "SecUserId", "HasGoodWindow", "HasLiveHistory",
                                                        "ShopId", "ShopName", "ProductType", "isFav", "RoomId",
                                                        "UserLevel", "roomGoodsFlag", "awemeGoodsFlag",
                                                        "fansMilestone", "deduplication", "spider_time"]
                                              )
        if db_res >= 0:
            return True, self.table, db_res
        else:
            return False, self.table, db_res


if __name__ == '__main__':
    offset = 0
    qc = CleanDaduoduoDyAuthorDetailExtractor()
    while True:
        sql = f"""
            select task_id, data, deduplication, update_time from daduoduo_dy_author_detail where
             date_sub(CURDATE(),INTERVAL 1 DAY) <= DATE(update_time) LIMIT 1000 OFFSET {offset};
        """
        res = qc.eb_supports.query(sql)
        if not res:
            break
        qc.process_item(res)
        offset += 1000
