#!/usr/bin/env python
#from distutils.core import setup
import setuptools
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', ]
test_requirements = ['pytest>=3', ]

setup(
    author="Gezahegne Wondachew",
    email="enggezahegn.w@gmail.com",
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Rossmann Pharmaceuticals Sales Prediction",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='modules',
    name='pharma_sales_pridiction',

    test_suite='test',
    tests_require=test_requirements,
    url='https://github.com/gezish/pharma_sales_pridiction',
    version='0.1.0',
    zip_safe=False,
)
