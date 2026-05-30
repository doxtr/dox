.. index:: OpenAPI Documentation, API Documentation; OpenAPI

OpenAPI Documentation
=====================

You can find the OpenAPI documentation at https://sphinxcontrib-openapi.readthedocs.io/

You can use https://sphinxcontrib-openapi.readthedocs.io/en/latest/ to generate API documentation from OpenAPI specifications. This allows you to create comprehensive and interactive API documentation for your project.

Configuration
-------------

Make sure to add :code:`sphinxcontrib.openapi` to the list of extensions in your :file:`conf.py` file:

.. code-block:: python
   :caption: conf.py options for sphinxcontrib-openapi

    extensions = [
        ...
        "sphinxcontrib.openapi",
        ...
    ]

Tic Tac Toe API
---------------

We're going to look at the following JSON file as an example:

.. openapi:: tictactoe.json

Visualizing the API
-------------------

With the PlantUML extension, we can fairly easily generate diagrams from the OpenAPI specification. This can be a great way to visualize the structure of your API and how different endpoints relate to each other.

.. uml:: tictactoe.puml

