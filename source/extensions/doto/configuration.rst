.. _doto-configuration:

Configuration reference
************************

All ``doxtr_doto`` settings live in :file:`conf.py` and are prefixed ``doto_``.  A
representative configuration:

.. code-block:: python
   :caption: conf.py — doxtr_doto configuration

    extensions = [
        # ... other extensions ...
        "doxtr_doto",
    ]

    # Core
    doto_enabled = True
    doto_include_done = True
    doto_render_in_toc = False

    # JSON store and sync
    doto_json_file = ".doto/tasks.json"
    doto_auto_create_json = True
    doto_sync_on_build = True
    doto_conflict_action = "warn"   # error | warn | prefer-rst | prefer-json

    # Defaults and validation
    doto_default_priority = "medium"
    doto_default_status = "open"
    doto_date_format = "%Y-%m-%d"
    doto_id_prefix = ""
    doto_statuses = ["open", "in-progress", "blocked", "done"]
    doto_priorities = ["low", "medium", "high", "critical"]
    doto_required_fields = []       # e.g. ["assignee", "due"]
    doto_warn_overdue = True

    # Auto-archive
    doto_auto_archive = False
    doto_archive_doc = "_doto_archive"
    doto_archive_after_days = 0
    doto_archive_statuses = ["done"]

    # Theming (default | minimal)
    doto_html_theme = "default"
    doto_latex_theme = "default"
    doto_epub_theme = "default"
    doto_html_css_files = []
    doto_latex_preamble = ""

    # Task-list rendering and charts
    doto_list_icon_mode = "icon-text"  # icon | icon-text | text
    doto_chart_engine = "svg"          # svg | plotly (plotly needs the [charts] extra)

    # Integration and export
    doto_export_json = True
    doto_doxtr_integration = "auto"  # auto | enabled | disabled

Options
=======

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Config
     - Default
     - Purpose
   * - ``doto_enabled``
     - ``True``
     - Master enable switch
   * - ``doto_include_done``
     - ``True``
     - Include done tasks in lists/summaries
   * - ``doto_render_in_toc``
     - ``False``
     - Inject tasks into the TOC
   * - ``doto_json_file``
     - ``.doto/tasks.json``
     - Path to the JSON task store
   * - ``doto_auto_create_json``
     - ``True``
     - Create the JSON store if missing
   * - ``doto_auto_archive``
     - ``False``
     - Auto-archive completed tasks
   * - ``doto_archive_doc``
     - ``_doto_archive``
     - Virtual archive document name
   * - ``doto_archive_after_days``
     - ``0``
     - Days after completion before archiving
   * - ``doto_archive_statuses``
     - ``['done']``
     - Statuses eligible for archiving
   * - ``doto_sync_on_build``
     - ``True``
     - Bidirectional RST/JSON sync on build
   * - ``doto_conflict_action``
     - ``error``
     - ``error``, ``warn``, ``prefer-rst``, ``prefer-json``
   * - ``doto_default_priority``
     - ``medium``
     - Default priority for new tasks
   * - ``doto_default_status``
     - ``open``
     - Default status for new tasks
   * - ``doto_date_format``
     - ``%Y-%m-%d``
     - Date display format
   * - ``doto_id_prefix``
     - ``''``
     - Prefix for auto-generated IDs
   * - ``doto_statuses``
     - ``['open','in-progress','blocked','done']``
     - Allowed statuses
   * - ``doto_priorities``
     - ``['low','medium','high','critical']``
     - Allowed priorities
   * - ``doto_required_fields``
     - ``[]``
     - Fields every task must set
   * - ``doto_warn_overdue``
     - ``True``
     - Emit warnings for overdue open tasks
   * - ``doto_html_theme``
     - ``default``
     - HTML theme: ``default`` or ``minimal``
   * - ``doto_latex_theme``
     - ``default``
     - LaTeX theme: ``default`` or ``minimal``
   * - ``doto_epub_theme``
     - ``default``
     - epub theme: ``default`` or ``minimal``
   * - ``doto_html_css_files``
     - ``[]``
     - Extra HTML CSS files
   * - ``doto_latex_preamble``
     - ``''``
     - Extra LaTeX preamble
   * - ``doto_list_icon_mode``
     - ``icon-text``
     - Task-list cell rendering: ``icon``, ``icon-text``, or ``text``
   * - ``doto_chart_engine``
     - ``svg``
     - doto-summary chart engine: ``svg`` or ``plotly``
   * - ``doto_export_json``
     - ``False``
     - Export tasks to ``_static/doto-tasks.json``
   * - ``doto_doxtr_integration``
     - ``auto``
     - ``auto``, ``enabled``, ``disabled``
   * - ``doto_latex_column_specs``
     - ``{}``
     - Per-column LaTeX table column specs
