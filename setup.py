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
    name='keepass',
    version='1.0',
    packages=['venv.lib.python2.7.distutils', 'venv.lib.python2.7.encodings', 'venv.lib.python2.7.site-packages.nmb',
              'venv.lib.python2.7.site-packages.pip', 'venv.lib.python2.7.site-packages.pip._vendor',
              'venv.lib.python2.7.site-packages.pip._vendor.idna',
              'venv.lib.python2.7.site-packages.pip._vendor.pytoml',
              'venv.lib.python2.7.site-packages.pip._vendor.certifi',
              'venv.lib.python2.7.site-packages.pip._vendor.chardet',
              'venv.lib.python2.7.site-packages.pip._vendor.chardet.cli',
              'venv.lib.python2.7.site-packages.pip._vendor.distlib',
              'venv.lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'venv.lib.python2.7.site-packages.pip._vendor.msgpack',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.util',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.contrib',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.packages',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.lib.python2.7.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.lib.python2.7.site-packages.pip._vendor.colorama',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib._trie',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib.python2.7.site-packages.pip._vendor.lockfile',
              'venv.lib.python2.7.site-packages.pip._vendor.progress',
              'venv.lib.python2.7.site-packages.pip._vendor.requests',
              'venv.lib.python2.7.site-packages.pip._vendor.packaging',
              'venv.lib.python2.7.site-packages.pip._vendor.cachecontrol',
              'venv.lib.python2.7.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib.python2.7.site-packages.pip._vendor.webencodings',
              'venv.lib.python2.7.site-packages.pip._vendor.pkg_resources',
              'venv.lib.python2.7.site-packages.pip._internal', 'venv.lib.python2.7.site-packages.pip._internal.req',
              'venv.lib.python2.7.site-packages.pip._internal.vcs',
              'venv.lib.python2.7.site-packages.pip._internal.utils',
              'venv.lib.python2.7.site-packages.pip._internal.models',
              'venv.lib.python2.7.site-packages.pip._internal.commands',
              'venv.lib.python2.7.site-packages.pip._internal.operations', 'venv.lib.python2.7.site-packages.smb',
              'venv.lib.python2.7.site-packages.smb.utils', 'venv.lib.python2.7.site-packages.lxml',
              'venv.lib.python2.7.site-packages.lxml.html', 'venv.lib.python2.7.site-packages.lxml.includes',
              'venv.lib.python2.7.site-packages.lxml.isoschematron', 'venv.lib.python2.7.site-packages.tests',
              'venv.lib.python2.7.site-packages.wheel', 'venv.lib.python2.7.site-packages.wheel.tool',
              'venv.lib.python2.7.site-packages.wheel.signatures', 'venv.lib.python2.7.site-packages.Crypto',
              'venv.lib.python2.7.site-packages.Crypto.IO', 'venv.lib.python2.7.site-packages.Crypto.Hash',
              'venv.lib.python2.7.site-packages.Crypto.Math', 'venv.lib.python2.7.site-packages.Crypto.Util',
              'venv.lib.python2.7.site-packages.Crypto.Cipher', 'venv.lib.python2.7.site-packages.Crypto.Random',
              'venv.lib.python2.7.site-packages.Crypto.Protocol', 'venv.lib.python2.7.site-packages.Crypto.SelfTest',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.IO',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Hash',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Math',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Util',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Cipher',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Random',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Protocol',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.PublicKey',
              'venv.lib.python2.7.site-packages.Crypto.SelfTest.Signature',
              'venv.lib.python2.7.site-packages.Crypto.PublicKey', 'venv.lib.python2.7.site-packages.Crypto.Signature',
              'venv.lib.python2.7.site-packages.pyasn1', 'venv.lib.python2.7.site-packages.pyasn1.type',
              'venv.lib.python2.7.site-packages.pyasn1.codec', 'venv.lib.python2.7.site-packages.pyasn1.codec.ber',
              'venv.lib.python2.7.site-packages.pyasn1.codec.cer', 'venv.lib.python2.7.site-packages.pyasn1.codec.der',
              'venv.lib.python2.7.site-packages.pyasn1.codec.native', 'venv.lib.python2.7.site-packages.pyasn1.compat',
              'venv.lib.python2.7.site-packages.colorama', 'venv.lib.python2.7.site-packages.dateutil',
              'venv.lib.python2.7.site-packages.dateutil.tz', 'venv.lib.python2.7.site-packages.dateutil.parser',
              'venv.lib.python2.7.site-packages.dateutil.zoneinfo', 'venv.lib.python2.7.site-packages.easypysmb',
              'venv.lib.python2.7.site-packages.pykeepass', 'venv.lib.python2.7.site-packages.libkeepass',
              'venv.lib.python2.7.site-packages.setuptools', 'venv.lib.python2.7.site-packages.setuptools.extern',
              'venv.lib.python2.7.site-packages.setuptools._vendor',
              'venv.lib.python2.7.site-packages.setuptools._vendor.packaging',
              'venv.lib.python2.7.site-packages.setuptools.command', 'venv.lib.python2.7.site-packages.pkg_resources',
              'venv.lib.python2.7.site-packages.pkg_resources.extern',
              'venv.lib.python2.7.site-packages.pkg_resources._vendor',
              'venv.lib.python2.7.site-packages.pkg_resources._vendor.packaging'],
    url='',
    license='',
    install_requires=requirements(),
    author='gopinathlangote',
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
