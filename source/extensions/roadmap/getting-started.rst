.. _roadmap-a-roadmap-without-sections:

Getting started
***************

Configuration
=============

Add both ``sphinxcontrib.plantuml`` and ``doxtr_roadmap`` to the ``extensions`` list in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py — enabling doxtr_roadmap

    extensions = [
        ...
        "sphinxcontrib.plantuml",
        "doxtr_roadmap",
        ...
    ]

``sphinxcontrib.plantuml`` must appear before ``doxtr_roadmap``.  If the PlantUML jar is not on the system path, set the ``plantuml`` config value as described in the :doc:`PlantUML chapter </extensions/diagrams/plantuml/plantuml>`:

.. code-block:: python
   :caption: conf.py — plantuml command (if needed)

    plantuml = "java -jar /path/to/plantuml.jar"

The version-check behaviour can be changed in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py — version-check behaviour

    # "error" (default) — abort the build if PlantUML is below v1.2026.7
    # "warn"            — emit a warning but continue building
    # "off" or False    — skip the version check entirely
    doxtr_roadmap_require_plantuml_version = "error"


A first roadmap
===============

The simplest use of the directive is an inline CSV body.  The first row must be a header that names the columns; subsequent rows are the roadmap items.  For example:

.. code:: rst

   .. roadmap::
      :title: Sprint Overview

      section,name,start,end,row_group,link,tags
      Sprints,Sprint 1,2027-01-06,2027-01-30,,,
      Sprints,Sprint 2,2027-02-03,2027-02-27,,,
      Backend,Auth Service,2027-01-06,2027-02-15,,,eng
      Backend,API Gateway,2027-01-20,2027-02-27,,,eng code
      Frontend,Login UI,2027-01-13,2027-02-05,,,code
      Frontend,Dashboard,2027-02-01,2027-02-27,,,code

Which will render like this:

.. roadmap::
   :title: Sprint Overview

   section,name,start,end,row_group,link,tags
   Sprints,Sprint 1,2027-01-06,2027-01-30,,,
   Sprints,Sprint 2,2027-02-03,2027-02-27,,,
   Backend,Auth Service,2027-01-06,2027-02-15,,,eng
   Backend,API Gateway,2027-01-20,2027-02-27,,,eng code
   Frontend,Login UI,2027-01-13,2027-02-05,,,code
   Frontend,Dashboard,2027-02-01,2027-02-27,,,code

The default scale is ``monthly``.  Each named group of rows (``Sprints``, ``Backend``, ``Frontend``) becomes a labelled section in the rendered chart.


A roadmap without sections
==========================

Sections are entirely optional.  If you leave the ``section`` column blank — or omit it from the header altogether — the tasks are rendered as a single flat list with no section separators.  This is handy for a short roadmap that doesn't need grouping.

Leaving the ``section`` cells empty:

.. code:: rst

   .. roadmap::
      :title: Release Checklist

      section,name,start,end,row_group,link,tags
      ,Feature freeze,2027-02-01,2027-02-01,,,
      ,Beta,2027-02-02,2027-02-20,,,
      ,Release candidate,2027-02-21,2027-03-05,,,
      ,Ship,2027-03-06,2027-03-06,,,

Which will render like this:

.. roadmap::
   :title: Release Checklist

   section,name,start,end,row_group,link,tags
   ,Feature freeze,2027-02-01,2027-02-01,,,
   ,Beta,2027-02-02,2027-02-20,,,
   ,Release candidate,2027-02-21,2027-03-05,,,
   ,Ship,2027-03-06,2027-03-06,,,

You can also drop the ``section`` column (and any other optional columns) from the header entirely — only ``name``, ``start``, and ``end`` are required:

.. code:: rst

   .. roadmap::
      :title: Minimal Roadmap

      name,start,end
      Research,2027-01-01,2027-02-15
      Prototype,2027-02-16,2027-04-01
      Launch,2027-04-02,2027-04-02

Which will render like this:

.. roadmap::
   :title: Minimal Roadmap

   name,start,end
   Research,2027-01-01,2027-02-15
   Prototype,2027-02-16,2027-04-01
   Launch,2027-04-02,2027-04-02

Both forms produce the same section-less layout.  You can mix approaches too: give some rows a section name and leave others blank — the blank rows simply render without a header before them.
