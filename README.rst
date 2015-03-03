PyPT
==========

PyPT (or ``pypt``) stands for **Py**\ thon **P**\ ackage **T**\ ools. The main purpose of this project is to streamline and simplify the boilerplate and annoyances in creating a Python package for distribution--either locally via ``python setup.py install`` or via ``pip``.

This is inspired by `pip-init <https://github.com/juanpabloaj/pip-init>`_ by `@juanpabloaj <https://github.com/juanpabloaj>`_. This package differs in the following ways:

* The aims are broader than simple initialization of a basic ``setup.py`` file, including:

  * Keeping track of non-Python files in your distribution and wrangling MANIFEST.in
  * Keeping track of and updating requirements for your package.
  * A relatively simple command-line API for other basic changes to the ``setup`` function of ``setup.py``.
  * Being somewhat "git aware", in grabbing a likely URL for the repo, collaborator names and emails, etc.

* It's written using ``jinja2`` for code templates, ``ast`` for parsing existing code, and ``GitPython`` for grabbing git repo metadata.


Install
=======

::

    pip install PyPT

Or, you can clone this repository, navigate to the directory in which you cloned this repository, and do a

::

    python setup.py install

Usage
=====

Once the package is installed, you'll get an executable command by the name of ``pypt``:

::

    Usage:  pypt [--version] [--help]
            pypt <command> [<args>...]

    Commands:
        init    Set up a new Python package (setup.py, MANIFEST.in, etc)
        config  Get/set configuration options


To initialize a package, do ``pypt init`` in the directory in which you want to create a ``setup.py``:

::

    Usage: pypt init [options]

        -h --help
        -i --interactive   Interactive mode (without this flag, defaults are used)

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
