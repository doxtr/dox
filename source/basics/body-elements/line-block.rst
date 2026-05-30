.. index:: Line Block, Basic Elements; Line Block

Line Block
==========

Sphinx also supports a special type of container called a "line block". A line block is a block of content that is used to display lines of text that are not wrapped, such as poetry or code snippets. Line blocks can be created using the ``line-block`` directive, and each line of text within the block is treated as a separate line. For example:

.. code-block:: rst
   :caption: Line Block Example

   | This is the first line of the line block.
   | This is the second line of the line block.
   | This is the third line of the line block.

| This is the first line of the line block.
| This is the second line of the line block.
| This is the third line of the line block.

