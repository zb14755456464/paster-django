#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""The setup script."""

from os import path

from pkg_resources import yield_lines
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    install_requires = list(yield_lines(f.read()))

with open(path.join(here, 'test-requirements.txt')) as f:
    tests_require = list(yield_lines(f.read()))

setup(
    packages=find_packages(
        include=[
            'lico*',
        ]
    ),
    namespace_packages=['lico', 'lico.job'],
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'deploy = lico.job.test_app.cmd:main'
        ],
        'paste.app_factory': [
            'main = lico.job.test_app.factory:make_application'
        ],
    }
)