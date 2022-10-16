# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = openmediavault-wiki
SOURCEDIR     = .
BUILDDIR      = _build
VENVDIR       = venv
PORT          = 8080

# Helper targets to create the isolated Python environment.
# E.g. `make PORT=8001 autobuild`
venv:
	( \
		virtualenv -p python3 $(VENVDIR); \
		. $(VENVDIR)/bin/activate; \
		pip install -r requirements.txt; \
	)

buildvenv: venv

autobuild: venv
	( \
		. $(VENVDIR)/bin/activate; \
		sphinx-autobuild --port $(PORT) "$(SOURCEDIR)" "$(BUILDDIR)/html" \
	)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf "$(BUILDDIR)"

lint:
	( \
		. $(VENVDIR)/bin/activate; \
		rstcheck --recursive *.rst ./administration ./development ./installation ./various \
	)

.PHONY: autobuild buildvenv clean help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
