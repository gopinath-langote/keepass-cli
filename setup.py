from distutils.core import setup

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def requirements():
    with open('requirements.txt') as f:
        install_requires = [line.strip() for line in f]

    # Terminal colors for Windows
    if 'win32' in sys.platform.lower():
        install_requires.append('colorama')

    return install_requires


setup(
    name='KeePass',
    url='',
    license='',
    install_requires=requirements(),
    entry_points={'console_scripts': ['keepcli = Main.__main__:main']},
    author='gopinathlangote',
    packages=['KeePass'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    include_package_data=True,
    author_email='',
    description=''
)
