*******
Roadmap
*******

The ``doxtr_roadmap`` extension provides a ``.. roadmap::`` directive that
generates PlantUML Gantt roadmaps directly from CSV data.  Rows are read from
an inline CSV body or an external :file:`.csv` file, passed through optional
tag and query filters, and emitted as a PlantUML Gantt chart rendered by
:xlink:`sphinxcontrib.plantuml <plantuml-home>`.  The extension optionally
integrates with ``sphinxcontrib.xlink`` for clickable task links and with the
``doxtr_pdf_theme_core`` palette for consistent colour and typography in PDF
output.

PlantUML :xlink:`v1.2026.7 or newer <plantuml-home>` is required.  The
extension checks the installed version at build startup and will abort the
build (or warn, depending on configuration) if the requirement is not met.


Configuration
=============

Add both ``sphinxcontrib.plantuml`` and ``doxtr_roadmap`` to the
``extensions`` list in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py — enabling doxtr_roadmap

    extensions = [
        ...
        "sphinxcontrib.plantuml",
        "doxtr_roadmap",
        ...
    ]

``sphinxcontrib.plantuml`` must appear before ``doxtr_roadmap``.  If the
PlantUML jar is not on the system path, set the ``plantuml`` config value as
described in the :doc:`PlantUML chapter </extensions/diagrams/plantuml/plantuml>`:

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

The simplest use of the directive is an inline CSV body.  The first row must
be a header that names the columns; subsequent rows are the roadmap items.
For example:

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

The default scale is ``monthly``.  Each named group of rows (``Sprints``,
``Backend``, ``Frontend``) becomes a labelled section in the rendered chart.


A roadmap without sections
==========================

Sections are entirely optional.  If you leave the ``section`` column blank —
or omit it from the header altogether — the tasks are rendered as a single
flat list with no section separators.  This is handy for a short roadmap that
doesn't need grouping.

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

You can also drop the ``section`` column (and any other optional columns)
from the header entirely — only ``name``, ``start``, and ``end`` are
required:

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

Both forms produce the same section-less layout.  You can mix approaches too:
give some rows a section name and leave others blank — the blank rows simply
render without a header before them.


Loading from a CSV file
=======================

For larger roadmaps, keep the data in a separate :file:`.csv` file and
reference it with the ``:file:`` option.  The path is resolved relative to
the document first, then relative to the Sphinx source directory:

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :title: Product Roadmap 2027

The contents of :file:`files/product-roadmap.csv` used in the example below
are:

.. literalinclude:: files/product-roadmap.csv
   :language: text

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :title: Product Roadmap 2027


Multiple files and globs
========================

For projects that split a roadmap across several CSV files — for example,
one file per sprint — ``:file:`` accepts multiple path specs separated by
spaces or commas, and each spec may contain glob metacharacters
(``*``, ``?``, ``[…]``).

All matched files are loaded as **one combined roadmap**: sections with the
same name merge across files, and subtasks or ``row_group`` references work
even when the parent task is defined in a different file.  The extension reads
every file's rows in the given spec order (glob matches are sorted
lexicographically within each pattern) and runs the full two-pass
subtask/section logic over all rows together.

**Explicit list** — space- or comma-separated paths::

   .. roadmap::
      :file: files/sprint-01.csv files/sprint-02.csv files/sprint-03.csv
      :title: All Sprints — Explicit List

**Glob pattern** — equivalent result::

   .. roadmap::
      :file: files/sprint-*.csv
      :title: All Sprints — Glob

Both produce the same combined roadmap.  Here is the explicit-list version
rendered live:

.. roadmap::
   :file: files/sprint-01.csv files/sprint-02.csv files/sprint-03.csv
   :title: All Sprints — Explicit List

And the glob version (identical output):

.. roadmap::
   :file: files/sprint-*.csv
   :title: All Sprints — Glob

The contents of the three sprint files used above are shown below.  Notice
that ``sprint-01.csv`` contains ``Auth Service`` as a top-level task and a
subtask row whose ``section`` column is ``Auth Service`` — demonstrating
that subtasks work within a single file.  The same mechanism works across
files: if ``sprint-02.csv`` had a row with ``section=Auth Service`` it would
become a subtask of the parent defined in ``sprint-01.csv``.

.. literalinclude:: files/sprint-01.csv
   :caption: files/sprint-01.csv
   :language: text

.. literalinclude:: files/sprint-02.csv
   :caption: files/sprint-02.csv
   :language: text

.. literalinclude:: files/sprint-03.csv
   :caption: files/sprint-03.csv
   :language: text

**Notes:**

- Paths are resolved relative to the document directory first, then
  ``srcdir`` — the same rules as a single ``:file:`` path.
- Glob matches within a single pattern are sorted lexicographically
  (``sprint-01``, ``sprint-02``, …), so files are always combined in a
  predictable order.
- If the same file is matched by more than one spec it is read only once
  (de-duplicated while preserving first-seen order).
- :func:`env.note_dependency` is called for every resolved file so that
  editing any of them triggers an incremental rebuild.  However, *adding a
  brand-new file* that matches an existing glob pattern is not detected
  automatically — run ``make clean html`` after adding new files to a glob.
- If a spec matches no files at all the directive reports an error.  Other
  specs in the same ``:file:`` value that do match files are still loaded.


Figures and captions
====================

Adding a ``:caption:`` to a ``.. roadmap::`` directive wraps the chart in a
docutils ``figure`` node.  Sphinx then numbers the figure (``Fig. 1``,
``Fig. 2``, …) and includes it in the List of Figures.  Users can
cross-reference the figure by name.

Enable ``numfig = True`` in :file:`conf.py` to activate "Figure N" numbering
and ``:numref:`` cross-references:

.. code-block:: python
   :caption: conf.py — enable figure numbering

    numfig = True

Then add ``:caption:`` (and optionally ``:name:`` and ``:align:``) to any
``.. roadmap::`` directive:

.. code:: rst

   .. roadmap::
      :caption: Q1 Sprint Overview
      :name: fig-q1-sprint
      :align: center
      :start: 2027-01-01

      section,name,start,end,row_group,link,tags
      Work,Task A,2027-01-01,2027-03-31,,,
      Work,Task B,2027-02-01,2027-04-30,,,

Which will render like this (numbered figure with caption):

.. roadmap::
   :caption: Q1 Sprint Overview
   :name: fig-q1-sprint
   :align: center
   :start: 2027-01-01

   section,name,start,end,row_group,link,tags
   Work,Task A,2027-01-01,2027-03-31,,,
   Work,Task B,2027-02-01,2027-04-30,,,

Cross-reference the figure by name::

   See :numref:`fig-q1-sprint` for the full timeline.
   Or: see :ref:`fig-q1-sprint`.


Making all roadmaps figures automatically
-----------------------------------------

Set ``doxtr_roadmap_figure = True`` in :file:`conf.py` to wrap **every**
``.. roadmap::`` as a figure automatically, without adding ``:caption:`` to
each directive.  The chart's ``:title:`` (or ``doxtr_roadmap_default_title``)
is used as the caption by default:

.. code-block:: python
   :caption: conf.py — global figure wrapping

    doxtr_roadmap_figure = True
    # Optional: set a fixed caption for all auto-wrapped figures.
    # None (default) → use each chart's :title: as the caption.
    doxtr_roadmap_figure_caption = None

When ``doxtr_roadmap_figure_caption`` is set to a non-empty string, that
string is used verbatim as the caption for any roadmap that does not carry
its own per-directive ``:caption:``.

**Caption precedence** (from highest to lowest):

1. Explicit ``:caption:`` option — used verbatim.
2. ``doxtr_roadmap_figure_caption`` if non-empty — global override.
3. The chart ``:title:`` (or ``doxtr_roadmap_default_title``) — default.

An ``:align:``-only wrap (no explicit ``:caption:``) also gets the chart title
as its caption by default, so the roadmap appears in the List of Figures
without any extra configuration.

.. note::

   The LaTeX/PDF builder emits ``\begin{figure}…\caption{…}\end{figure}``
   for every captioned roadmap.  These entries feed into ``\listoffigures``
   automatically when your LaTeX preamble includes it.  If
   ``doxtr_pdf_theme_core`` is in use, its ``show_list_of_figures``
   global controls whether ``\listoffigures`` is printed.


The CSV format
==============

The CSV must contain a header row followed by one or more data rows.  Only
``name``, ``start``, and ``end`` are required; every other column is optional
and may be omitted from the header entirely.  The recognised column names are:

.. list-table::
   :header-rows: 1
   :widths: 18 12 70

   * - Column
     - Required
     - Description
   * - ``section``
     - no
     - Section (group) name that this row belongs to.  If the value matches
       the ``name`` of an already-defined task in the same section, the row
       becomes a subtask of that task instead (see `Subtasks`_).  If left
       blank — or the column is omitted — the task renders with no section
       header (see `A roadmap without sections`_).
   * - ``name``
     - yes
     - Display name of the task or milestone shown on the Gantt bar.
   * - ``start``
     - yes
     - Start date in ISO format ``YYYY-MM-DD``.
   * - ``end``
     - yes
     - End date in ISO format ``YYYY-MM-DD``.  When ``start == end`` the row
       is rendered as a milestone diamond (see `Milestones`_).
   * - ``row_group``
     - no
     - Tasks that share the same non-empty ``row_group`` value are placed on
       a single Gantt row (see `Same-row grouping`_).
   * - ``link``
     - no
     - Plain ``https://`` URL or an ``:xlink:\`id\``` role expression.  When
       ``sphinxcontrib.xlink`` is loaded the ID is resolved to a URL and
       title (see `Links`_).
   * - ``tags``
     - no
     - Space- or comma-separated list of tag strings used for filtering (see
       `Tags and filtering`_).


Sections and tasks
==================

Every row belongs to a named section determined by its ``section`` value.
Rows that share the same section string are grouped under a single labelled
separator in the Gantt chart.  Sections appear in the order they are first
encountered in the CSV.

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


Subtasks
========

A row whose ``section`` value matches the ``name`` of an existing task in the
chart becomes a subtask of that parent task.  Subtasks are indented beneath
their parent in the rendered diagram.  For example, giving ``section`` the
value ``Backend Overhaul`` (which is an existing task name) makes the row a
subtask:

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

``Database Migration`` and ``API Redesign`` are rendered as subtasks of
``Backend Overhaul``.


Milestones
==========

When a row's ``start`` and ``end`` dates are identical, the extension renders
it as a Gantt milestone — a diamond marker on the timeline.  Milestones are
never clipped by the ``:start:`` / ``:end:`` date window.

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


Same-row grouping
=================

Tasks that share the same non-empty ``row_group`` value are placed on a
single Gantt row, displayed side-by-side.  This is useful for representing
parallel workstreams or paired activities that logically occupy the same swim
lane.

When ``row_group`` is used, enabling ``clean_style`` (the default) is
important: it suppresses the per-task start/end/duration column annotations
that would otherwise overlap on a shared row.

For two tasks to share a row cleanly, their bars *and* their text labels must
not overlap horizontally.  In the example below each pair is spaced far enough
apart in time that both labels have room to render side-by-side:

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

``API Redesign`` and ``Frontend Refresh`` share ``stream-a`` and appear on
one row; ``Security Audit`` and ``Compliance Check`` share ``stream-b`` and
appear on another.

.. note::

   If the tasks in a shared ``row_group`` would overlap in time — or their
   labels would run into one another — the extension automatically moves the
   colliding task to a new row so the text stays readable.  This is the
   default behaviour; see `Collision detection`_ below for how it works and
   how to turn it off.


Collision detection
-------------------

By default, the extension automatically detects when two tasks in the same
``row_group`` would have overlapping bar labels and splits them onto additional
rows rather than rendering illegible smeared text.  Tasks that fit together
without collision stay on one row (no unnecessary splits); only colliding tasks
are moved to a new row.  Collision is determined by estimating how many
calendar days each label occupies horizontally (based on the active
projectscale) and checking whether those footprints overlap.

Consider two tasks in the same ``row_group`` whose bars fully overlap in time.
With collision detection enabled (the default) they are automatically placed
on separate rows so both labels remain readable:

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

To force all same-group tasks onto one row regardless of overlap — for
example, when you deliberately want overlapping bars for a visual effect —
disable detection for a single chart with ``:collision-detection: false``.
With the *same* data as above, the two tasks are now packed onto a single
row and their labels overlap:

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

The label-width estimate can be tuned with
``doxtr_roadmap_collision_char_width_factor`` (default ``1.0``; higher values
reserve more space per character and cause earlier splits) and
``doxtr_roadmap_collision_gap_days`` (minimum calendar-day gap between tasks
on the same lane, default ``2``).

.. note::

   Collision detection is intentionally conservative: it slightly
   over-estimates label widths so that labels which are close to colliding
   are proactively split.  If you find the extension splitting tasks that
   look fine in your rendered output, lower ``doxtr_roadmap_collision_char_width_factor``
   (e.g. to ``0.7``) or set ``:collision-detection: false`` on that chart.

The ``:collision-char-width-factor:`` directive option applies the same tuning
per-chart, without changing the global default.  A value of ``1.0`` (the
default) is conservative — it reserves a full character-width of horizontal
space per label character, splitting tasks at the first sign of crowding.
Lowering the factor (e.g. to ``0.7``) reserves *less* space, so tasks need to
be actually closer before the extension decides to split them onto separate
rows.  Raising the factor above ``1.0`` makes splits happen even earlier.

The example below uses ``:collision-char-width-factor: 0.7`` on two
short-named tasks separated by a modest gap.  With the default factor of
``1.0`` the conservative label-width estimate would split them onto separate
rows; at ``0.7`` the estimator reserves less space, judges them clear, and
keeps them on one row:

.. code:: rst

   .. roadmap::
      :title: Collision factor 0.7 (less aggressive splitting)
      :scale: monthly
      :collision-char-width-factor: 0.7

      section,name,start,end,row_group,link,tags
      Lane,Import,2027-01-01,2027-01-20,lane,,eng
      Lane,Export,2027-02-15,2027-03-06,lane,,eng

Which will render like this (both tasks share one row because the lower factor
reserves less label space per character):

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


Periods and zooming
===================

A *period* is any named task in the CSV — typically a sprint or increment row
in a dedicated ``Periods`` section.  Specifying ``:period:`` clips the diagram
to exactly that task's date range.  When exactly one period is specified and
``:scale:`` is not set, the extension automatically switches to ``daily`` scale
and closes weekends, giving a fine-grained sprint view.

Multiple periods can be supplied as a comma-separated list; the clip window
spans from the earliest start to the latest end across all named periods.

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

Use ``:start:`` and ``:end:`` to clip the diagram to an explicit date window
without referring to a named period.  Tasks that fall entirely outside the
window are hidden; milestones are always preserved.  The ``:scale:`` option
controls the timeline unit (``daily``, ``weekly``, or ``monthly``), and
``:close-weekends:`` suppresses Saturday and Sunday columns.  Here
``:column-zoom: 4`` also widens each column fourfold so the clipped window
spreads across the full page width (see `Column width (zoom)`_).

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

``:title:`` overrides the diagram heading.  ``:scale:`` selects the timeline
granularity:

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


Column width (zoom)
===================

By default PlantUML sizes Gantt columns compactly, which can leave the chart
looking narrow on wide pages.  The ``:column-zoom:`` directive option (or the
global ``doxtr_roadmap_column_zoom`` config value) multiplies the width of each
time column by appending ``zoom <factor>`` to the ``projectscale`` line.

A zoom of ``1`` (the default) leaves column widths unchanged.  For example, a
zoom of ``2`` doubles each column’s width:

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

The ``:width:`` directive option forces the *rendered image* to fill a
specified width in HTML and PDF (via ``sphinxcontrib.plantuml``'s standard
image-width support).  Setting ``:width: 100%`` stretches the image to the
full available text width:

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

Without ``:width:``, the image uses its natural rendered size (current default
behaviour).  You can combine ``:width:`` with ``:column-zoom:`` to control
both the source column width and the final placement:

.. code:: rst

   .. roadmap::
      :column-zoom: 3
      :width: 100%
      :file: files/product-roadmap.csv

This widens each time column three-fold *and* stretches the image to the full
text width.

.. note::

   The ``zoom <factor>`` keyword form requires PlantUML v1.2026.7 or newer
   — already the extension's minimum baseline.


Links
=====

The ``link`` column attaches a URL to a task bar.  Two forms are supported:

**Plain URL** — any value that begins with ``https://`` or ``http://`` is
used directly as a hyperlink on the task bar.

**xlink role** — a value of the form ``:xlink:\`id\``` is resolved through
``sphinxcontrib.xlink`` (if loaded) to a URL and title drawn from the
project's ``.xlink`` files.  The resolved URL and title are emitted as a
PlantUML hyperlink.  If ``sphinxcontrib.xlink`` is not loaded, xlink-style
cells produce a one-time warning and the link is silently skipped.

The :file:`files/product-roadmap.csv` file used earlier already contains two
xlink links: ``API Redesign`` links to :xlink:`plantuml-home` and
``Compliance Review`` links to :xlink:`sphinx-home`.  To show a minimal
self-contained inline example:

.. code:: rst

   .. roadmap::
      :title: Projects with Links
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,:xlink:`plantuml-home`,eng
      Tools,Sphinx Migration,2027-03-01,2027-04-30,,:xlink:`sphinx-home`,eng code
      Tools,Docs Overhaul,2027-04-01,2027-05-31,,,code

Which will render like this (task bars for ``PlantUML Upgrade`` and
``Sphinx Migration`` are clickable in the HTML output):

.. roadmap::
   :title: Projects with Links
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,:xlink:`plantuml-home`,eng
   Tools,Sphinx Migration,2027-03-01,2027-04-30,,:xlink:`sphinx-home`,eng code
   Tools,Docs Overhaul,2027-04-01,2027-05-31,,,code


Link appendix
-------------

Links embedded inside the PlantUML image are **not clickable in PDF/LaTeX
output** — the image is rendered as a static graphic with no active
hyperlink areas.  The link appendix feature solves this by rendering the
task links as real docutils nodes placed *below*
the chart image.

The appendix is **on by default for PDF/LaTeX output** and **off for other
builders** (HTML, epub, …), whose image links are already clickable.  You can
change the mode, restrict or widen the builders, or disable it entirely —
globally in :file:`conf.py` or per-directive for a single chart.

**Global example — the default behaviour (appendix in PDF only):**

.. code-block:: python
   :caption: conf.py

    # Render task links as a bullet list below the chart in PDF/LaTeX output.
    doxtr_roadmap_link_appendix = "list"          # "list" | "footnote" | False
    doxtr_roadmap_link_appendix_builders = ["latex"]  # default; PDF only
    doxtr_roadmap_link_appendix_title = "Links"   # heading above the list

**Per-chart override:**

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :link-appendix: footnote
      :link-appendix-title: External References

Disable the appendix for one chart even when globally enabled::

   .. roadmap::
      :link-appendix: off
      :file: roadmap.csv

**Builder restriction.**  The ``doxtr_roadmap_link_appendix_builders`` list
is checked against both ``builder.name`` (e.g. ``"latex"``, ``"html"``) and
``builder.format`` (e.g. ``"latex"``, ``"html"``).  Use the special value
``"all"`` (or a list containing ``"*"``) to render the appendix for every
builder::

    doxtr_roadmap_link_appendix_builders = "all"

This means the same RST source builds an image-only HTML page and an
image-plus-appendix PDF page — no per-format conditionals needed.

**Mode: ``"list"`` vs ``"footnote"``.**

- ``"list"`` — a ``nodes.bullet_list``; each item is
  ``<Task Name>: <clickable URL or title>``.  Always rendered as a
  standalone block below the chart, regardless of whether the roadmap
  is wrapped in a figure.
- ``"footnote"`` — real reStructuredText auto-numbered footnotes.
  In PDF/LaTeX output Sphinx's LaTeX writer renders these as page-bottom
  ``\footnote{}`` commands.  In HTML they render as standard numbered
  footnotes with back-references.

  **When the roadmap is a figure** (via ``:caption:``, ``:align:``, or
  ``doxtr_roadmap_figure = True``) and the builder is in
  ``link_appendix_builders``, footnote mode embeds the links compactly
  **inside the figure caption** instead of a separate "Links" block.
  The caption shows a single label word (the ``link_appendix_title``,
  default ``"Links"``) followed by one auto-numbered footnote marker
  per link:

  .. code-block:: text

     Projects with Links (Links [1], [2])

  With ``numfig = True`` this renders as e.g.
  *Fig. 13.19: Projects with Links (Links\ :sup:`9`\ ,\ :sup:`10`\)*.

  Each footnote body carries the task name, the link title (when available
  via xlink resolution), and the URL:

  .. code-block:: text

     [1] API Redesign: https://example.com/api
     [2] Sphinx Migration >> Sphinx Docs: https://www.sphinx-doc.org

  Form with a plain URL (no resolved title): ``<Task Name>: <url>``.
  Form with a resolved title (xlink): ``<Task Name> >> <Title>: <url>``.

  The footnote definitions follow as sibling nodes after the figure.
  No separate "Links" rubric or container is emitted.  If there are no
  resolvable links the caption is the plain title with no brackets.

  Without a figure, ``"footnote"`` still produces the standalone footnote
  appendix below the chart (unchanged behaviour).

**Live example** (bullet list, rendered for all builders here):

.. code:: rst

   .. roadmap::
      :title: Projects with Links
      :link-appendix: list
      :link-appendix-title: Task links
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,https://plantuml.com,eng
      Tools,Sphinx Migration,2027-03-01,2027-04-30,,https://www.sphinx-doc.org,
      Tools,Internal Task,2027-04-01,2027-05-31,,,ops

Which will render like this (the chart image is always shown; the link
appendix appears below it in PDF/LaTeX output where
``doxtr_roadmap_link_appendix_builders = ["latex"]`` matches the builder):

.. roadmap::
   :title: Projects with Links
   :link-appendix: list
   :link-appendix-title: Task links
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,https://plantuml.com,eng
   Tools,Sphinx Migration,2027-03-01,2027-04-30,,https://www.sphinx-doc.org,
   Tools,Internal Task,2027-04-01,2027-05-31,,,ops

The same chart with ``footnote`` mode produces real page-bottom footnotes
in PDF and numbered footnotes in HTML instead of a bullet list:

.. code:: rst

   .. roadmap::
      :title: Projects with Links
      :link-appendix: footnote
      :link-appendix-title: Task links
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,https://plantuml.com,eng
      Tools,Sphinx Migration,2027-03-01,2027-04-30,,https://www.sphinx-doc.org,
      Tools,Internal Task,2027-04-01,2027-05-31,,,ops

Which will render like this:

.. roadmap::
   :title: Projects with Links
   :link-appendix: footnote
   :link-appendix-title: Task links
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,https://plantuml.com,eng
   Tools,Sphinx Migration,2027-03-01,2027-04-30,,https://www.sphinx-doc.org,
   Tools,Internal Task,2027-04-01,2027-05-31,,,ops


Tags and filtering
==================

Each row may carry one or more space- or comma-separated tags in the ``tags``
column.  The ``:tags:`` directive option filters which rows are included in
the rendered diagram.

The filter syntax is the same nested-bracket syntax used by
``sphinxcontrib.xlink`` (see the :doc:`xlink chapter </extensions/xlink/xlink>`
for the full syntax reference):

- ``eng`` — include rows that carry the ``eng`` tag.
- ``!security`` — exclude rows that carry ``security``.
- ``eng [ backend !! ]`` — include ``eng``; within that, hide ``backend`` and
  cascade the exclusion to any subtags.
- ``eng, security`` — include rows with ``eng`` *or* ``security``.

For example, to show only security-related items from the tagged roadmap:

.. code:: rst

   .. roadmap::
      :file: files/tagged-roadmap.csv
      :title: Security Items Only
      :tags: security

Which will render like this:

.. roadmap::
   :file: files/tagged-roadmap.csv
   :title: Security Items Only
   :tags: security

To include both engineering and security tasks:

.. code:: rst

   .. roadmap::
      :file: files/tagged-roadmap.csv
      :title: Engineering and Security
      :tags: eng, security

Which will render like this:

.. roadmap::
   :file: files/tagged-roadmap.csv
   :title: Engineering and Security
   :tags: eng, security

To restrict which tag values are valid project-wide, configure
``doxtr_roadmap_allowed_tags`` (an exact-match allow-list) and/or
``doxtr_roadmap_allowed_tag_patterns`` (regex patterns) in
:file:`conf.py`.  Tags not in either list emit a build warning:

.. code-block:: python
   :caption: conf.py — tag allow-lists

    # Exact tag names and their optional display labels
    doxtr_roadmap_allowed_tags = {
        "eng":      "Engineering",
        "code":     "Code",
        "ops":      "Operations",
        "security": "Security",
    }

    # Regex patterns for dynamically named tags (e.g. sprint-N, v\d+)
    doxtr_roadmap_allowed_tag_patterns = {
        r"sprint-\d+": "Sprint",
        r"v\d+":       "Version",
    }


Query filtering
===============

The ``:query:`` option accepts a Python expression that is evaluated per row.
Rows for which the expression returns a truthy value are included; all others
are excluded.  The expression is evaluated by a **restricted safe evaluator**
— attribute access, subscript access, lambdas, comprehensions, and arbitrary
imports are all forbidden, preventing sandbox escape.

The following names are available inside the expression:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Name
     - Type
     - Description
   * - ``name``
     - ``str``
     - Task display name.
   * - ``start``
     - ``datetime.date``
     - Task start date.
   * - ``end``
     - ``datetime.date``
     - Task end date.
   * - ``section``
     - ``str``
     - Section name for this row.
   * - ``tags``
     - ``set[str]``
     - Set of tag strings from the ``tags`` column.
   * - ``row_group``
     - ``str | None``
     - Row-group label, or ``None`` if not set.
   * - ``match(pattern, string)``
     - ``bool``
     - Safe regex helper; returns ``bool(re.search(pattern, string))`` without
       exposing the ``re`` module.

Safe built-in callables: ``any``, ``all``, ``bool``, ``set``, ``len``.

.. note::

   The safe evaluator forbids attribute access (``obj.attr``), so expressions
   like ``(end - start).days`` are not permitted.  Use the ``match()`` helper
   for regex checks and the ``in`` operator for tag membership tests.

For example, to include only rows that carry the ``eng`` tag:

.. code:: rst

   .. roadmap::
      :file: files/tagged-roadmap.csv
      :title: Engineering Tasks
      :query: "eng" in tags

Which will render like this:

.. roadmap::
   :file: files/tagged-roadmap.csv
   :title: Engineering Tasks
   :query: "eng" in tags

To include tasks whose names contain a digit (for example, sprint or versioned items):

.. code:: rst

   .. roadmap::
      :file: files/product-roadmap.csv
      :title: Versioned or Numbered Tasks
      :query: match(r"\d", name)

Which will render like this:

.. roadmap::
   :file: files/product-roadmap.csv
   :title: Versioned or Numbered Tasks
   :query: match(r"\d", name)

A row that raises an exception during evaluation is **included** (fail-open),
and a deduplicated warning is logged.


Styling
=======

All styling is controlled by ``doxtr_roadmap_*`` config values in
:file:`conf.py`.  Directive-level overrides (such as ``:clean-style:``) take
precedence over the global config.

.. code-block:: python
   :caption: conf.py — styling configuration

    # Global bar colours
    doxtr_roadmap_bar = {
        "done_color":   "#FF8C00",   # colour for the completed portion
        "undone_color": "#FFF3E0",   # colour for the remaining portion
        "frame_color":  None,        # bar border colour (None = default)
    }

    # Per-section overrides (keyed by exact section name)
    doxtr_roadmap_sections = {
        "Platform": {
            "done":  "#1976D2",       # blue bars for this section
            "frame": None,
            "frame_overrides": {
                "Backend Overhaul": "#E53935",  # red border on one task
            },
        },
    }

    # Today marker colour
    doxtr_roadmap_today = {"color": "#E53935"}

    # Font overrides for title, task labels, section separators
    doxtr_roadmap_fonts = {
        "title":     {"name": None, "size": 24, "style": "bold",  "color": None},
        "task":      {"name": None, "size": 14, "style": None,    "color": None},
        "separator": {"name": None, "size": 16, "style": "bold",  "color": None},
    }

    # Closed (non-working) day background colour
    doxtr_roadmap_closed = {"background_color": None}

    # Default scale and diagram zoom factor
    doxtr_roadmap_default_scale = "monthly"   # daily | weekly | monthly
    doxtr_roadmap_scale_factor  = 1.25

clean_style and the hide-column directives
------------------------------------------

``doxtr_roadmap_clean_style = True`` (the default) instructs PlantUML to hide
the per-task **Start**, **End**, and **Duration** columns from the Gantt table.
This keeps the diagram tidy and is essential when ``row_group`` grouping is
active, as the date stamps from multiple tasks sharing a row would otherwise
overlap.

``clean_style`` defaults to ``True`` because PlantUML v1.2026.7 — the
extension's minimum baseline — fully supports the ``hide column
start/end/duration`` syntax.  To disable it globally:

.. code-block:: python
   :caption: conf.py

    doxtr_roadmap_clean_style = False

The ``:clean-style:`` directive option overrides the global setting for a
single directive instance:

.. code:: rst

   .. roadmap::        ← bare flag or explicit true enables clean_style
      :clean-style:
      :file: roadmap.csv

   .. roadmap::        ← explicit false disables clean_style for this block
      :clean-style: false
      :file: roadmap.csv


Theme integration
=================

When ``doxtr_pdf_theme_core`` is present in ``extensions``, ``doxtr_roadmap``
automatically reads its semantic palette and typography globals to colour the
roadmap consistently with the rest of the PDF output.  User-configured
``doxtr_roadmap_*`` values always take precedence over theme-core values.

.. code-block:: python
   :caption: conf.py — theme-core integration

    # "auto"  → active if doxtr_pdf_theme_core is in extensions (default)
    # True    → always active (warns if core is absent)
    # False   → never active; use only explicit doxtr_roadmap_* values
    doxtr_roadmap_use_theme_core = "auto"

When active, the following palette keys are mapped:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Palette key
     - Maps to
   * - ``primary``
     - Bar ``done_color``
   * - ``secondary``
     - Today marker ``color``
   * - ``main_font``
     - Task font name
   * - ``sans_font``
     - Separator font name


Directive options reference
===========================

The following table summarises every option accepted by the ``.. roadmap::``
directive.  Per-directive options always override the corresponding global
``doxtr_roadmap_*`` config value.

.. list-table::
   :header-rows: 1
   :widths: 30 28 42

   * - Option
     - Accepted values / type
     - Description
   * - ``:file:``
     - path(s) / glob(s)
     - One or more CSV paths and/or glob patterns, space- or comma-separated.
       All matched files are combined into a single roadmap: sections merge by
       name and subtasks / ``row_group`` references work across files.  Glob
       metacharacters (``*``, ``?``, ``[…]``) are expanded; within each glob
       the matches are sorted lexicographically.  A single path with no
       separators behaves as before.  Paths are resolved relative to the
       document directory first, then ``srcdir``.  Adding a new file matching
       a glob may require a clean rebuild (see `Multiple files and globs`_).
   * - ``:title:``
     - text
     - Override the diagram title.  Falls back to
       ``doxtr_roadmap_default_title`` (``"Roadmap"`` by default).
   * - ``:scale:``
     - ``daily`` | ``weekly`` | ``monthly``
     - Timeline granularity.  Defaults to ``doxtr_roadmap_default_scale``
       (``"monthly"``).
   * - ``:start:``
     - ISO date (``YYYY-MM-DD``)
     - Clip-window start date.  Tasks ending before this date are hidden.
   * - ``:end:``
     - ISO date (``YYYY-MM-DD``)
     - Clip-window end date.  Tasks starting after this date are hidden.
   * - ``:period:``
     - comma-separated period names
     - Named period(s) to zoom to.  When a single period is given, scale
       auto-switches to ``daily`` and weekends are closed.
   * - ``:close-weekends:``
     - flag (no value)
     - Force weekend columns closed regardless of the active scale.
   * - ``:clean-style:``
     - ``true`` | ``false``; bare flag = ``true``
     - Hide the Start, End, and Duration columns.  Overrides
       ``doxtr_roadmap_clean_style`` for this chart.
   * - ``:tags:``
     - nested filter expression
     - Tag-based row filter (``eng``, ``!security``, ``eng, ops``, etc.).
   * - ``:query:``
     - safe Python expression
     - Expression-based row filter evaluated per row.  Available names:
       ``name``, ``start``, ``end``, ``section``, ``tags``, ``row_group``,
       ``match(pattern, string)``.
   * - ``:collision-detection:``
     - ``true`` | ``false``; bare flag = ``true``
     - Enable or disable automatic collision detection for same-row tasks.
       Overrides ``doxtr_roadmap_collision_detection``.
   * - ``:collision-char-width-factor:``
     - float (e.g. ``0.7``)
     - Label-width tuning: higher values split sooner, lower values pack
       more tightly.  Overrides
       ``doxtr_roadmap_collision_char_width_factor``.
   * - ``:column-zoom:``
     - float (e.g. ``2``)
     - Gantt time-column width multiplier.  ``1`` = unchanged (default).
       Overrides ``doxtr_roadmap_column_zoom``.
   * - ``:width:``
     - length or ``%`` (e.g. ``100%``, ``600px``)
     - Force the rendered image to fill the specified width in HTML and
       PDF.  Passed directly to ``sphinxcontrib.plantuml``.
   * - ``:link-appendix:``
     - ``list`` | ``footnote`` | ``off``; bare flag = ``list``
     - Render task links as real docutils nodes below the chart.  ``list``
       = bullet list; ``footnote`` = real RST auto-numbered footnotes
       (LaTeX ``\footnote`` in PDF, numbered footnotes in HTML);
       ``off`` = disable.
       Overrides ``doxtr_roadmap_link_appendix``.
   * - ``:link-appendix-title:``
     - text
     - Heading text above the link appendix.  Empty string suppresses the
       heading.  Overrides ``doxtr_roadmap_link_appendix_title``.
   * - ``:caption:``
     - text
     - Caption text for the roadmap chart.  When present, wraps the chart in
       a ``nodes.figure`` so it is numbered and appears in the List of Figures.
       Enable ``numfig = True`` in ``conf.py`` for "Figure N" numbering and
       ``:numref:`` cross-references.
   * - ``:align:``
     - ``left`` | ``center`` | ``right``
     - Horizontal alignment of the figure.  Also triggers figure wrapping even
       without ``:caption:``.
   * - ``:name:``
     - text
     - Cross-reference target for the figure (use with ``:numref:`` or
       ``:ref:``).  Attach only to a figure that has a caption or align.


Configuration reference
=======================

The following table lists all ``doxtr_roadmap_*`` config values with their
defaults.  Set any of them in :file:`conf.py`.

.. list-table::
   :header-rows: 1
   :widths: 42 16 42

   * - Config key
     - Default
     - Description
   * - ``doxtr_roadmap_default_scale``
     - ``"monthly"``
     - Default timeline unit: ``daily``, ``weekly``, or ``monthly``.
   * - ``doxtr_roadmap_scale_factor``
     - ``1.25``
     - PlantUML top-level ``scale`` zoom factor.
   * - ``doxtr_roadmap_default_start``
     - ``None``
     - Default clip-window start date (ISO string).  ``None`` falls back to
       today.
   * - ``doxtr_roadmap_default_title``
     - ``"Roadmap"``
     - Diagram title when ``:title:`` is not set.
   * - ``doxtr_roadmap_clean_style``
     - ``True``
     - Hide Start/End/Duration columns.  Requires PlantUML v1.2026.7+.
   * - ``doxtr_roadmap_close_weekends_on_single_period``
     - ``True``
     - Auto-close weekends when exactly one period is rendered.
   * - ``doxtr_roadmap_bar``
     - see above
     - Global bar colours: ``done_color``, ``undone_color``, ``frame_color``.
   * - ``doxtr_roadmap_sections``
     - ``{}``
     - Per-section colour overrides.
   * - ``doxtr_roadmap_today``
     - ``{"color": "#E53935"}``
     - Today-marker colour.
   * - ``doxtr_roadmap_fonts``
     - see above
     - Font name/size/style/color for ``title``, ``task``, ``separator``,
       ``month``, and ``year`` elements.
   * - ``doxtr_roadmap_closed``
     - ``{"background_color": None}``
     - Background colour for closed (non-working) days.
   * - ``doxtr_roadmap_use_theme_core``
     - ``"auto"``
     - Theme-core integration: ``"auto"``, ``True``, or ``False``.
   * - ``doxtr_roadmap_allowed_tags``
     - ``{}``
     - Optional tag allow-list mapping tag names to display strings.
   * - ``doxtr_roadmap_allowed_tag_patterns``
     - ``{}``
     - Optional regex patterns for allowed tag names.
   * - ``doxtr_roadmap_require_plantuml_version``
     - ``"error"``
     - Version-check behaviour: ``"error"`` aborts the build if PlantUML is
       below v1.2026.7; ``"warn"`` emits a warning but continues; ``"off"``
       or ``False`` skips the check entirely.
   * - ``doxtr_roadmap_collision_detection``
     - ``True``
     - Enable automatic collision detection for ``row_group`` same-row tasks.
       When ``True`` (default), tasks whose bars or labels overlap are split
       onto additional rows.  Set to ``False`` to force all same-group tasks
       onto one row regardless of overlap.
   * - ``doxtr_roadmap_collision_char_width_factor``
     - ``1.0``
     - Label-width tuning knob for collision detection.  Higher values
       reserve more horizontal space per label character, causing splits
       sooner.  Lower values pack tasks more tightly.
   * - ``doxtr_roadmap_collision_gap_days``
     - ``2``
     - Minimum calendar-day gap between adjacent tasks on the same lane
       after accounting for the left task's label.
   * - ``doxtr_roadmap_column_zoom``
     - ``1``
     - Gantt time-column width multiplier.  ``1`` (default) leaves column
       widths unchanged.  Higher values (e.g. ``3``) widen each time column
       proportionally via ``projectscale monthly zoom 3``.  Requires PlantUML
       v1.2026.7+ (already the extension minimum).
   * - ``doxtr_roadmap_link_appendix``
     - ``"list"``
     - Render task links as real docutils nodes below the chart image.
       ``"list"`` (default) produces a bullet list; ``"footnote"``
       produces real RST auto-numbered footnotes (rendered as page-bottom
       ``\footnote{}`` in PDF/LaTeX, numbered footnotes in HTML);
       ``False`` / ``"off"`` disables the feature.  The
       ``link_appendix_builders`` setting restricts *which* builders render
       it (default PDF/latex only).
   * - ``doxtr_roadmap_link_appendix_builders``
     - ``["latex"]``
     - Builder names/formats that render the appendix.  Checked against both
       ``builder.name`` and ``builder.format``.  Use ``"all"`` (or
       ``["*"]``) for every builder.  Default ``["latex"]`` means PDF gets
       the appendix; HTML/epub don't unless opted in.
   * - ``doxtr_roadmap_link_appendix_title``
     - ``"Links"``
     - Heading text rendered above the link appendix list.  Set to an empty
       string or ``None`` to suppress the heading.
   * - ``doxtr_roadmap_figure``
     - ``False``
     - When ``True``, every ``.. roadmap::`` is wrapped as a numbered figure
       automatically, even without a per-directive ``:caption:``.  The caption
       defaults to the chart title (or ``doxtr_roadmap_figure_caption`` when
       set).  Enable ``numfig = True`` in ``conf.py`` for ``Figure N``
       numbering and ``:numref:`` cross-references.
   * - ``doxtr_roadmap_figure_caption``
     - ``None``
     - Optional default caption text used when ``doxtr_roadmap_figure = True``
       and no per-directive ``:caption:`` is given.  ``None`` (default) falls
       back to the chart title.  Caption precedence: explicit ``:caption:``
       option → ``doxtr_roadmap_figure_caption`` (if non-empty) → chart title.
