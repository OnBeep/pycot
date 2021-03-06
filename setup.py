#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Python Cursor on Target Module.

:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2020 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/pycot>
"""

import os
import setuptools
import sys

__title__ = 'pycot'
__version__ = '2.5.1'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    version=__version__,
    name=__title__,
    packages=[__title__],
    package_dir={__title__: __title__},
    url=f'https://github.com/ampledata/{__title__}',
    description='Python Cursor on Target Module.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    package_data={'': ['LICENSE']},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'gexml >= 1.0.0'
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Cursor on Target', 'ATAK'
    ]
)
