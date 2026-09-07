Timeline views and zoom
***********************

Periods and zooming
===================

A *period* is any named task in the CSV — typically a sprint or increment row in a dedicated ``Periods`` section.  Specifying ``:period:`` clips the diagram to exactly that task's date range.  When exactly one period is specified and ``:scale:`` is not set, the extension automatically switches to ``daily`` scale and closes weekends, giving a fine-grained sprint view.

Multiple periods can be supplied as a comma-separated list; the clip window spans from the earliest start to the latest end across all named periods.

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :period: Q1-2027

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :period: Q1-2027

To zoom across two periods at once:

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :period: Q1-2027, Q2-2027
      :scale: weekly

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :period: Q1-2027, Q2-2027
   :scale: weekly


Date-window clipping
====================

Use ``:start:`` and ``:end:`` to clip the diagram to an explicit date window without referring to a named period.  Tasks that fall entirely outside the window are hidden; milestones are always preserved.  The ``:scale:`` option controls the timeline unit (``daily``, ``weekly``, or ``monthly``), and ``:close-weekends:`` suppresses Saturday and Sunday columns.  Here ``:column-zoom: 4`` also widens each column fourfold so the clipped window spreads across the full page width (see :ref:`roadmap-column-width-zoom`).

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :start: 2027-02-01
      :end: 2027-05-31
      :scale: monthly
      :column-zoom: 4
      :close-weekends:

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :start: 2027-02-01
   :end: 2027-05-31
   :scale: monthly
   :column-zoom: 4
   :close-weekends:


Titles and scale
================

``:title:`` overrides the diagram heading.  ``:scale:`` selects the timeline granularity:

- ``daily`` — one column per working day.
- ``weekly`` — one column per week.
- ``monthly`` — one column per month (default).

.. code:: rst

   .. roadmap::
      :title: Engineering Work — Weekly View
      :scale: weekly

      section,name,start,end,row_group,link,tags
      Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
      Backend,Observability,2027-04-01,2027-06-15,,,eng ops
      Frontend,Component Audit,2027-03-15,2027-04-30,,,code

Which will render like this:

.. roadmap::
   :title: Engineering Work — Weekly View
   :scale: weekly

   section,name,start,end,row_group,link,tags
   Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
   Backend,Observability,2027-04-01,2027-06-15,,,eng ops
   Frontend,Component Audit,2027-03-15,2027-04-30,,,code


.. _roadmap-column-width-zoom:

Column width (zoom)
===================

By default PlantUML sizes Gantt columns compactly, which can leave the chart looking narrow on wide pages.  The ``:column-zoom:`` directive option (or the global ``doxtr_roadmap_column_zoom`` config value) multiplies the width of each time column by appending ``zoom <factor>`` to the ``projectscale`` line.

A zoom of ``1`` (the default) leaves column widths unchanged.  For example, a zoom of ``2`` doubles each column’s width:

.. code:: rst

   .. roadmap::
      :title: Column Zoom Example (×2)
      :column-zoom: 2

      section,name,start,end,row_group,link,tags
      Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
      Backend,Observability,2027-04-01,2027-06-15,,,eng ops
      Frontend,Component Audit,2027-03-15,2027-04-30,,,code

Which will render like this — compare with the default-width chart above:

.. roadmap::
   :title: Column Zoom Example (×2)
   :column-zoom: 2

   section,name,start,end,row_group,link,tags
   Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
   Backend,Observability,2027-04-01,2027-06-15,,,eng ops
   Frontend,Component Audit,2027-03-15,2027-04-30,,,code

To set a zoom level for all charts in the project, add it to :file:`conf.py`:

.. code-block:: python
   :caption: conf.py

    doxtr_roadmap_column_zoom = 2

The ``:width:`` directive option forces the *rendered image* to fill a specified width in HTML and PDF (via ``sphinxcontrib.plantuml``'s standard image-width support).  Setting ``:width: 100%`` stretches the image to the full available text width:

.. code:: rst

   .. roadmap::
      :title: Full-width Roadmap (width\: 100%)
      :scale: monthly
      :width: 100%

      section,name,start,end,row_group,link,tags
      Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
      Backend,Observability,2027-04-01,2027-06-15,,,eng ops
      Frontend,Component Audit,2027-03-15,2027-04-30,,,code

Which will render like this — the image fills the available page width:

.. roadmap::
   :title: Full-width Roadmap (width: 100%)
   :scale: monthly
   :width: 100%

   section,name,start,end,row_group,link,tags
   Backend,Service Mesh,2027-03-01,2027-05-31,,,eng
   Backend,Observability,2027-04-01,2027-06-15,,,eng ops
   Frontend,Component Audit,2027-03-15,2027-04-30,,,code

Without ``:width:``, the image uses its natural rendered size (current default behaviour).  You can combine ``:width:`` with ``:column-zoom:`` to control both the source column width and the final placement:

.. code:: rst

   .. roadmap::
      :column-zoom: 3
      :width: 100%
      :file: files/product-roadmap.csv

This widens each time column three-fold *and* stretches the image to the full text width.

.. note::

   The ``zoom <factor>`` keyword form requires PlantUML v1.2026.7 or newer — already the extension's minimum baseline.
