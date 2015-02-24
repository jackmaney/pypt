``TODO`` items (some of which are more amibitious than others):

* Figure out how to parse existing ``setup.py`` files (at least the arguments to the ``setup`` function within ``setup.py``) to more intelligently form a set of questions (rather than asking everything every damn time). This will involve the use of the ``tokenize`` module, and *maybe* ``ast``.

* Automatically searching the distribution directory tree for non-python files and create a relatively simple way for the user to specify which of them--if any--s/he wants to include in the distribution (eg data files, etc).

* Sane handling of ``MANIFEST.in`` (if that's even possible :P) if the user requests it.

* Grabbing more metadata from the ``git`` repository for the repo (if it exists).

* Using ``tree`` to create a basic visualization showing a diff of files that exist in the code base vs what is kept in a distribution (by doing a ``python setup.py sdist``, opening up the resulting tarball, and peeking inside).

* Expanding the command line API: perhaps a ``-i`` flag to go into the full-blown interactive mode, choosing sane defaults if no arguments are provided, and perhaps being able to specify a configuration file (if things become unwieldy enough)?

*  Version hunting: do a basic search through the Python code files to see if any of them include a ``__version__`` variable. If more than one exists, try to pick intelligently, and when that's not possible, prompt the user to choose (if said option is configured).
