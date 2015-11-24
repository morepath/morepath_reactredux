Morepath backend for React + Redux
==================================

A Morepath REST backend with a React + Redux based frontend.

Morepath backend
----------------

You can run the code using a clean Python environment (using virtualenv)::

  $ python bootstrap-buildout.py

after this you can install dependencies using::

  $ bin/buildout

Once that is done you can start the server::

  $ bin/start

You can go to http://localhost:5000 to see the UI

JS bundle
---------

For an introduction to the JavaScript toolchain used see:

https://github.com/faassen/bundle_example

JavaScript code is in `js` subdirectory. To rebuild the bundle you
need to install the JS dependencies (listed in package.json). Run::

  $ npm install

to install them. Then run::

  $ webpack

To rebuild the bundle after changing it.
