VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
PYTEST := pytest

setup:
	$(MAKE) setup-hooks
	$(VENV)/bin/activate

setup-hooks:
	cp hooks/commit-msg .git/hooks/
	chmod +x .git/hooks/commit-msg

activate:  
	$(VENV)/bin/activate

build: 
	$(MAKE) activate
	python setup.py bdist_wheel

test: 
	$(MAKE) activate
	$(PYTHON) -m $(PYTEST) --cov-report term --cov=postmanrenderer
	
coverage:
	$(PYTHON) -m pytest --cov-report term --cov=postmanrenderer

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

.PHONY: activate clean build test setup setup-hooks coverage