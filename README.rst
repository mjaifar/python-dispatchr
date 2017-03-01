========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |coveralls|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-dispatchr/badge/?style=flat
    :target: https://readthedocs.org/projects/python-dispatchr
    :alt: Documentation Status

.. |coveralls| image:: https://coveralls.io/repos/mjaifar/python-dispatchr/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/mjaifar/python-dispatchr

.. |landscape| image:: https://landscape.io/github/mjaifar/python-dispatchr/master/landscape.svg?style=flat
    :target: https://landscape.io/github/mjaifar/python-dispatchr/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/mjaifar/python-dispatchr
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/mjaifar/python-dispatchr/badges/gpa.svg
   :target: https://codeclimate.com/github/mjaifar/python-dispatchr
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/dispatchr.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/dispatchr

.. |commits-since| image:: https://img.shields.io/github/commits-since/mjaifar/python-dispatchr/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mjaifar/python-dispatchr/compare/v0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/dispatchr.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/dispatchr

.. |wheel| image:: https://img.shields.io/pypi/wheel/dispatchr.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/dispatchr

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/dispatchr.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/dispatchr

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/dispatchr.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/dispatchr

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/mjaifar/python-dispatchr/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/mjaifar/python-dispatchr/


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD license

Installation
============

::

    pip install dispatchr

Documentation
=============

https://python-dispatchr.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
