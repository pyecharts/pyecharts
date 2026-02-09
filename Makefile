# Targets
.PHONY: help
help:
	@echo "Please use \`make <target>\` where <target> is one of"
	@echo "  test        -- run local unit tests"
	@echo "  lint        -- run flake8 for code linting"

.PHONY: test
test:
	@python test.py

.PHONY: lint
lint:
	@flake8 --exclude=build,images,example,examples --max-line-length=89 --ignore=F401
