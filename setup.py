"""
Created by Nathan Buckner
"""

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="concordance",
    version="0.0.1",
    description="Simple concordance repo",
    long_description=read("README.md"),
    author="Nathan Buckner",
    author_email="bucknerns@gmail.com",
    url="http://github.com/bucknerns/concordance",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("pip-requires").split("\n"),
    license=open("LICENSE").read(),
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python"),
    entry_points = {
        'console_scripts':
        ['create_concordance = concordance.drivers.runner:entry_point']})
