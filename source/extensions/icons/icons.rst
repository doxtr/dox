*****
Icons
*****

sphinx-icon is a Sphinx extention to allow developers to use the icon role to display inlined icons. The extention currently supports only Fontawsome 6.3.0 icons.

Configuration
-------------

To use the :code:`sphinx-icon` extension, you need to add it to the list of extensions in your :file:`conf.py` file:

.. code-block:: python
   :caption: conf.py options for sphinx-icon

    extensions = [
        ...
        "sphinxcontrib.icon",
        ...
    ]

Icon Role
---------

The :code:`sphinxcontrib.icon` extension provides the :code:`icon` role, which allows you to include icons in your documentation. You can use the role like this:

.. code-block:: rst

   - I'm an :icon:`fa-solid fa-folder` icon.
   - I'm an :icon:`fa-regular fa-user` icon.
   - I'm an :icon:`fa-brands fa-500px` icon.

- I'm an :icon:`fa-solid fa-folder` icon.
- I'm an :icon:`fa-regular fa-user` icon.
- I'm an :icon:`fa-brands fa-500px` icon.