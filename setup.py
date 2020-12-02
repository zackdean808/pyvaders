#!/usr/bin/python3

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='PyVaders',
    version='2020.10.26',
    author='nixbytes',
    author_email='real8686@gmail.com',
    description='pyvaders is classic game of shooting the enemies by a Space ship',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nixbytes/pyvaders',
    packages=find_packages('src')
)
