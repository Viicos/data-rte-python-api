
data-rte-python-api: A Python API wrapper for the data APIs of the RTE
======================================================================

|python-versions| |code-style| |mypy| |isort|


``data-rte-python-api`` is a Python API wrapper for the `APIs of the RTE <https://data.rte-france.com/>`_.

Installation
------------

The library can be installed using ``pip``:

.. code-block:: shell

    pip install data-rte-python-api

Usage
-----

You will have to register an application to get a ``client_id`` and ``client_secret`` before using any of the APIs.

.. code-block:: python

    from datetime import datetime

    from datarteapi import BigSubstations, BaseAPIException

    client = BigSubstations(client_id="your_client_id", client_secret="your_client_secret")

    try:
        apiresponse = client.get_pds_data(
            start_date=datetime.fromisoformat("2017-09-01T12:00:00"),
            end_date=datetime.fromisoformat("2017-09-01T23:00:00")
        )
    except BaseAPIException as e:
        # Handle the exception

    print(apiresponse.data, apiresponse.headers)

Currently, only the APIs working with OAuth are available.

Date entries
------------

Depending on the API you are using, date timezones are handled differently. If all timezones are supported by the API server, the datetime will be used as is.
If only UTC is supported, timezone aware dates will be converted to UTC. For unware dates, local timezone is used before being converted to UTC.

For more details, refer to the corresponding API documentation.

.. |python-versions| image:: https://img.shields.io/badge/python-3.7%2B-blue.svg
    :alt: Supported Python versions
    :target: https://www.python.org/downloads/

.. |code-style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style: Black
    :target: https://github.com/psf/black

.. |mypy| image:: https://img.shields.io/badge/mypy-checked-blue
    :alt: Mypy: checked
    :target: http://mypy-lang.org/

.. |isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :alt: Imports: isort
    :target: https://pycqa.github.io/isort/
