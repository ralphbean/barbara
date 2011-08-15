# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: False
# auth:       None
# mako:       True
#
#

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=['WebTest >= 1.2.3',
               'nose',
               'coverage',
               'wsgiref',
               'repoze.who-testutil >= 1.0.1',
               ]
if sys.version_info[:2] == (2,4):
    testpkgs.extend(['hashlib', 'pysqlite'])

setup(
    name='barbara',
    version='0.1',
    description='',
    author='',
    author_email='',
    #url='',
    install_requires=[
        "tg.devtools",
        "TurboGears2 >= 2.1.1",
        "Mako",
        "nltk",
        "pyyaml",
                                        ],
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2', 'tg.devtools'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'barbara': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'barbara': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
                        ('public/**', 'ignore', None)]},

    entry_points="""
    [paste.app_factory]
    main = barbara.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
    dependency_links=[
        "http://www.turbogears.org/2.1/downloads/current/"
        ],
    zip_safe=False
)
