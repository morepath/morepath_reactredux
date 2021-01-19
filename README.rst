.. image:: https://github.com/morepath/morepath_reactredux/workflows/CI/badge.svg?branch=master
   :target: https://github.com/morepath/morepath_reactredux/actions?workflow=CI
   :alt: CI Status

.. image:: https://coveralls.io/repos/github/morepath/morepath_reactredux/badge.svg?branch=master
    :target: https://coveralls.io/github/morepath/morepath_reactredux?branch=master

.. image:: https://img.shields.io/pypi/v/morepath_reactredux.svg
  :target: https://pypi.org/project/morepath_reactredux/

.. image:: https://img.shields.io/pypi/pyversions/morepath_reactredux.svg
  :target: https://pypi.org/project/morepath_reactredux/


Morepath backend for React + Redux
==================================

A Morepath REST backend with a React + Redux based frontend.

Morepath backend
----------------

You can run the code using a clean Python environment (using virtualenv)::

  $ virtualenv env
  $ source env/bin/activate

After this you can install dependencies using::

  $ env/bin/pip install -e .

Once that is done you can start the server::

  $ env/bin/run-app

You can go to http://localhost:5000 to see the UI

For installing the test suite and running the tests use::

  $ env/bin/pip install -e '.[test]'
  $ env/bin/py.test

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
