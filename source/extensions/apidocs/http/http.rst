.. index:: HTTP API Documentation, API Documentation; HTTP, Sphinx domain for documenting HTTP

HTTP API Documentation
======================

For the simplest way to document your HTTP API, you can use the Sphinx domain for documenting HTTP. This extension allows you to document your HTTP APIs in a structured and standardized way, making it easier for developers to understand and use your API.

You can find the Sphinx domain for documenting HTTP https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/. 

Configuration
-------------

To use the Sphinx domain for documenting HTTP, you need to add it to the list of extensions in your :file:`conf.py` file:

.. code-block:: python
   :caption: conf.py options for sphinxcontrib-httpdomain

    extensions = [
        ...
        "sphinxcontrib.httpdomain",
        ...
    ]

Basic usage
-----------

There are several provided directives that describe HTTP resources.

.. sourcecode:: rst

   .. http:get:: /users/(int:user_id)/posts/(tag)

      The posts tagged with `tag` that the user (`user_id`) wrote.

      **Example request**:

      .. sourcecode:: http

         GET /users/123/posts/web HTTP/1.1
         Host: example.com
         Accept: application/json, text/javascript

      **Example response**:

      .. sourcecode:: http

         HTTP/1.1 200 OK
         Vary: Accept
         Content-Type: text/javascript

         [
           {
             "post_id": 12345,
             "author_id": 123,
             "tags": ["server", "web"],
             "subject": "I tried Nginx"
           },
           {
             "post_id": 12346,
             "author_id": 123,
             "tags": ["html5", "standards", "web"],
             "subject": "We go to HTML 5"
           }
         ]

      :query sort: one of ``hit``, ``created-at``
      :query offset: offset number. default is 0
      :query limit: limit number. default is 30
      :reqheader Accept: the response content type depends on
                         :mailheader:`Accept` header
      :reqheader Authorization: optional OAuth token to authenticate
      :resheader Content-Type: this depends on :mailheader:`Accept`
                               header of request
      :statuscode 200: no error
      :statuscode 404: there's no user

will be rendered as:

.. http:get:: /users/(int:user_id)/posts/(tag)

   The posts tagged with `tag` that the user (`user_id`) wrote.

   **Example request**:

   .. sourcecode:: http

      GET /users/123/posts/web HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
      {
         "post_id": 12345,
         "author_id": 123,
         "tags": ["server", "web"],
         "subject": "I tried Nginx"
      },
      {
         "post_id": 12346,
         "author_id": 123,
         "tags": ["html5", "standards", "web"],
         "subject": "We go to HTML 5"
      }
      ]

   :query sort: one of ``hit``, ``created-at``
   :query offset: offset number. default is 0
   :query limit: limit number. default is 30
   :reqheader Accept: the response content type depends on
                     :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                           header of request
   :statuscode 200: no error
   :statuscode 404: there's no user
