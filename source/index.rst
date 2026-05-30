.. Doxamples documentation master file, created by
   sphinx-quickstart on Tue May 19 20:56:41 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections

   Sectioning syntax:
   ==================

   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

   all characters for sectioning syntax must be the same and must be repeated as many times as the length of the section title

Doxamples
=========

This document is a test document, to show off all the features of Sphinx and reStructuredText together with the doxtr container runtime. Build it with:: 

   make latexpdf && ls /workspaces/docs/build/latex/*.pdf

It showcases how certain elements of the documentation can be used, and how they look like when rendered.

For a real piece of documentation, this can be a good place for a foreword to the documentation, or an introduction to the documentation, or a general overview of the documentation.

It is not meant to be read like a book, but to be used as a template for your own documentation or a reference for how to use certain features of Sphinx and reStructuredText. Some examples may be specific to the doxtr container runtime, but most of the features shown here are general features of Sphinx and reStructuredText that can be used in any documentation.

.. toctree::
   :hidden:
   :maxdepth: 5

   basics/basics
   extensions/extensions


.. release new xlink version
.. .. only:: html

..    .. xlink-search::
..       :title: Doxtr Bookmark Search
..       :results: 1, 5, 10, 25, 50, 100
..       :overlay: