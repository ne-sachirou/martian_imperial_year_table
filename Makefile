.PHONY: help
help:
	@awk -F':.*##' '/^[-_a-zA-Z0-9]+:.*##/{printf"%-12s\t%s\n",$$1,$$2}' $(MAKEFILE_LIST) | sort

.PHONY: build
build: ## Build.
	pipenv run transcrypt -b -k -m -n main.py
	mv __target__ docs/__target__

.PHONY: clean
clean: ## Clean built.
	rm -rf __target__ docs/__target__

.PHONY: setup
setup: ## Install deps.
	pipenv install --dev
	npm install

.PHONY: start
start: ## Start dev server.
	ruby -run -e httpd docs

.PHONY: test
test: ## Test.
	pipenv check
	pipenv run flake8 martian_calendar tests
	pipenv run mypy martian_calendar
	pipenv run python -m unittest discover -s tests
	pipenv run python -m unittest discover -s tests/martian_calendar
