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

**Credentials**

To get your credentials, contact us by email with your all needs at: contact@idcheck.io
You will receive two sets of credentials: one for test purpose only and on for production.

**Platforms**

Three platforms can be targeted with the library:

+------------+----------------------------------+-------------+------------------------------------------+----------------------------------------+----------------------+
| Platform   |      API URL                     | Credentials | Purpose                                  | Restriction                            | Cost                 |
+============+==================================+=============+==========================================+========================================+======================+ 
| SANDBOX    | https://sandbox.idcheck.io/rest  | Test        | Dev integration + automated tests        | Only a fix set of images are supported | Free                 |
+------------+----------------------------------+-------------+------------------------------------------+----------------------------------------+----------------------+
| TEST       | https://api-test.idcheck.io/rest | Test        | Functional tests / Idcheck.io evaluation | No SLA                                 | Commercial agreement |
+------------+----------------------------------+-------------+------------------------------------------+----------------------------------------+----------------------+
| PROD       | https://api.idcheck.io/rest      | Prod        | Production service                       | None                                   | Commercial agreement |
+------------+----------------------------------+-------------+------------------------------------------+----------------------------------------+----------------------+


Installation
============
To install idcheckio library, simply:

.. code-block:: bash

    $ pip install idcheckio


Usage
=====

.. code-block:: python

    import idcheckio
    conn = idcheckio.IDCheckIO("example@example.com", "pwd")

You can use the created connection to call differents methods, as described below.

All responses use the same format and are made of 3 parts:

- status : the status of the request (http code)
- uid : the uid for the current analysis
- body : the server response in JSON format

For a full description of the JSON response, please see the API reference guide or use the sandbox to get some examples. 

Analysis
--------

**MRZ analysis**

.. code-block:: python

    result = conn.analyze_mrz("P<UTOBANDERAS<<LILIAN<<<<<<<<<<<<<<<<<<<<<<<",
                              "01234567894UTO8001014F2501017<<<<<<<<<<<<<06")

This example uses a 2 lines MRZ but you can set 1, 2 or 3 lines.

**Image analysis**

.. code-block:: python

    result = conn.analyze_image("/tmp/image.jpg", path=True)

This method accepts 2 images (recto and verso).

There are two different ways to specify the images:

- with the system path. In this case the path variable must be True
- directly encoded in base64 

By default, this function performs a synchronous call to the API and returns the analysis results. 
If you want to use an asynchronous call, you must set the optional "async" parameter to True.
In asynchronous mode, the get_status function should be used to know when the analysis is done. 

**Get the status of a request**

.. code-block:: python

    report = conn.get_status(result.uid)

To be used in asynchronous mode only. Returns the status of an analysis request.

You can set the argument wait (int in ms) to delegate the polling to the server

.. code-block:: python

    report = conn.get_status(result.uid, wait=20000)

This example returns the result of the analysis when it is done. Useful in a thread, avoid polling from client.

**Get a result of the analysis**

.. code-block:: python

    report = conn.get_result(result.uid)

Analysis results remain available a few minutes after the analysis. The API does not provide analysis storage features and it is your responsibility to save the results if needed.

**Get a PDF report**

.. code-block:: python

    report = conn.get_report(result.uid)

Again, the API does not provide analysis storage features and it is your responsibility to save report PDF if needed.

Administration
--------------

**Get the server status**

This method gives the state of the service: OK, WARN (partially available) or ERROR (unavailable).

.. code-block:: python

    status = conn.healthcheck()

**Get the number of credits**

This method lets you know how many credits remain on your account

.. code-block:: python

    status = conn.get_credits()


Sandbox
-------

**Get the list of sandbox MRZ**

.. code-block:: python

    mrzlist = conn.get_mrzlist()

Only keys returned in this list can be used with the function get_mrz.

**Get a MRZ for a test**

.. code-block:: python

    mrz = conn.get_mrz("CNI_BE_SPECIMEN_MRZ")

The returned MRZ can be used for a test with the function analyze_mrz.

**Get the list of sandbox images**

.. code-block:: python

    imagelist = conn.get_imagelist()

Only keys returned in this list can be used with the function get_image.

**Get a image for a test**

.. code-block:: python

    image = conn.get_image("PASSEPORT_CHN_SPECIMEN_ZHENGJIAN")

The returned image can be used for a test with the function analyze_image.

