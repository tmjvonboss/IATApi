from __future__ import with_statement
import re

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

# detect the current version
with open('line_api/__init__.py') as f:
    version = re.search(r'__version__\s*=\s*\'(.+?)\'', f.read()).group(1)
assert version

import codecs
with codecs.open('README.md','r',encoding='utf8') as f:
    setup(
        name='IATApi',
        packages=['IATApi'],
        version=version,
        description='Google Vision api made by bunnies, for bunnies...',
        long_description=f.read(),
        license='Bunny License',
        author='BUNNY TMJ',
        author_email='jackzett10@gmail.com',
        url='',
        keywords=['google-vision'],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        install_requires=[
            'requests',
            'aiohttp',
            'aiofiles',
            'asyncio'
        ],
    )