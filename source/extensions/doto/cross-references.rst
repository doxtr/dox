.. _doto-cross-references:

Cross-referencing tasks
***********************

The ``:doto:`` role links to a task by its ID.  The link resolves to wherever the
task is defined, regardless of which document the reference appears in.

Basic reference
===============

.. code:: rst

   See :doto:`AUTH-001` for the authentication work.

Which will render like this:

See :doto:`AUTH-001` for the authentication work.

Custom link text
================

Put the display text before the ID in angle brackets.

.. code:: rst

   See :doto:`the auth hardening work <AUTH-001>` and
   :doto:`the outage remediation <TASK-CRIT>`.

Which will render like this:

See :doto:`the auth hardening work <AUTH-001>` and
:doto:`the outage remediation <TASK-CRIT>`.

.. note::

   In PDF/LaTeX output these cross-references are **clickable hyperlinks** that jump
   directly to the task box, not just styled text.
