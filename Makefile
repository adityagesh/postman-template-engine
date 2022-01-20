SHELL=/bin/bash
VENV := venv
PYTHON := $(VENV)/bin/python3
PYTHON-M := $(PYTHON) -m
PIP := $(VENV)/bin/pip
PYTEST := pytest
EXPORT_PYPATH = export PYTHONPATH=./postmanrenderer

setup:
	$(MAKE) setup-hooks
	$(MAKE) $(VENV)/bin/activate

setup-hooks:
	if [ -d ".git" ]; then \
		cp hooks/commit-msg .git/hooks/; \
		chmod +x .git/hooks/commit-msg; \
	fi

activate: $(VENV)/bin/activate
	. $(VENV)/bin/activate

dist: $(VENV)/bin/activate
	$(PYTHON) setup.py sdist bdist_wheel

test: 
	$(MAKE) activate
	$(EXPORT_PYPATH) && $(PYTHON) -m $(PYTEST) --cov-report term --cov=postmanrenderer
	
coverage:
	$(EXPORT_PYPATH) && $(PYTHON) -m pytest --cov-report term --cov=postmanrenderer

twine-check: dist
	$(PYTHON-M) twine check dist/*

twine-test-upload: dist
	$(MAKE) twine-check
	$(PYTHON-M) twine upload --username ${TWINE_USERNAME} --password ${TWINE_TEST_PASSWORD} --verbose --repository-url https://test.pypi.org/legacy/ dist/* 


twine-upload: dist
	$(MAKE) twine-check
	$(PYTHON-M) twine upload --username ${TWINE_USERNAME} --password ${TWINE_PASSWORD} --verbose dist/* 

publish:
	if [[ "$(RELEASE_VERSION)" == *"pre-"* ]]; then \
	$(MAKE) twine-test-upload; \
	else \
	$(MAKE) twine-upload; \
	fi

update-requirements:
	pip freeze --all > requirements.txt

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__  $(VENV) dist/

.PHONY: activate clean test setup setup-hooks coverage twine-check twine-test-upload twine-upload publish