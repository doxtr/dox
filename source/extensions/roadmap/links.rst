.. _roadmap-links:

Links
*****

The ``link`` column attaches a URL to a task bar.  Two forms are supported:

**Plain URL** — any value that begins with ``https://`` or ``http://`` is used directly as a hyperlink on the task bar.

**xlink role** — a value of the form ``:xlink:\`id\``` is resolved through ``sphinxcontrib.xlink`` (if loaded) to a URL and title drawn from the project's ``.xlink`` files.  The resolved URL and title are emitted as a PlantUML hyperlink.  If ``sphinxcontrib.xlink`` is not loaded, xlink-style cells produce a one-time warning and the link is silently skipped.

The :file:`files/product-roadmap.csv` file used earlier already contains two xlink links: ``API Redesign`` links to :xlink:`plantuml-home` and ``Compliance Review`` links to :xlink:`sphinx-home`.  To show a minimal self-contained inline example:

.. code:: rst

   .. roadmap::
      :title: Projects with Links
      :scale: monthly

      section,name,start,end,row_group,link,tags
      Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,:xlink:`plantuml-home`,eng
      Tools,Sphinx Migration,2027-03-01,2027-04-30,,:xlink:`sphinx-home`,eng code
      Tools,Docs Overhaul,2027-04-01,2027-05-31,,,code

Which will render like this (task bars for ``PlantUML Upgrade`` and ``Sphinx Migration`` are clickable in the HTML output):

.. roadmap::
   :title: Projects with Links
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,:xlink:`plantuml-home`,eng
   Tools,Sphinx Migration,2027-03-01,2027-04-30,,:xlink:`sphinx-home`,eng code
   Tools,Docs Overhaul,2027-04-01,2027-05-31,,,code


Link appendix
-------------

Links embedded inside the PlantUML image are **not clickable in PDF/LaTeX output** — the image is rendered as a static graphic with no active hyperlink areas.  The link appendix feature solves this by rendering the task links as real docutils nodes placed *below* the chart image.

The appendix is **on by default for PDF/LaTeX output** and **off for other builders** (HTML, epub, …), whose image links are already clickable.  You can change the mode, restrict or widen the builders, or disable it entirely — globally in :file:`conf.py` or per-directive for a single chart.

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

**Builder restriction.**  The ``doxtr_roadmap_link_appendix_builders`` list is checked against both ``builder.name`` (e.g. ``"latex"``, ``"html"``) and ``builder.format`` (e.g. ``"latex"``, ``"html"``).  Use the special value ``"all"`` (or a list containing ``"*"``) to render the appendix for every builder::

    doxtr_roadmap_link_appendix_builders = "all"

This means the same RST source builds an image-only HTML page and an image-plus-appendix PDF page — no per-format conditionals needed.

**Mode: ``"list"`` vs ``"footnote"``.**

- ``"list"`` — a ``nodes.bullet_list``; each item is ``<Task Name>: <clickable URL or title>``.  Always rendered as a standalone block below the chart, regardless of whether the roadmap is wrapped in a figure.
- ``"footnote"`` — real reStructuredText auto-numbered footnotes.  In PDF/LaTeX output Sphinx's LaTeX writer renders these as page-bottom ``\footnote{}`` commands.  In HTML they render as standard numbered footnotes with back-references.

  **When the roadmap is a figure** (via ``:caption:``, ``:align:``, or ``doxtr_roadmap_figure = True``) and the builder is in ``link_appendix_builders``, footnote mode embeds the links compactly **inside the figure caption** instead of a separate "Links" block.  The caption shows a single label word (the ``link_appendix_title``, default ``"Links"``) followed by one auto-numbered footnote marker per link:

  .. code-block:: text

     Projects with Links (Links [1], [2])

  With ``numfig = True`` this renders as e.g. *Fig. 13.19: Projects with Links (Links\ :sup:`9`\ ,\ :sup:`10`\)*.

  Each footnote body carries the task name, the link title (when available via xlink resolution), and the URL:

  .. code-block:: text

     [1] API Redesign: https://example.com/api
     [2] Sphinx Migration >> Sphinx Docs: https://www.sphinx-doc.org

  Form with a plain URL (no resolved title): ``<Task Name>: <url>``.  Form with a resolved title (xlink): ``<Task Name> >> <Title>: <url>``.

  The footnote definitions follow as sibling nodes after the figure.  No separate "Links" rubric or container is emitted.  If there are no resolvable links the caption is the plain title with no brackets.

  Without a figure, ``"footnote"`` still produces the standalone footnote appendix below the chart (unchanged behaviour).

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

Which will render like this (the chart image is always shown; the link appendix appears below it in PDF/LaTeX output where ``doxtr_roadmap_link_appendix_builders = ["latex"]`` matches the builder):

.. roadmap::
   :title: Projects with Links
   :link-appendix: list
   :link-appendix-title: Task links
   :scale: monthly

   section,name,start,end,row_group,link,tags
   Tools,PlantUML Upgrade,2027-02-01,2027-03-31,,https://plantuml.com,eng
   Tools,Sphinx Migration,2027-03-01,2027-04-30,,https://www.sphinx-doc.org,
   Tools,Internal Task,2027-04-01,2027-05-31,,,ops

The same chart with ``footnote`` mode produces real page-bottom footnotes in PDF and numbered footnotes in HTML instead of a bullet list:

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
