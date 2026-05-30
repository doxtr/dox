.. index:: Container, Basic Elements; Container

Container
=========

Sphinx supports additional body elements called "container". These are special blocks that can be used to group content together and apply specific formatting or styling to that content. Containers can be used to create custom blocks of content, such as notes, warnings, or other types of information that you want to highlight in your documentation.

The built-in containers include:

- `rubric`, which is used to create a heading for a section of content. It is typically rendered in a larger font size and bolded to make it stand out from the rest of the text.
- `topic`, which is used to create a block of content that is related to a specific topic. It is typically rendered with a different background color or border to make it stand out from the rest of the text.
- `container`, which is a generic container that can be used to group content together. It does not have any specific styling or formatting, but can be used to apply custom styles using CSS.

Rubric
------

.. code-block:: rst
   :caption: Rubric Example
   
   .. rubric:: This is a rubric

This is a rubric, which is a sectioning element that is used to group together related sections. It is not a sectioning level, but rather a way to organize the documentation.

.. rubric:: This is a rubric

Topic
-----

This is a topic, which is a block of content that is related to a specific topic. It is typically rendered with a different background color or border to make it stand out from the rest of the text.

.. code-block:: rst
   :caption: Topic Example

   .. topic:: This is a topic

      This is the content of the topic ...

.. topic:: This is a topic

   This is the content of the topic. You can include any content you want here, and it will be rendered in a block with the title "This is a topic". You can also specify specific styling of the topic by using the ``:class:`` option, like this:

   .. code-block:: rst

      .. topic:: This is a topic
         :class: custom-topic

Container
---------

This is a container, which is a generic container that can be used to group content together. It does not have any specific styling or formatting, but can be used to apply custom styles using CSS.

.. code-block:: rst
   :caption: Container Example

   .. container::
      :name: Link Anchor Name

      This is the content of the container. You can include any content you want here, and it will be rendered in a block. With the ``name`` option, you can create a link anchor for the container (This allows you to link to the container from other parts of your documentation by appending the anchor name like `#link-anchor-name`). You can also specify specific styling of the container by adding a class to the container, like this:

         .. container:: container-class

            This is the content of the container with a custom class. You can use this to apply custom styles to the container using CSS.

.. container::
   :name: Link Anchor Name

   This is the content of the container. You can include any content you want here, and it will be rendered in a block. With the ``name`` option, you can create a link anchor for the container (This allows you to link to the container from other parts of your documentation by appending the anchor name like `#link-anchor-name`). You can also specify specific styling of the container by adding a class to the container, like this:

      .. container:: container-class

         This is the content of the container with a custom class. You can use this to apply custom styles to the container using CSS.

Containers can also be nested within each other, allowing you to create complex blocks of content that are organized and easy to read. For example, you can have a topic that contains a container, which in turn contains another topic. This allows you to provide detailed information and guidance to the reader in a structured way.

Typewriter Container
^^^^^^^^^^^^^^^^^^^^

You can also create a typewriter container, which is a special type of container that is used to display content in a typewriter font. This can be useful for displaying code snippets or other types of content that you want to stand out from the rest of the text.

You can create a typewriter container by using the ``:class:`` option with the value ``typewriter``, like this:

.. code-block:: rst
   :caption: Typewriter Container Example

   .. container:: typewriter

      This is the content of the typewriter container. It will be rendered in a typewriter font, which can be useful for displaying code snippets or other types of content that you want to stand out from the rest of the text.

.. container:: typewriter

   This is the content of the typewriter container. It will be rendered in a typewriter font, which can be useful for displaying code snippets or other types of content that you want to stand out from the rest of the text.