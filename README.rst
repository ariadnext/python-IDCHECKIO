python-IDCHECKIO
================
Python Library for IDCHECKIO API
================================

.. image:: https://www.idcheck.io/content/uploads/sites/2/2015/12/tick_mark.png

Web application : <https://idcheck.io>

Mashape REST API : <https://market.mashape.com/ariadnext/idcheck-io-api>

Swagger REST API : <https://api.idcheck.io/swagger/#/>

Requirements
============

This module works in Python2.X and Python3.X.

**Account**

To create your account an credit, contact us by email with your needs at : contact@idcheck.io


Installation
============
To install Requests, simply:

.. code-block:: bash

    $ pip install idcheckio


Usage
=====

.. code-block:: python
    import idcheckio
    conn = idcheckio.IDCheckIO("example@example.com", "exemple")

You can use the result object to call differents methods.

All response use the same format and is compose in 3 parts:
- status : the status of the request (http code)
- uid : the uid for the current analysis
- body : the server response in JSON format

Analysis
--------


Analyze a MRZ
.. code-block:: python
    result = conn.analyze_mrz("P<UTOBANDERAS<<LILIAN<<<<<<<<<<<<<<<<<<<<<<<",
                              "01234567894UTO8001014F2501017<<<<<<<<<<<<<06")

This example use 2 MRZ lines. You can set 1, 2 or 3 lines.

Analyze an image
.. code-block:: python
    result = conn.analyze_mrz("/tmp/image.jpg", path=True)

This method accept 2 images (recto and verso).

There are two different ways to put an image:
- with the system path and the argument path with value True
- directly encoded in base64

You can set the asynchronous mode with the argument async (True)

Get a result of the analyze
.. code-block:: python
    report = conn.get_result(result.uid)

This is useful in asynchronous mode. On synchronous mode, this result is directly returned in the response of the function.

Get a PDF report
.. code-block:: python
    report = conn.get_report(result.uid)

Get the status of a request
.. code-block:: python
    report = conn.get_status(result.uid)

Use in asynchronous mode. Return the status of an analysis request.

You can set the argument wait (int in ms) to delegate the polling to the server

.. code-block:: python
    report = conn.get_status(result.uid, wait=20000)

This example return the result of the analysis when this is done. Useful in a thread, avoid polling from client.

Administration
--------------

Get the server status
.. code-block:: python
    status = conn.healthcheck()

Get the number of credits
.. code-block:: python
    status = conn.get_credits()


Sandbox
-------

Get the list of sandbox MRZ
.. code-block:: python
    mrzlist = conn.get_mrzlist()

Only keys returned in this list can be used with the function get_mrz.

Get a MRZ for a test
.. code-block:: python
    mrz = conn.get_mrz("CNI_BE_SPECIMEN_MRZ")

The returned MRZ can be used for a test with the function analyze_mrz.

Get the list of sandbox images
.. code-block:: python
    imagelist = conn.get_imagelist()

Only keys returned in this list can be used with the function get_image.

Get a image for a test
.. code-block:: python
    image = conn.get_image("PASSEPORT_CHN_SPECIMEN_ZHENGJIAN")

The returned image can be used for a test with the function analyze_image.
