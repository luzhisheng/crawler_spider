from receivers.item_handler import ItemHandler
from extractors import __extractors__ as common_extractor
from spiders import __spiders__ as common_spider
from abc import ABCMeta, abstractmethod
from base import Base
import importlib


CLS_DICT = {'extractors': common_extractor}
SID_DICT = {'spiders': common_spider}


class BaseReceiver(Base):

    __meta_class__ = ABCMeta

    def __init__(self):
        super(BaseReceiver, self).__init__()
        self.item_handler = ItemHandler()
        self.extractors = {}
        self.spiders = {}

        for cls_mod, ex_list in CLS_DICT.items():
            for mod, klass in ex_list:
                module = importlib.import_module('{}.{}'.format(cls_mod, mod))
                klass = getattr(module, klass)
                self.extractors[klass.name] = klass

        for cls_mod, ex_list in SID_DICT.items():
            for mod, klass in ex_list:
                module = importlib.import_module('{}.{}'.format(cls_mod, mod))
                klass = getattr(module, klass)
                self.spiders[klass.name] = klass

    @abstractmethod
    def receive(self):
        pass
