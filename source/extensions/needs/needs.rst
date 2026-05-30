************
sphinx-needs
************

Sphinx-needs is an extension for Sphinx that allows you to model requirements, specifications, and other needs in your documentation. It provides a set of directives and roles that you can use to create and manage your needs, and it also provides a set of templates that you can use to display your needs in different ways.

Configuration
=============

To use the :code:`sphinx-needs` extension, you need to add it to the list of extensions in your :file:`conf.py` file:

.. code-block:: python
   :caption: conf.py options for sphinx-needs

    extensions = [
        ...
        "sphinxcontrib.needs",
        ...
    ]

You can also configure the extension by adding some settings to your :file:`conf.py` file. For example, you can configure the default type of need that is created when you use the :code:`.. need::` directive:

Here is a basic configuration that you can use as a starting point:

.. code-block:: python
   :caption: conf.py options for sphinx-needs

   ######################################
   #     sphinx-needs configuration     #
   ######################################

   needs_build_json = True
   needs_types = [
      {
         "directive": "dr",
         "title": "Decision Record",
         "prefix": "_DR",  # prefix for auto-generated IDs
         "style": "rectangle", # style for the type in diagrams
         "color": "#BFD8D2", # color for the type in diagrams
      }
   ]
   needs_id_regex = r'^[a-zA-Z0-9_-]+$'  # IDs can only contain letters, numbers, underscores, and hyphens

   # Available from sphinx-needs 7.0.0
   needs_fields = {
      "xlink": {
         "description": "Documentation link",
         "schema": {
               "type": "string",
         },
         "nullable": True
      },
      "documentation": {
         "description": "Documentation link",
         "schema": {
               "type": "string",
         },
         "nullable": True
      },
      "python-docs": {
         "description": "Python documentation link",
         "schema": {
               "type": "string",
         },
         "nullable": True
      }
   }

   # This is a custom setting that integrates with the xlink extension, and allows you to specify which xlink fields should be processed by the xlink extension. This is necessary because the xlink extension needs to know which fields contain xlink references, so it can process them correctly.
   xlink_needs_string_link_options = [ 'xlink', 'documentation']

Usage
=====

You can model requirements, specifications, and other needs in your documentation using the :code:`sphinx-needs` extension.

A need can e.g. be a decision record, a requirement, a specification, or any other type of need that you want to document. You can create a need using the :code:`.. need::` directive, and you can specify the type of need using the :code:`:type:` option. For example, if you want to create a decision record, you can use the following directive:

.. dr:: My decision
   :id: DR-0001
   :xlink: [[ xlink('drawio-github-releases') ]]; [[ xlink('drawio-home') ]]

   This is a decision that I have made, and I want to document it in my documentation. I can use the :code:`.. dr::` directive to create a decision, and then I can reference it throughout my documentation.

   :xlink:`drawio-github-releases`

Many different options are available for needs, and you can also create your own custom fields. For example, you can create a custom field called :code:`documentation`, which can be used to link to documentation related to the need. You can then use this field in your needs, and it will be processed by the xlink extension, so you can use it to create links to your documentation. For example:

.. dr:: My second decision
   :id: DR-0002
   :documentation: [[ xlink('drawio-github-releases, drawio-home') ]]

   This is a decision that I have made, and I want to document it in my documentation. I can use the :code:`.. dr::` directive to create a decision, and then I can reference it throughout my documentation.

   :xlink:`drawio-home`

If you try to use a field that is not configured as a xlink field, you will get an error. For example, if you try to use the :code:`python-docs` field as a xlink field, you will get an error, because it is not configured as a xlink field in the :code:`xlink_needs_string_link_options` setting. For example:

.. dr:: My third decision
   :id: DR-0003
   :python-docs: [[ xlink('python-docs') ]]; [[ xlink('drawio-github-releases, drawio-home') ]]

   .. note:: This must fail, as 'python-docs' is not configured as a xlink field.

   :xlink:`python-docs`

