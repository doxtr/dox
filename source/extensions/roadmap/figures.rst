Figures and captions
********************

Adding a ``:caption:`` to a ``.. roadmap::`` directive wraps the chart in a docutils ``figure`` node.  Sphinx then numbers the figure (``Fig. 1``, ``Fig. 2``, …) and includes it in the List of Figures.  Users can cross-reference the figure by name.

Enable ``numfig = True`` in :file:`conf.py` to activate "Figure N" numbering and ``:numref:`` cross-references:

.. code-block:: python
   :caption: conf.py — enable figure numbering

    numfig = True

Then add ``:caption:`` (and optionally ``:name:`` and ``:align:``) to any ``.. roadmap::`` directive:

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

Set ``doxtr_roadmap_figure = True`` in :file:`conf.py` to wrap **every** ``.. roadmap::`` as a figure automatically, without adding ``:caption:`` to each directive.  The chart's ``:title:`` (or ``doxtr_roadmap_default_title``) is used as the caption by default:

.. code-block:: python
   :caption: conf.py — global figure wrapping

    doxtr_roadmap_figure = True
    # Optional: set a fixed caption for all auto-wrapped figures.
    # None (default) → use each chart's :title: as the caption.
    doxtr_roadmap_figure_caption = None

When ``doxtr_roadmap_figure_caption`` is set to a non-empty string, that string is used verbatim as the caption for any roadmap that does not carry its own per-directive ``:caption:``.

**Caption precedence** (from highest to lowest):

1. Explicit ``:caption:`` option — used verbatim.
2. ``doxtr_roadmap_figure_caption`` if non-empty — global override.
3. The chart ``:title:`` (or ``doxtr_roadmap_default_title``) — default.

An ``:align:``-only wrap (no explicit ``:caption:``) also gets the chart title as its caption by default, so the roadmap appears in the List of Figures without any extra configuration.

.. note::

   The LaTeX/PDF builder emits ``\begin{figure}…\caption{…}\end{figure}`` for every captioned roadmap.  These entries feed into ``\listoffigures`` automatically when your LaTeX preamble includes it.  If ``doxtr_pdf_theme_core`` is in use, its ``show_list_of_figures`` global controls whether ``\listoffigures`` is printed.
