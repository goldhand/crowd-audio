# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import crowd_audio
version = crowd_audio.__version__

setup(
    name='crowd_audio',
    version=version,
    author='',
    author_email='will@django.nu',
    packages=[
        'crowd_audio',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['crowd_audio/manage.py'],
)