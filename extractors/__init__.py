import pkgutil
import os
import pyclbr

pkg_dir = os.path.dirname(os.path.realpath(__file__))

excluded_extractors = ('Base',)
extractors = set()

for (module_loader, name, _) in pkgutil.iter_modules([pkg_dir]):
    dct = pyclbr.readmodule_ex(name, path=[module_loader.path])
    for key in dct:
        if key not in excluded_extractors and key.endswith('Extractor'):
            extractors.add((name, key))

__extractors__ = list(extractors)
