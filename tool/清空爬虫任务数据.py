from base import Base

base = Base()

project_table_list = [
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxx'
]

for project_table in project_table_list:
    sql = f"""
        truncate table {project_table};
    """
    msg = base.eb_supports.query(sql)

base.log('清空任务数据完成')
