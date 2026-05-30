.. index:: Lists, Basic Elements; Lists

*****
Lists
*****

RestructuredText supports lists, both ordered and unordered.  The syntax is simple and straightforward, making it easy to create lists in your documentation.

Unordered Lists
===============

.. code-block:: rst
   :caption: Unordered list example

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

Ordered Lists
=============

You can create ordered lists using numbers followed by a period. The syntax is as follows:

.. code-block:: rst
   :caption: Ordered list example

   1. This is a numbered list.
   2. It also has two items, 
      the second item uses two lines.

1. This is a numbered list.
2. It also has two items, 
   the second item uses two lines.

You can also use # instead of numbers for ordered lists, which will automatically number the items for you. For example:

.. code-block:: rst
   :caption: Ordered list with automatic numbering

   #. This is a numbered list with automatic numbering.
   #. It also has two items, 
      the second item uses two lines.

#. This is a numbered list with automatic numbering.
#. It also has two items, 
   the second item uses two lines.

You can also use letters or Roman numerals for ordered lists. For example:

.. code-block:: rst
   :caption: Ordered list with letters

   a. This is a numbered list with letters.
   b. It also has two items, 
      the second item uses two lines.

a. This is a numbered list with letters.
b. It also has two items, 
   the second item uses two lines.

Nested Lists
============

Nested lists are possible, but be aware that they must be separated from the parent list items by blank lines: For example:

.. code-block:: rst
   :caption: Nested list example

   * This is a bulleted list.

      * This is a nested bulleted list.
      * This is another item in the nested bulleted list.

      a. This is a numbered list
      b. This is another entry in the numbered list.

         i. This is a nested numbered list.
         ii. This is another entry in the nested numbered list.

         #. This is a nested numbered list with automatic numbering.
         #. This is another entry in the nested numbered list with automatic numbering.

      #. Continue the numbered letter list.

   * This is another item in the bulleted list.
   * This is yet another item in the bulleted list.

* This is a bulleted list.

   * This is a nested bulleted list.
   * This is another item in the nested bulleted list.

   a. This is a numbered list
   b. This is another entry in the numbered list.

      i. This is a nested numbered list.
      ii. This is another entry in the nested numbered list.

      #. This is a nested numbered list with automatic numbering.
      #. This is another entry in the nested numbered list with automatic numbering.

   #. Continue the numbered letter list.

* This is another item in the bulleted list.
* This is yet another item in the bulleted list.



Definition Lists
================

Definition lists are used to define terms and their corresponding definitions. The syntax for definition lists is as follows:

.. code-block:: rst
   :caption: Definition list example

   Term 1
     Definition of term 1.

   Term 2
     Definition of term 2.

Term 1
  Definition of term 1.

Term 2
   Definition of term 2.

You can also have multiple definitions for a single term, like this:

.. code-block:: rst
   :caption: Definition list with multiple definitions

   Term 1
      Definition of term 1.
      
      Sub-term 1.1
         Definition of sub-term 1.1.

   Term 2
      Definition of term 2.
      
      Another definition of term 2.

Term 1
   Definition of term 1.
   
   Sub-term 1.1
      Definition of sub-term 1.1.

Term 2
   Definition of term 2.
   
   Another definition of term 2.