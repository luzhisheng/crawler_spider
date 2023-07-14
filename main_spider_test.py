from spiders.xxxxxxxxxxx import xxxxxxxxxxx

from datetime import datetime
import time


def log(s):
    print('【%s】 %s' % (datetime.now(), s), flush=True)


def jop():
    while True:
        try:
            log('xxxxxxxxxxx爬虫-开始')
            a = xxxxxxxxxxx()
            a.run()
            log('xxxxxxxxxxx爬虫-结束')
            time.sleep(10)
        except Exception as e:
            log(e)
            time.sleep(10)


if __name__ == '__main__':
    jop()
