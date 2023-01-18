from werkzeug.security import generate_password_hash


mysql_server = {
    "host": "55.555.55.555",
    "user": "",
    "password": "",
    "db": "",
    "port": 3306,
    "charset": "utf8mb4"
}

mysql_server_172 = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "db": "",
    "port": 3306,
    "charset": "utf8mb4"
}


USERS = [
    {
        "id": 1,
        "name": 'admin',
        "password": generate_password_hash('123456789')
    },
    {
        "id": 2,
        "name": 'tom',
        "password": generate_password_hash('123456789')
    }
]
