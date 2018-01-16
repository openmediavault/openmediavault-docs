# openmediavault-wiki
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

Now open <http://localhost:8000/> in your browser to view the documentation.
Any changes to the documentation code will be rendered now immediatelly.

Cleanup the generated HTML
--------------------------

	$ make clean
