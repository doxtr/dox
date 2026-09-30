.. _doto-lists:

Listing tasks
*************

``.. doto-list::`` renders a filtered, sorted view of every task collected during the
build.  It can output a list, a table, or cards, and accepts a rich set of filter
and display options.

.. note::

   The lists below draw on the tasks defined on the :doc:`tasks` page (``AUTH-001``,
   ``TASK-LOW`` … ``TASK-CRIT``, ``STATUS-OPEN`` … ``STATUS-DONE``).

Default list
============

With no options, ``doto-list`` shows every task sorted by priority, highest first.

.. code:: rst

   .. doto-list::

Which will render like this:

.. doto-list::

As a table with explicit columns
================================

The ``:format: table`` option renders a table; ``:columns:`` selects which fields
appear and in what order.

.. code:: rst

   .. doto-list::
      :format: table
      :columns: id, title, assignee, priority, status, due, progress

Which will render like this:

.. doto-list::
   :format: table
   :columns: id, title, assignee, priority, status, due, progress

As cards
========

.. code:: rst

   .. doto-list::
      :format: cards
      :status: open, in-progress

Which will render like this:

.. doto-list::
   :format: cards
   :status: open, in-progress

Sorting by priority
===================

``:sort:`` accepts one or more fields (comma-separated); ``:order:`` chooses ``asc``
or ``desc``.  Sorting by priority descending puts ``critical`` first.

.. code:: rst

   .. doto-list::
      :sort: priority
      :order: desc
      :format: table
      :columns: id, title, priority, status

Which will render like this:

.. doto-list::
   :sort: priority
   :order: desc
   :format: table
   :columns: id, title, priority, status

Filtering
=========

Filter by assignee and tag, and choose the columns to show:

.. code:: rst

   .. doto-list::
      :assignee: alice
      :tags: security
      :format: table
      :columns: id, title, tags, due

Which will render like this:

.. doto-list::
   :assignee: alice
   :tags: security
   :format: table
   :columns: id, title, tags, due

Filter by priority, sort by due date ascending, and limit the number of rows:

.. code:: rst

   .. doto-list::
      :priority: high, critical
      :sort: due
      :order: asc
      :limit: 5
      :format: table
      :columns: id, title, priority, due

Which will render like this:

.. doto-list::
   :priority: high, critical
   :sort: due
   :order: asc
   :limit: 5
   :format: table
   :columns: id, title, priority, due

Filter by a date window and exclude a status:

.. code:: rst

   .. doto-list::
      :due-after: 2099-01-01
      :due-before: 2099-12-31
      :exclude-status: done
      :format: list

Which will render like this:

.. doto-list::
   :due-after: 2099-01-01
   :due-before: 2099-12-31
   :exclude-status: done
   :format: list

List options
============

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Option
     - Values
     - Default
   * - ``:sort:``
     - ``priority``, ``due``, ``status``, ``assignee``, ``created``, ``title``, ``id``
     - ``priority``
   * - ``:order:``
     - ``asc``, ``desc``
     - ``desc``
   * - ``:limit:``
     - non-negative integer
     - none
   * - ``:format:``
     - ``table``, ``list``, ``cards``
     - ``list``
   * - ``:columns:``
     - any of ``id, title, assignee, priority, status, due, tags, depends-on, progress, created, updated``
     - ``id, title, priority, status``
   * - ``:show-archived:``
     - ``true`` / ``false``
     - ``false``
   * - ``:icon-mode:``
     - ``icon``, ``icon-text``, ``text``
     - config ``doto_list_icon_mode``

Filter options: ``:assignee:``, ``:priority:``, ``:status:``, ``:tags:``,
``:due-before:``, ``:due-after:``, ``:depends-on:``, ``:regex:``,
``:exclude-status:`` (all comma-separated where applicable).
