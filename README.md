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

	$ virtualenv -p python3 venv
	$ cd venv
	$ source bin/activate
	$ pip install -r ../requirements.txt
