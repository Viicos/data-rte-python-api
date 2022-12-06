
data-rte-python-api: Une API Python permettant de communiquer avec les APIs Data RTE
====================================================================================

|python-versions| |code-style| |mypy| |isort|


``data-rte-python-api`` permet de communiquer avec les `APIs du RTE <https://data.rte-france.com/>`_.

Installation
------------

La librairie peut être installée en utilisant ``pip`` (la librairie n'est pas publiée sur PyPI pour le moment) :

.. code-block:: shell

    pip install data-rte-python-api

Usage
-----

Vous devez au préalable enregistrer une application pour obtenir un ``client_id`` et ``client_secret`` avant de pouvoir utiliser les APIs.

.. code-block:: python

    from datetime import datetime

    from datarteapi import BigSubstations, BaseAPIException

    client = BigSubstations(client_id="your_client_id", client_secret="your_client_secret")

    try:
        client.get_pds_data(
            start_date=datetime.fromisoformat("2017-09-01T12:00:00"),
            end_date=datetime.fromisoformat("2017-09-01T23:00:00")
        )
    except BaseAPIException as e:
        # Handle the exception

Pour le moment, uniquement les APIs utilisant OAuth sont disponibles.

Gestion des dates
-----------------

En fonction de l'API que vous utilisez, les fuseaux horaires ne sont pas gérés de la même manière. Si tous les fuseaux horaires sont supportés par le serveur, la date sera envoyée telle quelle.
Si uniquement le fuseau UTC est supporté, les dates avec fuseau horaire seront converties en UTC. Dans le cas contraire, le fuseau horaire local est utilisé avant d'être converti en UTC.

Pour plus de détails, se référer à la documentation de l'API correspondante.

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
