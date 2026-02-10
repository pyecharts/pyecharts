# AGENTS.md

This file contains guidelines for agents working on the pyecharts project.

## Build/Lint/Test Commands

### Running Tests

The project uses multiple testing frameworks. Here are the commands to run tests:

1. **Run all tests**:
   ```bash
   make test
   # or
   python test.py
   # or
   nose2 --with-coverage --coverage pyecharts --coverage-config .coveragerc -s test
   # or
   pytest -cov-config=.coveragerc --cov=./ test/
   ```

2. **Run a single test file**:
   ```bash
   # Using pytest (recommended)
   pytest test/test_chart.py
   
   # Using nose2
   nose2 --with-coverage --coverage pyecharts --coverage-config .coveragerc test.test_chart
   ```

3. **Run a specific test method**:
   ```bash
   # Using pytest
   pytest test/test_chart.py::TestChartClass::test_chart_dark_mode
   
   # Using nose2
   nose2 --with-coverage --coverage pyecharts --coverage-config .coveragerc test.test_chart.TestChartClass.test_chart_dark_mode
   ```

4. **Run tests with verbose output**:
   ```bash
   pytest -v test/test_chart.py
   ```

5. **Run tests with coverage reporting**:
   ```bash
   pytest -v --cov=./ --cov-report=html test/test_chart.py
   ```

### Linting

1. **Run linter**:
   ```bash
   make lint
   # or
   flake8 --exclude=build,images,example,examples --max-line-length=89 --ignore=F401
   ```

2. **Lint a specific file**:
   ```bash
   flake8 --exclude=build,images,example,examples --max-line-length=89 --ignore=F401 test/test_chart.py
   ```

### Formatting

The project uses black and isort for code formatting:

1. **Run black formatter**:
   ```bash
   black .
   ```

2. **Run isort for imports**:
   ```bash
   isort .
   ```

### Building

1. **Build the package**:
   ```bash
   python setup.py sdist bdist_wheel
   ```

2. **Upload to PyPI**:
   ```bash
   make upload
   # This runs the UploadCommand defined in setup.py
   ```

## Code Style Guidelines

### Imports

1. **Import organization**:
   - Standard library imports
   - Related third party imports
   - Local application/library specific imports

2. **Import style**:
   ```python
   # Good
   from pyecharts import options as opts
   from pyecharts.charts import Line, Bar
   
   # Avoid
   from pyecharts.options import *
   import pyecharts.charts.Line
   ```

3. **Use aliases** for commonly used modules:
   ```python
   import pyecharts.options as opts
   import pyecharts.globals as globals
   ```

### Formatting

1. **Line length**: 89 characters max (as specified in flake8 command)

2. **Indentation**: 4 spaces (no tabs)

3. **Quotes**: Use double quotes " for strings, single quotes ' for char literals

4. **Blank lines**:
   - Top-level functions and classes: 2 blank lines
   - Methods within a class: 1 blank line

5. **Use black formatter** to ensure consistent code style

### Naming Conventions

1. **Variables and functions**: snake_case
   ```python
   def add_yaxis(self, series_name, y_axis, *args, **kwargs):
       pass
   ```

2. **Classes**: PascalCase
   ```python
   class TestChartClass(unittest.TestCase):
       pass
   ```

3. **Constants**: UPPER_CASE
   ```python
   MAX_RETRIES = 3
   ```

4. **Private members**: prefix with _
   ```python
   def _internal_method(self):
       pass
   ```

### Error Handling

1. **Use exceptions** for error conditions, not return codes

2. **Be specific** with exception types:
   ```python
   try:
       result = do_something()
   except ValueError as e:
       logger.error(f"Invalid value: {e}")
       raise
   except RuntimeError as e:
       logger.error(f"Runtime error: {e}")
       raise
   ```

3. **Don't catch all exceptions** indiscriminately:
   ```python
   # Avoid
   try:
       do_something()
   except:
       pass
   
   # Prefer
   try:
       do_something()
   except SpecificError:
       handle_specific_error()
   ```

### Testing Guidelines

1. **Test structure**:
   - Use unittest framework with TestCase classes
   - Group related tests in classes
   - Use descriptive test method names

2. **Test naming**:
   ```python
   def test_chart_dark_mode(self):
       # Tests a specific feature
       
   def test_chart_line_style_opts(self):
       # Tests a specific option
   ```

3. **Use mocking** for external dependencies:
   ```python
   @patch("pyecharts.render.engine.write_utf8_html_file")
   def test_chart_dark_mode(self, fake_writer):
       # Test code here
   ```

4. **Test coverage**:
   - Aim for high test coverage
   - Test both success and failure cases
   - Test edge cases

### Documentation

1. **Docstrings**:
   - Use Google-style docstrings
   - Include Args, Returns, and Raises sections when applicable

   ```python
   def add_yaxis(self, series_name, y_axis, color=None):
       """Add a series to the chart.
   
       Args:
           series_name (str): Name of the series.
           y_axis (list): Data values.
           color (str, optional): Color of the series. Defaults to None.
   
       Returns:
           Chart: The chart instance for method chaining.
       """
   ```

2. **Comments**:
   - Use comments to explain "why", not "what"
   - Keep comments up-to-date with code changes

### Best Practices

1. **Method chaining**: The library supports method chaining, so return self in methods that modify the object:
   ```python
   def add_xaxis(self, xaxis_data):
       self.options["xAxis"][0]["data"] = xaxis_data
       return self  # Enable method chaining
   ```

2. **Type hints**: Use type hints for better code documentation and IDE support:
   ```python
   def add_yaxis(self, series_name: str, y_axis: list) -> "Base":
       # method implementation
       return self
   ```

3. **Immutable options**: When adding options, don't modify the original option objects:
   ```python
   # Good - create a copy
   self.options = deepcopy(self.options)
   
   # Or use dict constructor
   new_opts = dict(old_opts)
   ```

4. **Performance**: Be mindful of performance when processing large datasets.

5. **Backward compatibility**: When making changes, consider backward compatibility for existing users.

## Development Workflow

1. **Make changes** to the code
2. **Run tests** to ensure nothing is broken:
   ```bash
   make test
   ```
3. **Lint the code**:
   ```bash
   make lint
   ```
4. **Format the code**:
   ```bash
   black .
   isort .
   ```
5. **Commit and push** your changes

## Additional Notes

- The project uses both pytest and nose2 for testing. pytest is recommended for running individual tests.
- Coverage is configured in .coveragerc to exclude test files and templates.
- The build process is defined in setup.py with a custom UploadCommand for publishing to PyPI.
- JavaScript dependencies are managed through the js_dependencies attribute in Base class.
- The default locale is Chinese (ZH), but can be changed to English (EN).
- Charts support dark mode via set_dark_mode() method.
- Use the render() method to generate HTML files, and render_embed() for embedding charts.