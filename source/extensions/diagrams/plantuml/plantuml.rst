********
PlantUML
********

This extension allows you to include PlantUML diagrams in your documentation. It uses a local PlantUML instance to generate the diagrams, so you can be sure, the information stays local and is not sent to any third party service. It also allows you to include the PlantUML source code in your documentation, so you can easily edit the diagrams without having to go back to the source code.

You can find more information about PlantUML :xlink:`here <plantuml-home>`

Configuration
=============

Make sure to add :code:`sphinxcontrib.plantuml` to the list of extensions in your :file:`conf.py` file:

.. code-block:: python
   :caption: conf.py options for sphinxcontrib-plantuml

    extensions = [
        ...
        "sphinxcontrib.plantuml",
        ...
    ]

You also need to specify the path to the PlantUML jar file in your :file:`conf.py` file, if you've set it up in a location other than the default (or accessible via the system path):

.. code-block:: python
   :caption: conf.py options for sphinxcontrib-plantuml

    plantuml = "java -jar /path/to/plantuml.jar"

Sequence Diagram
================

.. uml::

   actor Bob #red
   ' The only difference between actor
   'and participant is the drawing
   participant Alice
   participant "I have a really\nlong name" as L #99FF99
   /' You can also declare:
      participant L as "I have a really\nlong name"  #99FF99
   '/

   Alice->Bob: Authentication Request
   Bob->Alice: Authentication Response
   Bob->L: Log transaction

Another way is to include is with a file:

.. uml:: files/nested-groups.puml

Use Case Diagram
================

You can also include use case diagrams, which are a type of behavioral diagram that describes the interactions between a system and its actors. Use case diagrams are used to capture the functional requirements of a system, and to identify the actors that interact with the system.

.. uml:: files/use-case.puml

Class Diagram
=============

You can also include class diagrams, which are a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

.. uml:: files/class.puml

JSON Visualization
==================

You can also include JSON visualizations, which are a type of diagram that describes the structure of a JSON object. JSON visualizations are used to capture the structure of a JSON object, and to identify the different elements that make up the JSON object.

.. uml:: files/json.puml