.. index:: Epigraph, Basic Elements; Epigraph

Epigraph
========

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

This is an epigraph, which is a block of text that is used to provide a quote or a saying that is relevant to the content of the documentation. It is typically rendered in a different style than the rest of the text, such as italicized or indented, to make it stand out from the rest of the content.

.. code-block:: rst

   .. epigraph::

      No matter where you go, there you are.

      -- Buckaroo Banzai

.. pull-quote:: This is a pull quote

   This is the content of the pull quote. You can include any content you want here, and it will be rendered in a block with the title "This is a pull quote". You can also specify specific styling of the pull quote by using the ``:class:`` option, like this:

   .. code-block:: rst

      .. pull-quote:: This is a pull quote
         :class: custom-pull-quote

.. highlights:: This is a highlights block, which is used to highlight specific text or phrases in the documentation. It is typically rendered with a different background color or border to make it stand out from the rest of the text. You can also specify specific styling of the highlights block by using the ``:class:`` option, like this:

   .. code-block:: rst

      .. highlights:: This is a highlights block
         :class: custom-highlights