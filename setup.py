#!/usr/bin/env python

"""
The setup script for pip. Allows for `pip install -e .` installation.
"""

from setuptools import setup, find_packages

requirements = []
setup_requirements = []
tests_requirements = ['numpy', 'pytest']

setup(
    author='L. Cheng',
    author_email='cheng@cerfacs.fr',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8'
    ],
    description='Markdown to latex file converter',
    install_requires=requirements,
    license='GNU General Public License v3',
    long_description='\n\n',
    include_package_data=True,
    keywords='markdown latex converter',
    name='md2latex',
    packages=find_packages(include=['md2latex']),
    setup_requires=setup_requirements,

    test_suite='tests',
    tests_require=tests_requirements,
    version='0.1',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'md2latex=md2latex.main:convert'
        ],
    },
)
