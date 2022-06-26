# -*- coding: utf-8 -*-
import codecs
import os
from setuptools import setup, find_packages

from marc import __app_name__, __version__

here = os.path.dirname(os.path.abspath(__file__))

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requirements = [
        line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')
    ]

setup(
    name=__app_name__,
    version=__version__,
    description='TODO:',
    long_description=readme,
    license=license,
    install_requires=install_requirements,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    py_modules=['marc'],
    entry_points='''
        [console_scripts]
        marc=marc.main:cli
    ''',
)
