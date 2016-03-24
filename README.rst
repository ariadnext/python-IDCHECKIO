python-IDCHECKIO
================
Python Library for IDCHECKIO API
================================

.. image:: https://www.idcheck.io/content/uploads/sites/2/2015/12/tick_mark.png

Web application : <https://idcheck.io>

Mashape REST API : <https://market.mashape.com/ariadnext/idcheck-io-api>

Swagger REST API : <https://api.idcheck.io/swagger/#/>

Requirements
------------

This module works in Python2.X and Python3.X.

**Account**

To create your account an credit, contact us by email with your needs at : contact@idcheck.io


Installation
------------
To install Requests, simply:

.. code-block:: bash

    $ pip install idcheckio


Usage
-----
**AnalyseMRZ**

.. code-block:: python

    import idcheckio
    conn = idcheckio.IDCheckIO("example@example.com", "exemple")
    result = conn.analyse_mrz("P<UTOBANDERAS<<LILIAN<<<<<<<<<<<<<<<<<<<<<<<",
                              "01234567894UTO8001014F2501017<<<<<<<<<<<<<06")

Documentation
-------------

Soon...
