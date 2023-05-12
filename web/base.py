from dao.mysql_dao import StoreMysqlPool
from pymysql.err import OperationalError
import platform
import settings


try:
    if "window" in platform.platform():
        eb_supports = StoreMysqlPool(**settings.mysql_server)
    else:
        eb_supports = StoreMysqlPool(**settings.mysql_server_127)
except OperationalError:
    eb_supports = StoreMysqlPool(**settings.mysql_server)
