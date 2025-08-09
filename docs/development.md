# Development

This guide covers how to contribute to and develop the PSScriptAnalyzer Pre-commit Hook.

## Prerequisites

- Python 3.9+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- PowerShell Core (pwsh) or Windows PowerShell

## Development Setup

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/thetestlabs/psscriptanalyzer-pre-commit.git
cd psscriptanalyzer-pre-commit

# Install uv (if not already installed)
# On macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install dependencies using uv
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install
```

### Using Traditional Python Setup

```bash
# Clone the repository
git clone https://github.com/thetestlabs/psscriptanalyzer-pre-commit.git
cd psscriptanalyzer-pre-commit

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Testing the Hook

### Local Testing

```bash
# Run on files directly
uv run psscriptanalyzer-hook --help
uv run psscriptanalyzer-hook script.ps1
uv run psscriptanalyzer-hook --format script.ps1
uv run psscriptanalyzer-hook --severity Error script.ps1

# Alternative: using Python module execution
uv run python -m psscriptanalyzer_hook script.ps1
```

### Without uv

```bash
python -m psscriptanalyzer_hook --help
python -m psscriptanalyzer_hook script.ps1
```

## Code Quality

### Running Quality Checks

```bash
# With uv
uv run ruff check .
uv run ruff format .
uv run mypy psscriptanalyzer_hook.py

# Without uv
ruff check .
ruff format .
mypy psscriptanalyzer_hook.py
```

### Running Tests

```bash
# With uv
uv run pytest

# Without uv
pytest
```

### Pre-commit Hooks

```bash
# Run all pre-commit hooks
uv run pre-commit run --all-files

# Without uv
pre-commit run --all-files
```

## Building and Publishing

### Building the Package

```bash
# Build wheel and source distribution
uv build

# Check package integrity
uv run twine check dist/*
```

### Documentation

The documentation is built using Sphinx and hosted on ReadTheDocs. To build locally:

```bash
# Install documentation dependencies
uv sync --group docs

# Build documentation
uv run sphinx-build -b html docs docs/_build/html
```

## Project Structure

```
psscriptanalyzer-pre-commit/
├── psscriptanalyzer_hook.py    # Main hook implementation
├── pyproject.toml              # Project configuration
├── .pre-commit-hooks.yaml      # Hook definitions
├── docs/                       # Documentation
├── tests/                      # Test suite
└── examples/                   # Example PowerShell files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Run the quality checks
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Write docstrings for public functions
- Keep functions focused and well-documented
- Add tests for new functionality

### Testing

- Write tests for new features and bug fixes
- Ensure all tests pass before submitting a PR
- Test on multiple platforms if possible (Windows, macOS, Linux)
- Test with different PowerShell versions if available

## Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with new version
3. Create and push a version tag: `git tag v0.1.0 && git push origin v0.1.0`
4. GitHub Actions will automatically build and publish to PyPI

## Architecture

### How the Hook Works

1. **File Detection**: The hook detects PowerShell files (`.ps1`, `.psm1`, `.psd1`) in the commit
2. **PowerShell Discovery**: Finds available PowerShell executable (`pwsh` or `powershell`)
3. **PSScriptAnalyzer Check**: Verifies PSScriptAnalyzer module is installed, installs if needed
4. **Analysis/Formatting**: Runs the appropriate PSScriptAnalyzer command
5. **Output Processing**: Formats and displays results with color coding and GitHub Actions annotations

### Key Components

- **`find_powershell_executable()`**: Cross-platform PowerShell detection
- **`main()`**: Main entry point and argument parsing
- **Color output**: Environment-aware formatting for terminal vs CI
- **Error handling**: Robust error reporting and recovery
