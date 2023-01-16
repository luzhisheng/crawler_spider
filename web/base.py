from dao.mysql_dao import StoreMysqlPool
from pymysql.err import OperationalError
import platform
import settings


try:
    if "Ubuntu" in platform.platform() or "Linux-5.0.0" in platform.platform():
        eb_supports = StoreMysqlPool(**settings.mysql_server)
    else:
        eb_supports = StoreMysqlPool(**settings.mysql_server_172)
except OperationalError:
    eb_supports = StoreMysqlPool(**settings.mysql_server)
