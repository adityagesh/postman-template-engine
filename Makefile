VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
PYTEST := pytest

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
	$(shell export PYTHONPATH=./postmanrenderer)
	$(PYTHON) -m $(PYTEST) --cov-report term --cov=postmanrenderer
	
coverage:
	$(PYTHON) -m pytest --cov-report term --cov=postmanrenderer

twine-check: dist
	twine check dist/*

twine-test-upload: dist
	$(MAKE) twine-check
	twine upload  --verbose --repository-url https://test.pypi.org/legacy/ dist/* 

twine-upload: dist
	$(MAKE) twine-check
	twine upload dist/*

publish:
	$(MAKE) twine-test-upload

update-requirements:
	pip freeze --all > requirements.txt

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__  $(VENV) dist/

.PHONY: activate clean test setup setup-hooks coverage twine-check twine-test-upload twine-upload publish