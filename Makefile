# Makefile for fastcomp
#
# Mostly for development.

PYTHON=/usr/bin/env python

all:

test:
	$(PYTHON) -m unittest discover -v tests

publish:
	$(PYTHON) setup.py sdist register upload

.PHONY: test
