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


# TODO: get metadata from elsewhere
# TODO: add classifiers: https://pypi.org/classifiers
setup(name='dockertools',
      version='0.0.7',
      description='Bash scripts to work with Docker containers',
      author='Stefan Schablowski',
      author_email='stefan.schablowski@desmodyne.com',
      url='https://github.com/desmodyne/DockerTools',
      project_urls={
        'Bug Tracker': 'https://github.com/desmodyne/DockerTools/issues',
        'Source Code': 'https://github.com/desmodyne/DockerTools',
      },
      license='MIT',
      scripts=['code/python/dd-dt-run-remote.py'])
