.PHONY: help
help:
	@awk -F':.*##' '/^[-_a-zA-Z0-9]+:.*##/{printf"%-12s\t%s\n",$$1,$$2}' $(MAKEFILE_LIST) | sort

.PHONY: build
build: ## Build.
	mkdir -p docs/css
	cp node_modules/bulma/css/* docs/css/
	pipenv run transcrypt -b -k -m -n main.py
	mkdir -p docs/js
	mv __target__/* docs/js/

.PHONY: clean
clean: ## Clean built.
	rm -rf __target__ docs/css docs/js

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
	# pipenv check
	# npm audit
	pipenv run flake8 imperial_calendar tests
	pipenv run mypy imperial_calendar
	pipenv run python -m unittest discover -s tests
	pipenv run python -m unittest discover -s tests/imperial_calendar
