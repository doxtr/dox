.. index:: Sectioning, Basic Elements; Sectioning

**********
Sectioning
**********

The ``*`` overline and underline represents the 'Chapter' level of the documentation, as ``latex_toplevel_sectioning = "part"`` is set in the configuration (``conf.py``). It contains examples of all the different sectioning levels, and how they look like when rendered.

The 'chapter' heading is created with::

   **********
   Sectioning
   **********

Sectioning hierarchy conventions
================================

Section headers in the documentation follow a specific hierarchy, which is determined by the characters used for the overline and underline of the section headers. 

The 'section' heading is created with::

   Sectioning hierarchy conventions
   ================================

Sectioning syntax
=================

If you design the document structure according to the sectioning hierarchy, you can use the following syntax for the section headers. This makes it easier to maintain a consistent structure throughout the documentation, and also allows for better organization and navigation for the readers.

- `#` with overline, for parts
- `*` with overline, for chapters
- `=`, for sections
- `-`, for subsections
- `^`, for subsubsections
- `"`, for paragraphs
- `~`, for subparagraphs

The sectioning levels can be nested within each other, and the hierarchy will be maintained. For example, you can have a section that contains subsections, which in turn contain subsubsections, and so on. This allows for a clear and organized structure for the documentation, making it easier for readers to navigate and find the information they are looking for.

A simple section
================

This formatting represents the 'Section' level of the documentation. It is the most commonly used sectioning level, and is used for most of the sections in the documentation.

And this is a simple second paragraph.

A sub-section
-------------

This formatting represents the 'Sub-section' level of the documentation. It is used for sections that are nested within a section.

The 'sub-section' heading is created with::

   A sub-section
   -------------

A sub-sub-section
^^^^^^^^^^^^^^^^^

This formatting represents the 'Sub-sub-section' level of the documentation. It is used for sections that are nested within a sub-section.

The 'sub-sub-section' heading is created with::

   A sub-sub-section
   ^^^^^^^^^^^^^^^^^

A paragraph
"""""""""""

This formatting represents the 'Paragraph' level of the documentation. It is used for sections that are nested within a sub-sub-section, and is the lowest level of sectioning in the documentation.

The 'paragraph' heading is created with::

   A paragraph
   """""""""""

.. rubric:: This is called a rubric

This is a rubric, which is a sectioning element that is used to group together related sections. It is not a sectioning level, but rather a way to organize the documentation.

The 'rubric' heading is created with::

   .. rubric:: This is called a rubric

Another simple section
======================

This is another simple section, to show how the sectioning levels look like when rendered.

You can also use the sectioning levels to create a table of contents, which is a list of all the sections in the documentation, and their corresponding page numbers. This can be done using the ``toctree`` directive, which is used to create a table of contents for the documentation.

A section can also span multiple pages, and the sectioning levels will be maintained across the pages. This means that if you have a section that starts on one page, and continues on another page, the sectioning levels will be maintained, and the section will still be considered a section, even if it spans multiple pages.

Depending on the PDF theme you are using, the sectioning levels may be displayed differently in the table of contents, and in the headers of the pages. For example, some themes may display the sectioning levels in different colors, or with different fonts, to make it easier to distinguish between the different levels of sectioning.

This is however highly dependent on the PDF theme you are using, and may not be the case for all themes. It is recommended to check the documentation of the PDF theme you are using, to see how it handles sectioning levels in the table of contents and in the headers of the pages.

You can also reference the sections like |xlink-ref-a-sub-sub-section| fairly easily in the document using the generated Visual Studio Code commands.

.. toctree::
   :hidden:

   reset-showcase/reset-showcase