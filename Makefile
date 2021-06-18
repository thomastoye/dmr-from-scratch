.PHONY: test

default: test

test:
	black --check dmrpy
	PYTHONPATH=. pytest

format:
	black dmrpy
