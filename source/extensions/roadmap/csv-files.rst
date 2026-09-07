CSV files and format
********************

Loading from a CSV file
=======================

For larger roadmaps, keep the data in a separate :file:`.csv` file and reference it with the ``:file:`` option.  The path is resolved relative to the document first, then relative to the Sphinx source directory:

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :title: Product Roadmap 2027

The contents of :file:`files/product-roadmap.csv` used in the example below are:

.. literalinclude:: files/product-roadmap.csv
   :language: text

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :title: Product Roadmap 2027


.. _roadmap-multiple-files-and-globs:

Multiple files and globs
========================

For projects that split a roadmap across several CSV files — for example, one file per sprint — ``:file:`` accepts multiple path specs separated by spaces or commas, and each spec may contain glob metacharacters (``*``, ``?``, ``[…]``).

All matched files are loaded as **one combined roadmap**: sections with the same name merge across files, and subtasks or ``row_group`` references work even when the parent task is defined in a different file.  The extension reads every file's rows in the given spec order (glob matches are sorted lexicographically within each pattern) and runs the full two-pass subtask/section logic over all rows together.

**Explicit list** — space- or comma-separated paths::

   .. roadmap::
      :file: files/sprint-01.csv files/sprint-02.csv files/sprint-03.csv
      :title: All Sprints — Explicit List

**Glob pattern** — equivalent result::

   .. roadmap::
      :file: files/sprint-*.csv
      :title: All Sprints — Glob

Both produce the same combined roadmap.  Here is the explicit-list version rendered live:

.. roadmap::
   :file: files/sprint-01.csv files/sprint-02.csv files/sprint-03.csv
   :title: All Sprints — Explicit List

And the glob version (identical output):

.. roadmap::
   :file: files/sprint-*.csv
   :title: All Sprints — Glob

The contents of the three sprint files used above are shown below.  Notice that ``sprint-01.csv`` contains ``Auth Service`` as a top-level task and a subtask row whose ``section`` column is ``Auth Service`` — demonstrating that subtasks work within a single file.  The same mechanism works across files: if ``sprint-02.csv`` had a row with ``section=Auth Service`` it would become a subtask of the parent defined in ``sprint-01.csv``.

.. literalinclude:: files/sprint-01.csv
   :caption: files/sprint-01.csv
   :language: text

.. literalinclude:: files/sprint-02.csv
   :caption: files/sprint-02.csv
   :language: text

.. literalinclude:: files/sprint-03.csv
   :caption: files/sprint-03.csv
   :language: text

.. note::

   - Paths are resolved relative to the document directory first, then ``srcdir`` — the same rules as a single ``:file:`` path.
   - Glob matches within a single pattern are sorted lexicographically (``sprint-01``, ``sprint-02``, …), so files are always combined in a predictable order.
   - If the same file is matched by more than one spec it is read only once (de-duplicated while preserving first-seen order).
   - :func:`env.note_dependency` is called for every resolved file so that editing any of them triggers an incremental rebuild.  However, *adding a brand-new file* that matches an existing glob pattern is not detected automatically — run ``make clean html`` after adding new files to a glob.
   - If a spec matches no files at all the directive reports an error.  Other specs in the same ``:file:`` value that do match files are still loaded.


The CSV format
==============

The CSV must contain a header row followed by one or more data rows.  Only ``name``, ``start``, and ``end`` are required; every other column is optional and may be omitted from the header entirely.  The recognised column names are:

.. list-table::
   :header-rows: 1
   :widths: 18 12 70

   * - Column
     - Required
     - Description
   * - ``section``
     - no
     - Section (group) name that this row belongs to.  If the value matches the ``name`` of an already-defined task in the same section, the row becomes a subtask of that task instead (see :ref:`roadmap-subtasks`).  If left blank — or the column is omitted — the task renders with no section header (see :ref:`roadmap-a-roadmap-without-sections`).
   * - ``name``
     - yes
     - Display name of the task or milestone shown on the Gantt bar.
   * - ``start``
     - yes
     - Start date in ISO format ``YYYY-MM-DD``.
   * - ``end``
     - yes
     - End date in ISO format ``YYYY-MM-DD``.  When ``start == end`` the row is rendered as a milestone diamond (see :ref:`roadmap-milestones`).
   * - ``row_group``
     - no
     - Tasks that share the same non-empty ``row_group`` value are placed on a single Gantt row (see :ref:`roadmap-same-row-grouping`).
   * - ``link``
     - no
     - Plain ``https://`` URL or an ``:xlink:\`id\``` role expression.  When ``sphinxcontrib.xlink`` is loaded the ID is resolved to a URL and title (see :ref:`roadmap-links`).
   * - ``tags``
     - no
     - Space- or comma-separated list of tag strings used for filtering (see :ref:`roadmap-tags-and-filtering`).
