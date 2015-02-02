pip-create
==========

Tools to simplify the process of creating and sharing Python distributions to `pypi <https://pypi.python.org/pypi>`_.

This is a fork of `pip-init <https://github.com/juanpabloaj/pip-init>`_ by `@juanpabloaj <https://github.com/juanpabloaj>`_. The primary difference is that it makes use of the `Jinja2 <http://jinja.pocoo.org/>`_ templating engine to make the code templates more extensible.

Install
=======

::

    pip install pip-create

Or, you can clone this repository, navigate to the directory in which you cloned this repository, and do a

::

    python setup.py install

Usage
=====

::

    pip-create


...and then just follow the interactive prompts. Once you're done, you'll have a bright, new, shiny `setup.py`.
