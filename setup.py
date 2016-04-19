# -*- cording: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NAME',
    'author': 'SeoSangho',
    'url': 'https://owlinux.github.com',
    'download_url': 'https://owlinux.github.com',
    'author_email': 'ssh0702@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
