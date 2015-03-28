zbox
====

.. image:: https://pypip.in/version/zbox/badge.svg
    :target: https://pypi.python.org/pypi/zbox/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/zbox/badge.svg
    :target: https://pypi.python.org/pypi/zbox/
    :alt: Supported Python versions

.. image:: https://pypip.in/wheel/zbox/badge.svg
    :target: https://pypi.python.org/pypi/zbox/
    :alt: Wheel Status

.. image:: https://travis-ci.org/jiffyclub/zbox.svg?branch=master
    :target: https://travis-ci.org/jiffyclub/zbox
    :alt: Travis-CI Status

zbox is a tiny library to help me use toolz_ and cytoolz_.
I frequently use ``toolz`` and would like to use ``cytoolz`` if it's
available, but don't want to put a ``try``/``except`` in
all my projects. By importing ``toolz`` from ``zbox`` I always
get ``cytoolz`` if ``cytoolz`` is installed and otherwise I get
``toolz``.

Installation
------------

zbox is on PyPI, install it with: ``pip install zbox``.
zbox works on Python 2 and Python 3.

Usage
-----

.. code::

   from zbox import toolz

If cytoolz_ is installed ``toolz`` will be ``cytoolz``,
otherwise it will be ``toolz``.

.. _toolz: http://toolz.readthedocs.org/
.. _cytoolz: https://github.com/pytoolz/cytoolz/
