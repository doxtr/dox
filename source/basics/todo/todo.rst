.. index:: TODO, Basic Elements; TODO

****
TODO
****

Sometimes you may want to include a TODO list in your documentation. Sphinx provides a simple way to create TODO lists using the ``todo`` directive. Here are some examples of how to create TODO lists in Sphinx.

.. code-block:: rst

  .. todo:: This is a simple TODO item.

Which will render like this:

.. todo:: This is a simple TODO item.

Your documentation may contain multiple TODO items, which you can later collect into a list using the ``todolist`` directive. The ``todolist`` directive will generate a list of all TODO items in your documentation.

But for the list to be generated, you need more than one TODO item.

.. todo:: This is another TODO item, that helps us build a list of TODO items.

Then you continue with your documentation until you hit the moment, when you need to generate another todo item.

.. todo:: This is yet another TODO item, that helps us build a list of TODO items.

You can also create a list of TODO items using the ``todolist`` directive. This directive will generate a list of all TODO items in your documentation.

.. code-block:: rst

   .. todolist::

Which will render like this:

.. todolist::


