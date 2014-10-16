import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


setup(
    name='heka-py',
    version='0.30.3',
    description="Metrics Logging",
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
    keywords='heka metrics logging client',
    author='Rob Miller',
    author_email='rmiller@mozilla.com',
    url='https://github.com/mozilla-services/heka-py',
    license='MPLv2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'protobuf',
    ],
    tests_require=[
        'mock',
        'pytest',
    ],
)
