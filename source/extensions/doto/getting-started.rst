.. _doto-getting-started:

Getting started
***************

Configuration
=============

Add ``doxtr_doto`` to the ``extensions`` list in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py — enabling doxtr_doto

    extensions = [
        ...
        "doxtr_doto",
        ...
    ]

The import name uses an underscore (``doxtr_doto``); the distribution on PyPI is
named ``doxtr-doto`` (with a hyphen).  Install it with:

.. code-block:: console

    $ pip install doxtr-doto

To also install the command-line interface and the optional charting engine:

.. code-block:: console

    $ pip install "doxtr-doto[cli,charts]"

By default tasks are stored in :file:`.doto/tasks.json` relative to the Sphinx
source directory.  You can point the store anywhere with ``doto_json_file``:

.. code-block:: python
   :caption: conf.py — task store location

    doto_json_file = ".doto/tasks.json"   # default
    doto_auto_create_json = True          # create the store if missing
    doto_sync_on_build = True             # keep RST and JSON in sync on build

A first task
============

The simplest task is a title.  When you omit the ``:id:`` option, an ID is generated
automatically from the document name and line number.

.. code:: rst

   .. doto:: Write the getting-started guide

Which will render like this:

.. doto:: Write the getting-started guide
   :id: extensions-doto-getting-started-L55

That is all it takes.  The next page shows every option a task can carry.
