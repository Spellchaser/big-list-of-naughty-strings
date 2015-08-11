from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='blns',
    version='0.1',
    url='https://github.com/danggrianto/big-list-of-naughty-strings',
    license='MIT',
    author='Daniel Anggrianto',
    author_email='daniel@anggrianto.com',
    description='Big List of Naughty String. Forked from https://github.com/minimaxir/big-list-of-naughty-strings',
    keywords='Big List of Naughty String',
    long_description=long_description,
    packages=['blns'],
    zip_safe=False,
    platforms='any',
)
