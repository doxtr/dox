.. index:: Draw.io, Diagrams; Draw.io

Draw.io
=======

To use draw.io diagrams in your documentation, the draw.io extension is required. This extension allows you to include draw.io diagrams directly in your reStructuredText files.

.. important:: If you want to use the draw.io extension with your documentation, you need to make sure, that you have the following settings in your :file:`conf.py` file, as the build may get stuck if you don't have the right settings:

.. code-block:: python

    extensions = [
        ...
        "sphinxcontrib.drawio",
        ...
    ]

    # conf.py

    #################################
    #     Draw.io configuration     #
    #################################

    # See https://pypi.org/project/sphinxcontrib-drawio/
    # Force the extension to strictly run its own background Xvfb setup
    drawio_headless = True
    drawio_no_sandbox = True
    drawio_builder_export_format = {
        "html": "svg",
        "latexpdf": "png",
        "docx": "png"
    }
    drawio_default_export_scale = 100
    drawio_default_transparency = True
    # --- END Draw.io CONFIGURATION ---

To get some privacy, you can start a local draw.io container with the following :command:`podman` command:

.. code-block:: shell

    #> podman run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 docker.io/jgraph/drawio

After running the above command, you can access the draw.io interface by navigating to http://localhost:8080 in your web browser. You can create and edit your diagrams there, and once you're done, you can save them to your local machine. Make sure to save the file using the :menuselection:`Where --> Download` location to store the file, and store it in the .drawio format, as this is required for the next steps.

.. image:: img/save-drawio.png
   :alt: Save draw.io diagram

.. note:: Make sure it's not running inside the VScode container, as this will not work.

Save the draw.io file by downloading and copying it into the documentation tree, under say :download:`example.drawio <img/example.drawio>`. Once that's done, the file can be included with the following command:

.. code-block:: reStructuredText

    .. drawio-image:: example.drawio

Which will render the image like this:

.. drawio-image:: img/example.drawio

There is also a directive for including the draw.io file as a figure, which allows you to add a caption and reference the figure in your documentation:

.. code-block:: reStructuredText

    .. drawio-figure:: example.drawio
       :alt: Example draw.io diagram with figure directive
       :name: example-diagram

       This is an example draw.io diagram with figure directive.

Which will render the image like this:

.. drawio-figure:: img/example.drawio
   :alt: Example draw.io diagram with figure directive
   :name: example-diagram

   This is an example draw.io diagram with figure directive.