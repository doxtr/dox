.. _doto-tasks:

Defining tasks
**************

A task is declared with ``.. doto:: <title>``.  The title is the only required
argument.  Everything else is supplied through options, and the directive body is
parsed as reStructuredText.

A fully specified task
======================

The block below uses every option the ``doto`` directive accepts.  The source is
shown first, then the rendered task box.

.. code:: rst

   .. doto:: Harden the authentication flow
      :id: AUTH-001
      :assignee: alice
      :priority: critical
      :status: in-progress
      :due: 2099-08-15
      :tags: security, backend
      :depends-on: AUTH-000
      :progress: 40
      :created: 2099-01-10
      :updated: 2099-02-01

      Rotate signing keys, add rate limiting to the login endpoint, and require
      MFA for admin accounts. This body is parsed as reST, so you can use
      **bold**, ``code``, lists, and links.

      - Rotate signing keys
      - Add rate limiting
      - Require MFA for admins

Which will render like this:

.. doto:: Harden the authentication flow
   :id: AUTH-001
   :assignee: alice
   :priority: critical
   :status: in-progress
   :due: 2099-08-15
   :tags: security, backend
   :depends-on: AUTH-000
   :progress: 40
   :created: 2099-01-10
   :updated: 2099-02-01

   Rotate signing keys, add rate limiting to the login endpoint, and require
   MFA for admin accounts. This body is parsed as reST, so you can use
   **bold**, ``code``, lists, and links.

   - Rotate signing keys
   - Add rate limiting
   - Require MFA for admins

Task options
============

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Option
     - Meaning
     - Valid values / format
   * - ``:id:``
     - Explicit task ID (auto-generated ``{docname}-L{lineno}`` if omitted)
     - letters, numbers, ``-``, ``_``, ``.``
   * - ``:assignee:``
     - Person responsible
     - free text
   * - ``:priority:``
     - Task priority
     - ``low``, ``medium``, ``high``, ``critical``
   * - ``:status:``
     - Task status
     - ``open``, ``in-progress``, ``blocked``, ``done``
   * - ``:due:``
     - Due date
     - ``YYYY-MM-DD`` (relative forms also accepted)
   * - ``:tags:``
     - Comma-separated tags
     - free text list
   * - ``:depends-on:``
     - Task IDs this task depends on
     - comma-separated task IDs
   * - ``:progress:``
     - Percent complete
     - integer ``0``–``100``
   * - ``:created:``
     - Creation date
     - ``YYYY-MM-DD``
   * - ``:updated:``
     - Last-updated date
     - ``YYYY-MM-DD``

One task per priority
=====================

Priority drives sorting in lists and the colour of the task box in PDF output.

.. code:: rst

   .. doto:: Low priority cleanup task
      :id: TASK-LOW
      :priority: low
      :status: open
      :due: 2099-12-01

   .. doto:: Critical outage remediation
      :id: TASK-CRIT
      :priority: critical
      :status: in-progress
      :due: 2099-12-01

Which will render like this:

.. doto:: Low priority cleanup task
   :id: TASK-LOW
   :priority: low
   :status: open
   :due: 2099-12-01

.. doto:: Medium priority documentation task
   :id: TASK-MED
   :priority: medium
   :status: open
   :due: 2099-12-01

.. doto:: High priority bug fix
   :id: TASK-HIGH
   :priority: high
   :status: blocked
   :due: 2099-12-01

.. doto:: Critical outage remediation
   :id: TASK-CRIT
   :priority: critical
   :status: in-progress
   :due: 2099-12-01

One task per status
===================

Status is used by filters (for example ``:exclude-status: done``) and by the
summary directive.

.. code:: rst

   .. doto:: An open task
      :id: STATUS-OPEN
      :status: open

   .. doto:: A completed task
      :id: STATUS-DONE
      :status: done
      :progress: 100

Which will render like this:

.. doto:: An open task
   :id: STATUS-OPEN
   :status: open

.. doto:: An in-progress task
   :id: STATUS-INPROGRESS
   :status: in-progress
   :progress: 60

.. doto:: A blocked task
   :id: STATUS-BLOCKED
   :status: blocked
   :depends-on: TASK-CRIT

.. doto:: A completed task
   :id: STATUS-DONE
   :status: done
   :progress: 100
