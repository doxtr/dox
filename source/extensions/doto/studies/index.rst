Studies
=======

A worked example data set for the ``doto`` extension: a student's study notes
that grew over time, from secondary-school subjects through to a first- and
second-year university programme. Each subject/module folder is its own *doto
repository* (it has a ``.doto.toml`` and a ``.doto/tasks.json``), so you can
test cross-repo discovery, filtering, aggregation, and time-tracking.

Each subject uses its own task-ID prefix -- a task created in
``highschool/maths/`` becomes ``MATHS-001``, one in
``university/cs101-programming/`` becomes ``CS101-001``, and so on.

.. toctree::
   :maxdepth: 2

   highschool/index
   university/index

Try it out
----------

From any subject/module folder (for example ``highschool/maths/`` or
``university/cs201-data-structures/``)::

   doto list                 # tasks in this repo
   doto list --status open   # filter by status
   doto stats --by-status    # aggregate counts
   doto timesheet            # logged time
   doto tui                  # interactive view

To discover and aggregate across every subject, run from ``studies/``::

   doto repos rescan .
   doto repos
