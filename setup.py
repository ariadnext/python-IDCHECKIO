import os
import re
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'idcheckio',
]

requires = [
    'requests',
]
test_requirements = []

setup(
    name='idcheckio',
    version='0.0.6',
    description='Python IDCheckIO library',
    long_description='See on https://github.com/ariadnext/IDCheckIO',
    author='Denis Jagoudel',
    author_email='denis.jagoudel@ariadnext.com',
    url='https://idcheck.io',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'idcheckio': ['*.pem']},
    package_dir={'idcheckio': 'idcheckio'},
    include_package_data=True,
    install_requires=requires,
    license='None',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    cmdclass={},
    tests_require=test_requirements,
    extras_require={},
)
