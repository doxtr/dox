.. index:: Images, Basic Elements; Images

******
Images
******

There are two directives to include images: image and figure. The image directive is used to include an image in the documentation, while the figure directive is used to include an image with a caption. Because of the caption, the figure directive allows the image to show up in the list of figures, which is a page that lists all the figures in the documentation, along with their captions and page numbers. 

Both directives support various options for controlling the appearance and behavior of the included images, such as alignment, scaling, and linking.

Image Directive
===============

This is a simple example of the image directive in Sphinx. The image directive allows you to include an image in your documentation using the following syntax:

.. code-block:: rst

   .. image:: ./img/robo-sphinx.png
      :alt: Robo Sphinx
      :align: right

Which will render as follows:

.. image:: ./img/robo-sphinx.png
   :alt: Robo Sphinx

Figure Directive
================

This is a simple example of the figure directive in Sphinx. The figure directive allows you to include an image with a caption in your documentation using the following syntax:

.. code-block:: rst

   .. figure:: ./img/robo-sphinx-wizard.png
      :alt: Robo Sphinx Enchantment
      :align: right

      This is the caption of the robo sphinx figure.

Which will render as follows:

.. figure:: ./img/robo-sphinx-wizard.png
   :alt: Robo Sphinx Enchantment

   This is the caption of the robo sphinx enchantment figure.

More Examples
=============

You can also include multiple images in a table to display them side by side. For example:

.. list-table::
   :widths: 50 50
   :class: borderless nocolorrows

   * - .. figure:: ./img/doxtr-logo-color-round.png
          :alt: Doxtr Logo Color Round
          :width: 100%
          :align: center

          Colored, round version of the Doxtr logo.

     - .. figure:: ./img/doxtr-logo-line-art-round.png
          :alt: Doxtr Logo Line Art Round
          :width: 100%
          :align: center

          Line art, round version of the Doxtr logo.