# Variables
PACKAGE_NAME = pyecharts

# Targets
.PHONY: help
help:
	@echo "Please use \`make <target>\` where <target> is one of"
	@echo "  test        -- run local unit tests"
	@echo "  build       -- build the package"
	@echo "  lint        -- run flake8 for code linting"
	@echo "  clean       -- clean up temporary files"

.PHONY: test
test:
	@uv run pytest -v --cov-config=pyproject.toml --cov=./ test/

.PHONY: build
build:
	@uv build

.PHONY: lint
lint:
	@uv run flake8 --exclude=build,images,example,examples,.venv --max-line-length=89 --ignore=F401,F824

.PHONY: clean
clean:
	@rm -rf dist build $(PACKAGE_NAME).egg-info
	@rm -f .coverage coverage.xml tests/.coverage tests/coverage.xml resize_render.html
