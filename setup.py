import re
from setuptools import setup
from os import path

project_path = path.abspath(path.dirname(__file__))

with open(path.join(project_path, 'README.md')) as f:
    long_description = f.read()

setup(
    name = 'djangomosquito',
    packages = ['mosquito'],
    license = 'MIT',
    version = '0.0.1',
    description = 'Limit visitors to your django app by count',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = 'Sina Farhadi',
    author_email = 'sina.farhadi.cyber@gmail.com',
    url = 'https://github.com/E-RROR/django-mosquito/',
    keywords = ['django','visit','filter','limit','mosquito', 'django mosquito'],
    classifiers = [
        "Framework :: Django"
    ],
)
