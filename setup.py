from importlib.metadata import version

import numpy as np
from setuptools import setup, Extension

ext_modules = [
    Extension(
        'xtcocotools._mask',
        sources=['./common/maskApi.c', 'xtcocotools/_mask.pyx'],
        include_dirs=[np.get_include(), './common'],
        extra_compile_args=[]
    )
]

setup(
    ext_modules=ext_modules,
)
