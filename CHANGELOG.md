# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-08-08

### Added

- **PSScriptAnalyzer Integration**: Seamless integration with Microsoft's PSScriptAnalyzer for PowerShell static analysis
- **Pre-commit Hook Support**: Full compatibility with the pre-commit framework for automated code quality checks
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux with automatic PowerShell detection
- **Multiple PowerShell File Support**: Supports `.ps1`, `.psm1`, and `.psd1` file extensions
- **Configurable Severity Levels**: Filter analysis results by Error, Warning, Information, or All severity levels
- **Color-coded Terminal Output**: Enhanced readability with severity-based color coding in terminal output
- **GitHub Actions Integration**: Native support for GitHub Actions with proper error annotations (`::error`, `::warning`, `::notice`)
- **Automatic PowerShell Installation Detection**: Intelligent detection of PowerShell Core, Windows PowerShell, and pwsh installations
- **Comprehensive Documentation**: Complete documentation with installation guides, usage examples, and API reference
- **Professional Package Distribution**: Published to PyPI with proper metadata and dependency management

### Technical Features

- **Modern Python Packaging**: Built with `pyproject.toml` using modern Python packaging standards
- **Type Hints**: Full type annotation support for better IDE integration and maintainability
- **Robust Error Handling**: Comprehensive error handling with informative error messages
- **Environment-aware Output**: Different output formats for local development vs CI/CD environments
- **Zero Dependencies**: No external Python dependencies required for core functionality
- **Python 3.9+ Support**: Compatible with Python 3.9 through 3.13

### Documentation

- **ReadTheDocs Integration**: Professional documentation hosted at https://psscriptanalyzer-pre-commit.thetestlabs.io/
- **Comprehensive Guides**: Installation, usage, and configuration documentation
- **API Reference**: Complete function documentation with examples
- **CI/CD Examples**: Ready-to-use examples for GitHub Actions and other CI platforms
- **Troubleshooting Guide**: Common issues and solutions

### Package Management

- **PyPI Distribution**: Available via `pip install psscriptanalyzer-pre-commit`
- **Semantic Versioning**: Follows semantic versioning for reliable dependency management
- **MIT License**: Open source with permissive MIT license
- **Professional Metadata**: Complete package metadata with proper classifiers and keywords
