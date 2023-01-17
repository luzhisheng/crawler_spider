from dao.mysql_dao import StoreMysqlPool
from pymysql.err import OperationalError
from datetime import datetime
import platform
import settings


class Base(object):

    def __init__(self):
        try:
            if "Linux-5.0.0" in platform.platform() or 'Ubuntu' in platform.platform():
                self.eb_supports = StoreMysqlPool(**settings.mysql_server)
            else:
                self.eb_supports = StoreMysqlPool(**settings.mysql_server_172)
        except OperationalError:
            self.eb_supports = StoreMysqlPool(**settings.mysql_server)

    def log(self, s):
        print('【%s】 %s' % (datetime.now(), s), flush=True)
