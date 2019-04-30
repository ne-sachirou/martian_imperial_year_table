.PHONY: help
help:
	@awk -F':.*##' '/^[-_a-zA-Z0-9]+:.*##/{printf"%-12s\t%s\n",$$1,$$2}' $(MAKEFILE_LIST) | sort

.PHONY: build
build: ## Build.
	pipenv run transcrypt -b -k -m -n main.py
	mkdir -p docs/js
	mv __target__/* docs/js/

.PHONY: clean
clean: ## Clean built.
	rm -rf __target__ docs/js

.PHONY: format
format: ## Format code.
	pipenv run yapf -i -r main.py imperial_calendar tests

.PHONY: setup
setup: ## Install deps.
	pipenv install --dev
	npm install

.PHONY: start
start: ## Start dev server.
	python -m http.server --directory docs

.PHONY: test
test: ## Test.
	pipenv check
	pipenv run flake8 imperial_calendar tests
	pipenv run mypy imperial_calendar
	pipenv run python -m unittest discover -s tests
	pipenv run python -m unittest discover -s tests/imperial_calendar
