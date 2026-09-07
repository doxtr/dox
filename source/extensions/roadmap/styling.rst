Styling and theming
*******************

Styling
=======

All styling is controlled by ``doxtr_roadmap_*`` config values in :file:`conf.py`.  Directive-level overrides (such as ``:clean-style:``) take precedence over the global config.

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

``doxtr_roadmap_clean_style = True`` (the default) instructs PlantUML to hide the per-task **Start**, **End**, and **Duration** columns from the Gantt table.  This keeps the diagram tidy and is essential when ``row_group`` grouping is active, as the date stamps from multiple tasks sharing a row would otherwise overlap.

``clean_style`` defaults to ``True`` because PlantUML v1.2026.7 — the extension's minimum baseline — fully supports the ``hide column start/end/duration`` syntax.  To disable it globally:

.. code-block:: python
   :caption: conf.py

    doxtr_roadmap_clean_style = False

The ``:clean-style:`` directive option overrides the global setting for a single directive instance:

.. code:: rst

   .. roadmap::        ← bare flag or explicit true enables clean_style
      :clean-style:
      :file: roadmap.csv

   .. roadmap::        ← explicit false disables clean_style for this block
      :clean-style: false
      :file: roadmap.csv


Theme integration
=================

When ``doxtr_pdf_theme_core`` is present in ``extensions``, ``doxtr_roadmap`` automatically reads its semantic palette and typography globals to colour the roadmap consistently with the rest of the PDF output.  User-configured ``doxtr_roadmap_*`` values always take precedence over theme-core values.

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
