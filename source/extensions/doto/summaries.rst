.. _doto-summaries:

Summaries and charts
********************

``.. doto-summary::`` computes statistics over the collected tasks, grouped by a
field.  It can render as a text summary or as a chart.

Group by status (default)
==========================

.. code:: rst

   .. doto-summary::

Which will render like this:

.. doto-summary::

Group by priority as a bar chart
================================

Set ``:show-chart: true`` and choose a ``:chart-type:``.

.. code:: rst

   .. doto-summary::
      :group-by: priority
      :show-chart: true
      :chart-type: bar

Which will render like this:

.. doto-summary::
   :group-by: priority
   :show-chart: true
   :chart-type: bar

Group by assignee as a pie chart
================================

.. code:: rst

   .. doto-summary::
      :group-by: assignee
      :show-chart: true
      :chart-type: pie

Which will render like this:

.. doto-summary::
   :group-by: assignee
   :show-chart: true
   :chart-type: pie

Completion as a progress chart
==============================

.. code:: rst

   .. doto-summary::
      :group-by: status
      :show-chart: true
      :chart-type: progress

Which will render like this:

.. doto-summary::
   :group-by: status
   :show-chart: true
   :chart-type: progress

Filtered summary
================

Filters apply before the statistics are computed.  This example summarises only the
critical and high tasks, grouped by both status and priority.

.. code:: rst

   .. doto-summary::
      :priority: critical, high
      :group-by: status, priority

Which will render like this:

.. doto-summary::
   :priority: critical, high
   :group-by: status, priority

Summary options
===============

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Option
     - Values
     - Default
   * - ``:group-by:``
     - ``status``, ``priority``, ``assignee``, ``tags`` (comma-separated)
     - ``status``
   * - ``:show-chart:``
     - ``true`` / ``false``
     - ``false``
   * - ``:chart-type:``
     - ``bar``, ``pie``, ``stacked-bar``, ``progress``, ``burndown``
     - ``bar``
   * - ``:assignee:`` / ``:status:`` / ``:priority:`` / ``:tags:``
     - filter before summarising
     - —

.. note::

   The chart engine is selected globally by ``doto_chart_engine`` (``svg`` by
   default, or ``plotly``).  With ``plotly`` and the ``[charts]`` extra installed,
   charts render as static images; when plotly, kaleido, or Chrome are unavailable
   the build falls back to the built-in SVG charts.  PDF output always renders a
   native chart.
