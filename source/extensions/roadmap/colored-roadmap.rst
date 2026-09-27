Colored roadmap with completion levels
======================================

This example shows several tasks in different colors, each partially
completed, so the relationship between the *done* (completed) portion and the
*undone* (remaining) portion of every bar can be inspected visually.

* Colors come from the CSV ``color`` column — a mix of semantic theme-core
  expressions (``dd:primary``, ``dd:secondary``) and hex colors.
* The *undone* portion of every bar is derived automatically from the *done*
  color: it is ``doxtr_roadmap_bar["undone_brightness_delta"]`` percent
  lighter in light mode and that much darker in dark mode.  (PlantUML gantt
  supports only one global undone color, so it is derived from the global
  ``done_color`` and shared by all bars.)
* Start / end dates are written relative to ``@now()`` so every bar always
  straddles the build date and renders with a visible completion level,
  regardless of when the documentation is built.
* The directive uses ``:start: now() - 12 weeks`` so the diagram window
  reaches into the past far enough to actually *show* the completed
  ("done") portion of each bar.  Without it the diagram would start at
  ``now()`` and every bar would be clamped to today, hiding the done part.
  (Note: ``:start:`` / ``:end:`` take a bare period expression — no ``@``
  prefix; the ``@`` prefix is only used inside CSV ``start`` / ``end`` cells.)
* ``GA readiness`` uses ``color=default`` to fall back to the roadmap default
  color, and ``Milestone GA`` is a milestone (start == end).

.. roadmap::
   :file: files/colored-roadmap.csv
   :title: Colored roadmap with completion levels
   :start: now() - 12 weeks
