# openmediavault-docs

Creating a virtual environment for Sphinx
-----------------------------------------

To avoid polluting your development system you should create and use an isolated
Python environment to install and use Sphinx.

To do so you need to install the Python virtualenv module. On Debian/Ubuntu you
can do this the following way:

	# apt-get install python3-virtualenv

To initially setup the virtual Python environment simply execute the following
lines:

	$ make buildvenv

Build the HTML code
-------------------

	$ make autobuild

Now open <http://localhost:8080/> in your browser to view the documentation.
Any changes to the documentation code will be rendered now immediatelly.

Cleanup the HTML code
---------------------

	$ make clean

reStructured text cheat-sheets
------------------------------
* http://www.sphinx-doc.org/en/stable/rest.html
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
* https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html

Contribute
----------
To contribute to the documentation simply clone this repository, make your
changes and create a PR (pull request).

License
-------
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
