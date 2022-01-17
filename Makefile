VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

activate: $(VENV)/bin/activate

build: 
	$(MAKE) activate
	python setup.py bdist_wheel

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

.PHONY: activate clean