import os

mysql_server = {
    "host": "",
    "user": "",
    "password": "",
    "db": "",
    "port": 3306,
    "charset": "utf8mb4"
}

mysql_server_172 = {
    "host": "",
    "user": "",
    "password": "",
    "db": "eb_supports_jd",
    "port": 3306,
    "charset": "utf8mb4"
}

DOCS_PATH = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(DOCS_PATH, 'docs/')
stop_file_path = excel_path + "stopwords.txt"
