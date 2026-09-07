Sections, tasks and rows
************************

Sections and tasks
==================

Every row belongs to a named section determined by its ``section`` value.  Rows that share the same section string are grouped under a single labelled separator in the Gantt chart.  Sections appear in the order they are first encountered in the CSV.

For example:

.. code:: rst

   .. roadmap::
      :title: Q1 Work

      section,name,start,end,row_group,link,tags
      Infrastructure,Database Upgrade,2027-01-10,2027-02-10,,,ops
      Infrastructure,Cache Layer,2027-02-01,2027-03-15,,,ops
      Product,User Profiles,2027-01-15,2027-03-01,,,code
      Product,Search v2,2027-02-15,2027-03-31,,,code

Which will render like this:

.. roadmap::
   :title: Q1 Work

   section,name,start,end,row_group,link,tags
   Infrastructure,Database Upgrade,2027-01-10,2027-02-10,,,ops
   Infrastructure,Cache Layer,2027-02-01,2027-03-15,,,ops
   Product,User Profiles,2027-01-15,2027-03-01,,,code
   Product,Search v2,2027-02-15,2027-03-31,,,code


.. _roadmap-subtasks:

Subtasks
========

A row whose ``section`` value matches the ``name`` of an existing task in the chart becomes a subtask of that parent task.  Subtasks are indented beneath their parent in the rendered diagram.  For example, giving ``section`` the value ``Backend Overhaul`` (which is an existing task name) makes the row a subtask:

.. code:: rst

   .. roadmap::
      :title: Platform with Subtasks
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Platform,Backend Overhaul,2027-01-15,2027-04-30,,,eng
      Backend Overhaul,Database Migration,2027-01-15,2027-02-28,,,eng
      Backend Overhaul,API Redesign,2027-03-01,2027-04-30,,,eng code
      Platform,Frontend Refresh,2027-02-01,2027-05-31,,,code

Which will render like this:

.. roadmap::
   :title: Platform with Subtasks
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Platform,Backend Overhaul,2027-01-15,2027-04-30,,,eng
   Backend Overhaul,Database Migration,2027-01-15,2027-02-28,,,eng
   Backend Overhaul,API Redesign,2027-03-01,2027-04-30,,,eng code
   Platform,Frontend Refresh,2027-02-01,2027-05-31,,,code

``Database Migration`` and ``API Redesign`` are rendered as subtasks of ``Backend Overhaul``.


.. _roadmap-milestones:

Milestones
==========

When a row's ``start`` and ``end`` dates are identical, the extension renders it as a Gantt milestone — a diamond marker on the timeline.  Milestones are never clipped by the ``:start:`` / ``:end:`` date window.

.. code:: rst

   .. roadmap::
      :title: Release Milestones
      :scale: monthly

      section,name,start,end,row_group,link,tags
      2027 Releases,Feature Freeze,2027-03-15,2027-03-15,,,
      2027 Releases,v2.0 Release,2027-04-30,2027-04-30,,,
      2027 Releases,v2.1 Release,2027-07-31,2027-07-31,,,
      2027 Releases,Year-End Wrap,2027-09-30,2027-09-30,,,

Which will render like this:

.. roadmap::
   :title: Release Milestones
   :scale: monthly

   section,name,start,end,row_group,link,tags
   2027 Releases,Feature Freeze,2027-03-15,2027-03-15,,,
   2027 Releases,v2.0 Release,2027-04-30,2027-04-30,,,
   2027 Releases,v2.1 Release,2027-07-31,2027-07-31,,,
   2027 Releases,Year-End Wrap,2027-09-30,2027-09-30,,,


.. _roadmap-same-row-grouping:

Same-row grouping
=================

Tasks that share the same non-empty ``row_group`` value are placed on a single Gantt row, displayed side-by-side.  This is useful for representing parallel workstreams or paired activities that logically occupy the same swim lane.

When ``row_group`` is used, enabling ``clean_style`` (the default) is important: it suppresses the per-task start/end/duration column annotations that would otherwise overlap on a shared row.

For two tasks to share a row cleanly, their bars *and* their text labels must not overlap horizontally.  In the example below each pair is spaced far enough apart in time that both labels have room to render side-by-side:

.. code:: rst

   .. roadmap::
      :title: Parallel Workstreams
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Roadmap,API Redesign,2026-09-01,2026-11-30,stream-a,,eng
      Roadmap,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code
      Roadmap,Security Audit,2026-09-15,2026-11-15,stream-b,,security
      Roadmap,Compliance Check,2027-04-01,2027-05-31,stream-b,,security

Which will render like this:

.. roadmap::
   :title: Parallel Workstreams
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Roadmap,API Redesign,2026-09-01,2026-11-30,stream-a,,eng
   Roadmap,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code
   Roadmap,Security Audit,2026-09-15,2026-11-15,stream-b,,security
   Roadmap,Compliance Check,2027-04-01,2027-05-31,stream-b,,security

``API Redesign`` and ``Frontend Refresh`` share ``stream-a`` and appear on one row; ``Security Audit`` and ``Compliance Check`` share ``stream-b`` and appear on another.

.. note::

   If the tasks in a shared ``row_group`` would overlap in time — or their labels would run into one another — the extension automatically moves the colliding task to a new row so the text stays readable.  This is the default behaviour; see :ref:`roadmap-collision-detection` below for how it works and how to turn it off.


.. _roadmap-collision-detection:

Collision detection
-------------------

By default, the extension automatically detects when two tasks in the same ``row_group`` would have overlapping bar labels and splits them onto additional rows rather than rendering illegible smeared text.  Tasks that fit together without collision stay on one row (no unnecessary splits); only colliding tasks are moved to a new row.  Collision is determined by estimating how many calendar days each label occupies horizontally (based on the active projectscale) and checking whether those footprints overlap.

Consider two tasks in the same ``row_group`` whose bars fully overlap in time.  With collision detection enabled (the default) they are automatically placed on separate rows so both labels remain readable:

.. code:: rst

   .. roadmap::
      :title: Overlapping Workstreams (detection on)
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Q2 2027,API Redesign,2027-04-01,2027-05-31,stream-a,,eng
      Q2 2027,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code

Which will render like this — note the two tasks each get their own row:

.. roadmap::
   :title: Overlapping Workstreams (detection on)
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Q2 2027,API Redesign,2027-04-01,2027-05-31,stream-a,,eng
   Q2 2027,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code

To force all same-group tasks onto one row regardless of overlap — for example, when you deliberately want overlapping bars for a visual effect — disable detection for a single chart with ``:collision-detection: false``.  With the *same* data as above, the two tasks are now packed onto a single row and their labels overlap:

.. code:: rst

   .. roadmap::
      :title: Overlapping Workstreams (detection off)
      :collision-detection: false
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Q2 2027,API Redesign,2027-04-01,2027-05-31,stream-a,,eng
      Q2 2027,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code

Which will render like this — both tasks share one row (labels overlap):

.. roadmap::
   :title: Overlapping Workstreams (detection off)
   :collision-detection: false
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Q2 2027,API Redesign,2027-04-01,2027-05-31,stream-a,,eng
   Q2 2027,Frontend Refresh,2027-04-01,2027-05-31,stream-a,,code

Or disable it globally in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py

    doxtr_roadmap_collision_detection = False

The label-width estimate can be tuned with ``doxtr_roadmap_collision_char_width_factor`` (default ``1.0``; higher values reserve more space per character and cause earlier splits) and ``doxtr_roadmap_collision_gap_days`` (minimum calendar-day gap between tasks on the same lane, default ``2``).

.. note::

   Collision detection is intentionally conservative: it slightly over-estimates label widths so that labels which are close to colliding are proactively split.  If you find the extension splitting tasks that look fine in your rendered output, lower ``doxtr_roadmap_collision_char_width_factor`` (e.g. to ``0.7``) or set ``:collision-detection: false`` on that chart.

The ``:collision-char-width-factor:`` directive option applies the same tuning per-chart, without changing the global default.  A value of ``1.0`` (the default) is conservative — it reserves a full character-width of horizontal space per label character, splitting tasks at the first sign of crowding.  Lowering the factor (e.g. to ``0.7``) reserves *less* space, so tasks need to be actually closer before the extension decides to split them onto separate rows.  Raising the factor above ``1.0`` makes splits happen even earlier.

The example below uses ``:collision-char-width-factor: 0.7`` on two short-named tasks separated by a modest gap.  With the default factor of ``1.0`` the conservative label-width estimate would split them onto separate rows; at ``0.7`` the estimator reserves less space, judges them clear, and keeps them on one row:

.. code:: rst

   .. roadmap::
      :title: Collision factor 0.7 (less aggressive splitting)
      :scale: monthly
      :collision-char-width-factor: 0.7

      section,name,start,end,row_group,link,tags
      Lane,Import,2027-01-01,2027-01-20,lane,,eng
      Lane,Export,2027-02-15,2027-03-06,lane,,eng

Which will render like this (both tasks share one row because the lower factor reserves less label space per character):

.. roadmap::
   :title: Collision factor 0.7 (less aggressive splitting)
   :scale: monthly
   :collision-char-width-factor: 0.7

   section,name,start,end,row_group,link,tags
   Lane,Import,2027-01-01,2027-01-20,lane,,eng
   Lane,Export,2027-02-15,2027-03-06,lane,,eng

To set the factor globally across all charts:

.. code-block:: python
   :caption: conf.py

    doxtr_roadmap_collision_char_width_factor = 0.7
