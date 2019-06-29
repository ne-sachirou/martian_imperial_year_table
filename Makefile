.PHONY: help
help:
	@awk -F':.*##' '/^[-_a-zA-Z0-9]+:.*##/{printf"%-12s\t%s\n",$$1,$$2}' $(MAKEFILE_LIST) | sort

within_docker := $(shell sh -c 'stat /.dockerenv 2> /dev/null')

.PHONY: build
build: ## Build.
ifeq ($(within_docker),)
	docker build -f Dockerfiles/Dockerfile.dev -t martian_imperial_year_table:latest --force-rm --pull .
	docker run -v $(shell pwd | sed -e 's/^\/mnt\/c/\/c/'):/data:cached --rm martian_imperial_year_table:latest make setup build
else
	mkdir -p static/css static/js
	cp node_modules/bulma/css/* static/css/
	pipenv run transcrypt -b -m -n ui_main.py
	mv __target__/* static/js/
endif

.PHONY: clean
clean: ## Clean built files.
	rm -rf __target__ static/css static/js

.PHONY: format
format: ## Format code.
	git grep -l $$'\r' | xargs -t sed -i -e 's/\r//'
	pipenv run black *.py imperial_calendar tests ui
	node_modules/.bin/prettier --write README.md

.PHONY: setup
setup: ## Install deps.
	pipenv install -d
	npm install

.PHONY: sh
sh: ## Run shell in docker.
	docker run -it -v $(shell pwd | sed -e 's/^\/mnt\/c/\/c/'):/data:cached --rm martian_imperial_year_table:latest sh

.PHONY: start
start: ## Start dev server.
	docker run -p 0.0.0.0:5000:5000 -v $(shell pwd | sed -e 's/^\/mnt\/c/\/c/'):/data --rm martian_imperial_year_table:latest

.PHONY: test
test: ## Test.
	# pipenv check || true
	# npm audit
	pipenv run black --check *.py imperial_calendar tests ui
	pipenv run flake8 .
	pipenv run mypy debug.py
	pipenv run python -m unittest discover -s tests/imperial_calendar
	pipenv run python -m unittest discover -s tests/imperial_calendar/internal
	pipenv run python -m unittest discover -s tests/imperial_calendar/transform
