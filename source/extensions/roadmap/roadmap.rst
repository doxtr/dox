*******
Roadmap
*******

The ``doxtr_roadmap`` extension provides a ``.. roadmap::`` directive that generates PlantUML Gantt roadmaps directly from CSV data.  Rows are read from an inline CSV body or an external :file:`.csv` file, passed through optional tag and query filters, and emitted as a PlantUML Gantt chart rendered by :xlink:`sphinxcontrib.plantuml <plantuml-home>`.  The extension optionally integrates with ``sphinxcontrib.xlink`` for clickable task links and with the ``doxtr_pdf_theme_core`` palette for consistent colour and typography in PDF output.

PlantUML :xlink:`v1.2026.7 or newer <plantuml-home>` is required.  The extension checks the installed version at build startup and will abort the build (or warn, depending on configuration) if the requirement is not met.

.. toctree::
   :maxdepth: 2

   getting-started
   csv-files
   structure
   views
   figures
   links
   filtering
   styling
   reference
