.PHONY: test

default: test

test:
	PYTHONPATH=. pytest

