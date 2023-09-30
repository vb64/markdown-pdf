.PHONY: all setup static db example superuser
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
PTEST = venv/Scripts/pytest.exe
COVERAGE = venv/Scripts/coverage.exe
else
PYTHON = ./venv/bin/python
PTEST = ./venv/bin/pytest
COVERAGE = ./venv/bin/coverage
endif

SOURCE = source
TESTS = tests

FLAKE8 = $(PYTHON) -m flake8
PYLINT = $(PYTHON) -m pylint
PYTEST = $(PTEST)
PIP = $(PYTHON) -m pip install

all: tests

test:
	$(PTEST) -s $(TESTS)/test/$(T)

flake8:
	$(FLAKE8) $(TESTS)/test
	$(FLAKE8) $(SOURCE)

lint:
	$(PYLINT) $(TESTS)/test
	$(PYLINT) $(SOURCE)

pep257:
	$(PYTHON) -m pydocstyle $(TESTS)/test
	$(PYTHON) -m pydocstyle $(SOURCE)

tests: flake8 pep257 lint
	$(PYTEST) --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

package:
	$(PYTHON) -m build -n

pypitest: package
	$(PYTHON) -m twine upload --config-file .pypirc --repository testpypi dist/*

pypi: package
	$(PYTHON) -m twine upload --config-file .pypirc dist/*

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r $(TESTS)/requirements.txt
	$(PIP) -r requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
