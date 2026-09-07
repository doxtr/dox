Filtering
*********

.. _roadmap-tags-and-filtering:

Tags and filtering
==================

Each row may carry one or more space- or comma-separated tags in the ``tags`` column.  The ``:tags:`` directive option filters which rows are included in the rendered diagram.

The filter syntax is the same nested-bracket syntax used by ``sphinxcontrib.xlink`` (see the :doc:`xlink chapter </extensions/xlink/xlink>` for the full syntax reference):

- ``eng`` — include rows that carry the ``eng`` tag.
- ``!security`` — exclude rows that carry ``security``.
- ``eng [ backend !! ]`` — include ``eng``; within that, hide ``backend`` and cascade the exclusion to any subtags.
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

To restrict which tag values are valid project-wide, configure ``doxtr_roadmap_allowed_tags`` (an exact-match allow-list) and/or ``doxtr_roadmap_allowed_tag_patterns`` (regex patterns) in :file:`conf.py`.  Tags not in either list emit a build warning:

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

The ``:query:`` option accepts a Python expression that is evaluated per row.  Rows for which the expression returns a truthy value are included; all others are excluded.  The expression is evaluated by a **restricted safe evaluator** — attribute access, subscript access, lambdas, comprehensions, and arbitrary imports are all forbidden, preventing sandbox escape.

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
     - Safe regex helper; returns ``bool(re.search(pattern, string))`` without exposing the ``re`` module.

Safe built-in callables: ``any``, ``all``, ``bool``, ``set``, ``len``.

.. note::

   The safe evaluator forbids attribute access (``obj.attr``), so expressions like ``(end - start).days`` are not permitted.  Use the ``match()`` helper for regex checks and the ``in`` operator for tag membership tests.

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

A row that raises an exception during evaluation is **included** (fail-open), and a deduplicated warning is logged.
