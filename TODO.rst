``TODO`` items (some of which are more amibitious than others):

* Requirements:

  * Fix `The conflation of requirements in setup.py with requirements.txt <https://caremad.io/2013/07/setup-vs-requirement/>`_.
  * Different types of requirements (install, dev, setup).
  * Use ``ast`` and `our newly built package <https://github.com/jackmaney/python-stdlib-list>`_ to find module imports within the given package that are not in the Python standard library.
  

* Use ``ast`` to parse an existing ``setup.py``. Use this layer of parameters when merging user input (and prioritize it higher than any existing ``.pyptrc``).

* Automatically searching the distribution directory tree for non-python files and create a relatively simple way for the user to specify which of them--if any--s/he wants to include in the distribution (eg data files, etc).

* Sane handling of ``MANIFEST.in`` (if that's even possible :P) if the user requests it.

* Using ``tree`` to create a basic visualization showing a diff of files that exist in the code base vs what is kept in a distribution (by doing a ``python setup.py sdist``, opening up the resulting tarball, and peeking inside).

*  Version hunting: do a basic search through the Python code files to see if any of them include a ``__version__`` variable. If more than one exists, try to pick intelligently, and when that's not possible, prompt the user to choose (if said option is configured).
