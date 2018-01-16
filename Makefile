# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = openmediavault-wiki
SOURCEDIR     = .
BUILDDIR      = _build
VENVDIR       = venv

# Helper targets to create the isolated Python environment.
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
		sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" \
	)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf "$(BUILDDIR)"

.PHONY: autobuild buildvenv clean help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
