# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "TimeSeriesIoT"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0",
    "pymongo>=3.11.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="TimeSeries API IoT",
    author_email="",
    url="",
    keywords=["OpenAPI", "TimeSeries API IoT"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['TimeSeriesIoT=TimeSeriesIoT.__main__:main']},
    long_description="""\
    Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.
    """
)

