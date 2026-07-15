.PHONY: run clean
.DEFAULT_GOAL := run

# You can set this to the name of your python interpreter
PY_COMMAND = python3

venv/bin/python:
	$(PY_COMMAND) -m venv venv

# Install requirements ONLY when requirements.txt changes.
# This depends on 'venv/bin/python' existing first.
# We 'touch' venv/bin/python at the end so its timestamp is newer than requirements.txt.
venv/bin/pip: requirements.txt venv/bin/python
	./venv/bin/pip install -r requirements.txt
	touch venv/bin/python

init: venv/bin/pip
	./venv/bin/python make_emojis.py

run: init
	./venv/bin/python main.py

clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
