# -*-  coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'transdb',
    version = '0.91',
    packages = ['transdb'],
    include_package_data = True,
    license = 'LGPL 3.0', # example license
    description = 'Django\'s field that stores labels in more than one language in database.',
    long_description = README,
    url = 'https://github.com/intelligenia/transdb',
    author = 'Diego J. Romero López',
    author_email = 'diego@intelligenia.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL 3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
