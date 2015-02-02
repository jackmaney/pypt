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

License
=======

The MIT License (MIT)

Copyright (c) 2015 Jack Maney

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
