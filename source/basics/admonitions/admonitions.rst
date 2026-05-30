.. index:: Admonitions, Basic Elements; Admonitions

***********
Admonitions
***********

Sphinx supports a number of built-in admonitions, which are special blocks that can be used to highlight important information, warnings, notes, and other types of content. These admonitions are rendered with different styles to make them stand out from the rest of the text.

The built-in admonitions include:

.. rubric:: Attention

.. code-block:: rst

   .. attention:: This is an attention admonition. It is used to highlight information that requires special attention from the reader.

.. attention:: This is an attention admonition. It is used to highlight information that requires special attention from the reader.

.. rubric:: Caution

.. code-block:: rst

   .. caution:: This is a caution admonition. It is used to highlight information that could potentially cause harm or danger if not followed.

.. caution:: This is a caution admonition. It is used to highlight information that could potentially cause harm or danger if not followed.

.. rubric:: Danger

.. code-block:: rst

   .. danger:: This is a danger admonition. It is used to highlight information that could potentially cause serious harm or danger if not followed.

.. danger:: This is a danger admonition. It is used to highlight information that could potentially cause serious harm or danger if not followed.

.. rubric:: Error

.. code-block:: rst

   .. error:: This is an error admonition. It is used to highlight information that indicates an error has occurred.

.. error:: This is an error admonition. It is used to highlight information that indicates an error has occurred.

.. rubric:: Hint

.. code-block:: rst

   .. hint:: This is a hint admonition. It is used to provide helpful hints or suggestions to the reader.

.. hint:: This is a hint admonition. It is used to provide helpful hints or suggestions to the reader.

.. rubric:: Important

.. code-block:: rst

   .. important:: This is an important admonition. It is used to highlight information that is crucial for the reader to understand or follow.

.. important:: This is an important admonition. It is used to highlight information that is crucial for the reader to understand or follow.

.. rubric:: Note

.. code-block:: rst

   .. note:: This is a note admonition. It is used to highlight important information that the reader should pay attention to.

.. note:: This is a note admonition. It is used to highlight important information that the reader should pay attention to.

.. rubric:: See Also

.. code-block:: rst

   .. seealso:: This is a see also admonition. It is used to provide references to related information or resources.

.. seealso:: This is a see also admonition. It is used to provide references to related information or resources.

.. rubric:: Tip

.. code-block:: rst

   .. tip:: This is a tip admonition. It is used to provide helpful hints or suggestions to the reader.

.. tip:: This is a tip admonition. It is used to provide helpful hints or suggestions to the reader.

.. rubric:: Warning

.. code-block:: rst

   .. warning:: This is a warning admonition. It is used to highlight information that could potentially cause problems or issues if not followed.

.. warning:: This is a warning admonition. It is used to highlight information that could potentially cause problems or issues if not followed.

You can also create custom admonitions using the ``admonition`` directive, which allows you to specify the title and content of the admonition. This can be useful for creating custom blocks of content that do not fit into the built-in categories.

.. rubric:: Custom Admonition

.. code-block:: rst

   .. admonition:: This is a custom admonition

      This is the content of the custom admonition. You can include any content you want here, and it will be rendered in a block with the title "This is a custom admonition". You can also specify the title of the admonition by using the ``:class:`` option, like this:

.. admonition:: This is a custom admonition

   This is the content of the custom admonition. You can include any content you want here, and it will be rendered in a block with the title "This is a custom admonition". You can also specify the title of the admonition by using the ``:class:`` option, like this:

Admonition Nesting
==================

Admonitions can also be nested within each other, allowing you to create complex blocks of content that are organized and easy to read. For example, you can have a warning admonition that contains a note admonition, which in turn contains a tip admonition. This allows you to provide detailed information and guidance to the reader in a structured way.

.. warning:: This is a warning admonition

   This is the content of the warning admonition. It contains a note admonition and a custom nested admonition, which provides additional information about the warning.

   .. note:: This is a note admonition

      This is the content of the note admonition. It contains a tip admonition, which provides helpful hints related to the note.

      .. tip:: This is a tip admonition

         This is the content of the tip admonition. It provides helpful hints related to the note and the warning.

   We can also include a custom nested admonition within the warning admonition, which provides additional information related to the warning. This allows us to provide more detailed information and guidance to the reader, while still keeping the content organized and easy to read.

   .. admonition:: This is a custom nested admonition

      This is the content of the custom admonition. It is nested within the warning admonition, and provides additional information related to the warning.