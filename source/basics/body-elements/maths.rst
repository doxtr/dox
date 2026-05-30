.. index:: Basic Elements; Body Elements, Maths

Maths
=====

This is an example of a math block in Sphinx. The math block allows you to include mathematical equations and expressions in your documentation using LaTeX syntax.

.. code-block:: rst

   .. math::

      (a + b)^2 = a^2 + 2ab + b^2

      (a - b)^2 = a^2 - 2ab + b^2

It will render as follows:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

You can also include inline math expressions using the :math: role, like this ``:math:`E = mc^2```, which will render as: :math:`E = mc^2` inline with the text.

