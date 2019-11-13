About
=====

The Airship ``uareach`` (``Wallet``) library is a Python library for
using the `Airship <https://airship.com/>`__ Wallet REST API.

Version 0.1.0 is a beta release.  Please visit `Airship Support
<https://support.airship.com/>`_ with feature requests, questions,
bug reports, or comments.

Requirements
============

As of version 0.1.0, Python 2.7 is required.

For tests, ``uareach`` also needs `Mock <https://github.com/testing-cabal/mock>`_.

Running Tests
=============

To run tests, run:

    $ nosetests

Usage
=====

To get started, simply import the library and set up a client:

.. sourcecode:: python

   import uareach as ua

   client = ua.Reach('email', 'wallet_key')

   # Example: getting a pass
   my_pass = ua.get_pass(client, pass_id=12345)

For more details on using this library, please see the `full documentation
<https://docs.airship.com/api/libraries/reach/python/>`__, as well as the
`Airship Wallet API Documentation <https://docs.airship.com/api/wallet/>`__.
