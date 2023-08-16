from gevent import Greenlet
import gevent
import gevent.monkey
from base import Base

gevent.monkey.patch_all(thread=False, select=False)


class ItemHandler(Base):

    def __init__(self):
        super(ItemHandler, self).__init__()

    def process_single_item(self, table, task_id, extractor, retry_cnt):
        sql = f"""
            select task_id, data, deduplication, update_time from {table} where task_id='{task_id}';
        """
        raw = self.eb_supports.query(sql)
        if not raw:
            self.log(f"结果表为空-{table}-{task_id}")
        task_id, data, deduplication, update_time = raw[0]
        result = {'task_id': task_id, 'table': extractor.name, 'retry_cnt': retry_cnt, 'status': 0}
        try:
            exists, table, db_res = extractor.process_item(raw)
            if exists:
                self.log(f"解析数据-入库成功-{table}-{db_res}")
            else:
                self.log(f"解析数据-入库失败-{table}-{db_res}")
                result['status'] = 'error'
            result['deduplication'] = deduplication
            return result
        except Exception as e:
            self.log(e)
            result['deduplication'] = deduplication
            result['status'] = 'error'
            return result

    def process_items(self, process_list):
        extraction_jobs = [Greenlet.spawn(self.process_single_item, item[0], item[1], item[2], item[3])
                           for item in process_list]
        gevent.joinall(extraction_jobs, timeout=15)
        return (job.value for job in extraction_jobs if job.value)

    def process_single_item_spider(self, table, spiders, retry_cnt, task_id, deduplication):
        project_table = 'project_' + table
        sql = f"""
            select task_id, payload_get, payload_post, deduplication from {project_table} where task_id='{task_id}' 
            and deduplication='{deduplication}';
        """
        raw = self.eb_supports.query(sql)
        result = {'task_id': task_id, 'deduplication': deduplication, 'table': spiders.name, 'retry_cnt': retry_cnt,
                  'status': 0}
        try:
            if not raw:
                self.log(f"任务表为空-{table}-{deduplication}")
                return result
            exists, table, deduplication = spiders.run(raw)
            if exists is None:
                self.log(f"数据为空 {table}-{deduplication}")
            elif exists:
                self.log(f"元数据-入库成功-{table}-{deduplication}")
            else:
                self.log(f"元数据-入库失败-{table}-{deduplication}")
                result['status'] = 'error'
            result['deduplication'] = deduplication
            return result
        except Exception as e:
            self.log(e)
            result['deduplication'] = deduplication
            result['status'] = 'error'
            return result

    def process_items_spider(self, process_list):
        item = []
        for i in process_list:
            item = i
        result = [self.process_single_item_spider(item[0], item[1], item[2], item[3], item[4])]
        return result
