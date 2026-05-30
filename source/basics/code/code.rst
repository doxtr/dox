.. index:: Code, Basic Elements; Code

************
Showing Code
************

This chapter shows the different ways to include simple text, program or e.g. shell code in your documentation, and how it looks like when rendered.

The code-block directive
========================

To properly display code in your documentation, use the ``code-block`` directive. This allows you to specify the language of the code, which enables syntax highlighting and makes it easier for readers to understand the code.

On top of that, you can also specify a caption for the code block, which will be displayed above the code block. This is useful for generating a list of listings page, providing context or explaining what the code does.

Showing bash code
-----------------

You can use the ``code-block`` directive to show bash code in your documentation. For example, you can show how to install a theme and build the PDF using the following code block:

.. code-block:: rst
   :caption: Install the doxtr theme and build the PDF
   
   .. code-block:: bash
      :caption: Install the doxtr theme and build the PDF
      :name: install-theme-anchor

      pip install --no-cache-dir --upgrade "docdash-pdf-theme-core @ git+https://github.com/authsec/docdash-pdf-theme-core-dev" && \
      make clean latexpdf

      # fix this in the theme to have a good fallback
      docdash_section_number_color = "#55FFF4"

.. code-block:: bash
   :caption: Install the doxtr theme and build the PDF
   :name: install-theme-anchor

   pip install --no-cache-dir --upgrade "docdash-pdf-theme-core @ git+https://github.com/authsec/docdash-pdf-theme-core-dev" && \
   make clean latexpdf

   # fix this in the theme to have a good fallback
   docdash_section_number_color = "#55FFF4"

Showing Plain Text
------------------

.. code-block:: text
   :caption: Showcase: Plain text code block

   This is a plain text code block. It will be rendered as a block of text with no syntax highlighting.

Showing Python Code
-------------------

.. code-block:: python
   :caption: Showcase: Hello World in Python

   def hello_world():
       print("Hello, world!")

This will render the code block with syntax highlighting for Python. You can also specify the language for syntax highlighting, such as ``.. code-block:: javascript`` for JavaScript code.

Showing Java Code
-----------------

.. code:-block:: java
   :caption: Showcase: Hello World in Java

   .. code-block:: java
      :caption: Showcase: Hello World in Java

      public class HelloWorld {
         public static void main(String[] args) {
            System.out.println("Hello, world!");
         }
      }

This will render like this:

.. code-block:: java
   :caption: Showcase: Hello World in Java

   public class HelloWorld {
       public static void main(String[] args) {
           System.out.println("Hello, world!");
       }
   }



The code directive
==================

You can simply use the ``code`` directive to include code in your documentation too. This is however only recommended for use, if you're sure, that the code you're showing must not be included in the list of listings and does not have a proper caption. This is because the ``code`` directive does not allow you to specify a caption for the code block, and it will not be included in the list of listings.


