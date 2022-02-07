##########################################################################
# Copyright (c) 2010-2021 Robert Bosch GmbH
#
# This source code is copyright protected and proprietary
# to Robert Bosch GmbH. Only those rights that have been
# explicitly granted to you by Robert Bosch GmbH in written
# form may be exercised. All other rights remain with
# Robert Bosch GmbH.
##########################################################################

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


install_requirements = [
    "black>=19.3b0",
    "grpclib>=0.4.1, <1.0.0",
    "jinja2>=2.11.2, <3.0.0",
    "python-dateutil>=2.8, <3.0.0",
]

setup(
    name="betterproto",
    version="2.0.0b4",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=install_requirements,
    setup_requires=[],
    entry_points={"console_scripts": ["protoc-gen-python_betterproto = betterproto.plugin:main"]},
)
