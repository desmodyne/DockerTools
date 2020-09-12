#!/usr/bin/env python
# encoding: utf-8

"""
setup.py

DockerTools Python package installation script

author  : stefan schablowski
contact : stefan.schablowski@desmodyne.com
created : 2020-11-12
"""


# https://docs.python.org/3/distutils/setupscript.html
# https://docs.python.org/3/distutils/introduction.html#a-simple-example


from distutils.core import setup


setup(name='dockertools',
      version='0.0.6',
      packages=['dockertools'],
      package_dir={'dockertools': 'code/python'},
      py_modules=['dockertools.dd-dt-run-remote'])
