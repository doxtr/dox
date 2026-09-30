.. _doto-cli:

Command-line interface
**********************

The ``doto`` CLI manages the same tasks that the directives render.  It reads and
writes the JSON task store, so tasks created on the command line appear in
``doto-list``/``doto-summary`` output on the next build, and tasks edited in your
documentation are reflected back on the command line.

Install the CLI with the ``cli`` extra:

.. code-block:: console

    $ pip install "doxtr-doto[cli]"

Initializing a task repository
==============================

``doto init`` creates the configuration and an empty task store.  Run it from the
root of your Sphinx project.  It writes :file:`.doto.toml`, :file:`.doto/tasks.json`,
and an inbox file for new tasks:

.. code-block:: console

    $ doto init
    ✓ Created .doto.toml
    ✓ Created .doto/tasks.json

If you want to manage a personal task list that is not tied to a documentation
project, use standalone mode.  It keeps everything in your home directory under
:file:`~/.doto/`:

.. code-block:: console

    $ doto init --standalone

    Standalone mode initialized.
    Use 'doto add' to create your first task.

Storing tasks in a dedicated folder
====================================

By default the task store lives in :file:`.doto/tasks.json`.  If you prefer to keep
tasks in a dedicated folder, for example a :file:`tasks/` directory at the root of
your project, create the folder and point the CLI at a JSON file inside it with the
global ``--json`` option:

.. code-block:: console

    $ mkdir -p tasks
    $ doto --json tasks/tasks.json add "Write installation guide"

The same ``--json`` path applies to every subcommand (``add``, ``list``, ``stats``,
and so on).  To make the choice permanent so the directives and the CLI share one
store, set ``doto_json_file`` in :file:`conf.py`:

.. code-block:: python
   :caption: conf.py — point the store at tasks/

    doto_json_file = "tasks/tasks.json"

With that in place you no longer need ``--json`` on each command inside the project.

Creating tasks
==============

``doto add`` creates a task.  The title can be several words; options set the
metadata:

.. code-block:: console

    $ doto add "Write installation guide" \
        --priority high --assignee alice --tags docs --due 2099-09-01
    ✓ Added task DOTO-001
    ╭─ DOTO-001 - Write installation guide ─────────────────────────────────────╮
    │ Assignee: alice                                                            │
    │ Priority: high                                                             │
    │ Status: open                                                               │
    │ Due: 2099-09-01                                                            │
    │ Tags: docs                                                                 │
    ╰────────────────────────────────────────────────────────────────────────────╯

    $ doto add "Fix broken links in API docs" \
        --priority critical --status in-progress --tags docs,api
    ✓ Added task DOTO-002

    $ doto add "Review changelog wording" --priority low --tags docs
    ✓ Added task DOTO-003

Common ``add`` options:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Meaning
   * - ``-I, --id``
     - Explicit task ID (auto-generated if omitted)
   * - ``-a, --assignee``
     - Assignee name
   * - ``-p, --priority``
     - Task priority
   * - ``-s, --status``
     - Task status
   * - ``-d, --due``
     - Due date (``YYYY-MM-DD`` or relative such as ``+7d`` or ``friday``)
   * - ``-t, --tags``
     - Comma-separated tags
   * - ``-D, --depends-on``
     - Comma-separated dependency task IDs
   * - ``-b, --body``
     - Task description/body
   * - ``-n, --dry-run``
     - Show the result without writing

Listing and filtering tasks
============================

``doto list`` shows the current tasks.  Filters accept comma-separated values and
combine with AND across different fields:

.. code-block:: console

    $ doto list --status open,in-progress --priority high,critical
       ID         Priority   Status        Assignee   Due          Title
      ────────────────────────────────────────────────────────────────────────────
       DOTO-002   critical   in-progress   -          -            Fix broken links
                                                                    in API docs
       DOTO-001   high       open          alice      2099-09-01   Write
                                                                    installation guide

    2 tasks

Available filters: ``--assignee``, ``--priority``, ``--status``, ``--tags``,
``--due-before``, ``--due-after``, and ``--archived``.

Sorting by priority
====================

Use ``--sort`` to order the results.  Sorting by priority lists the most important
tasks first; add ``--reverse`` to flip the order:

.. code-block:: console

    $ doto list --sort priority
       ID         Priority   Status        Assignee   Due          Title
      ────────────────────────────────────────────────────────────────────────────
       DOTO-002   critical   in-progress   -          -            Fix broken links
                                                                    in API docs
       DOTO-001   high       open          alice      2099-09-01   Write
                                                                    installation guide
       DOTO-003   low        open          -          -            Review changelog
                                                                    wording

    3 tasks

``--sort`` accepts multiple fields (comma-separated), for example
``--sort due,priority``.  Other output formats are available through
``--format`` (``table``, ``list``, ``cards``, ``json``, ``csv``, ``tree``), which
makes ``doto list --format json`` handy for scripting.

Statistics
==========

``doto stats`` prints a breakdown by status, priority, assignee, and tag:

.. code-block:: console

    $ doto stats
    Task Statistics
    ========================================

    Total tasks: 3
      Active: 3

    By Status:
      open            █████████████░░░░░░░   2 ( 66.7%)
      in-progress     ██████░░░░░░░░░░░░░░   1 ( 33.3%)

    By Priority:
      critical        ██████░░░░░░░░░░░░░░   1 ( 33.3%)
      high            ██████░░░░░░░░░░░░░░   1 ( 33.3%)
      low             ██████░░░░░░░░░░░░░░   1 ( 33.3%)

Other commands
==============

The CLI also provides ``show``, ``update``, ``done``, ``reopen``, ``delete``,
``archive``, ``search``, ``next``, ``tree``, ``deps``, ``series``, ``export``,
``git``, and ``config``.  Run ``doto <command> --help`` for the full option list of
any command.
