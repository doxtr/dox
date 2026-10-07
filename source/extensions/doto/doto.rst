****
Doto
****

The ``doxtr_doto`` extension provides documentation task management directly inside
Sphinx.  Tasks are authored with the ``.. doto::`` directive, listed and filtered
with ``.. doto-list::``, summarised (optionally as charts) with ``.. doto-summary::``,
and cross-referenced with the ``:doto:`` role.  Tasks are kept in sync with a JSON
store, so the same tasks can be managed from the command line with the ``doto`` CLI
and from the documentation source.

Every example on the following pages shows the reStructuredText source *and* the
element it renders to, so the page doubles as a live reference.

.. toctree::
   :maxdepth: 2

   getting-started
   tasks
   lists
   summaries
   cross-references
   cli
   configuration
   studies/index
