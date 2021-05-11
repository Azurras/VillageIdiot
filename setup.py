#!usr/bin/env python3

from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    author='Flush Media',
    author_email='',
    data_files=['.env'],
    description='A discord bot to find idiots',
    keywords=['villageidiot'],
    install_requires=requirements,
    license='MIT',
    name='villageidiot',
    packages=['villageidiot'],
    package_dir={'villageidiot': 'villageidiot'},
    version='1.0.0',
    url='https://github.com/Flush-Media/Village-Idiot-Locator.git',

    entry_points={'console_scripts': [
        'villageidiot = villageidiot.__main__:main',
    ], },
)
