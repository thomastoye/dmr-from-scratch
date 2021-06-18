.PHONY: test

default: test

test:
	black dmrpy
	PYTHONPATH=. pytest

test-ci:
	black --check --verbose dmrpy
	PYTHONPATH=. pytest

test-watch:
	PYTHONPATH=. ptw

format:
	black dmrpy
