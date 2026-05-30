.. index:: Sidebar, Basic Elements; Sidebar

Sidebar
=======

Sphinx also supports a special type of container called a "sidebar". A sidebar is a block of content that is typically displayed on the side of the page, and can be used to provide additional information or navigation options to the reader. Sidebars can be created using the ``sidebar`` directive, and can include any content that you want to include in the sidebar.

.. code-block:: rst
   :caption: Sidebar Example

   .. sidebar:: Optional Sidebar Title
      :subtitle: Optional Sidebar Subtitle

      Subsequent indented lines comprise
      the body of the sidebar, and are
      interpreted as body elements.

The sidebar will be rendered on the side of the page, and will include the title and subtitle (if provided), as well as the content of the sidebar. You can include any body elements in the sidebar, such as paragraphs, lists, images, etc., and they will be rendered within the sidebar.

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

Sidebars are a great way to provide additional context or information to the reader without cluttering the main content of the page. They can be used for things like related links, notes, warnings, or any other type of information that you want to highlight in a separate section of the page.