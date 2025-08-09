[![codecov](https://codecov.io/github/thetestlabs/psscriptanalyzer-pre-commit/graph/badge.svg?token=TNARPWYQDS)](https://codecov.io/github/thetestlabs/psscriptanalyzer-pre-commit)
[![docs](https://app.readthedocs.org/projects/psscriptanalyzer-pre-commit/badge/?version=latest)](https://readthedocs.org/projects/psscriptanalyzer-pre-commit/)
[![PyPI version](https://badge.fury.io/py/psscriptanalyzer-pre-commit.svg)](https://badge.fury.io/py/psscriptanalyzer-pre-commit)

# PSScriptAnalyzer Pre-commit Hook

---

**[Read the documentation on ReadTheDocs!](https://psscriptanalyzer-pre-commit.thetestlabs.io)**

---

A pre-commit hook for [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) - catch PowerShell issues before they hit your repo!

## What it does

✅ **Lints PowerShell files** (`.ps1`, `.psm1`, `.psd1`) for code quality issues
✅ **Formats PowerShell code** automatically
✅ **Works everywhere** - Windows, macOS, Linux
✅ **Zero config** - installs PSScriptAnalyzer automatically
✅ **GitHub Actions ready** - standard error annotations

## Quick Start

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/thetestlabs/psscriptanalyzer-pre-commit
    rev: v0.1.0
    hooks:
      - id: psscriptanalyzer # Lint your PowerShell
      - id: psscriptanalyzer-format # Format your PowerShell
```

Then install and run:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files  # Test it out!
```

## Configuration

Show only critical errors:

```yaml
- id: psscriptanalyzer
  args: ["--severity", "Error"]
```

Show everything (default is Warning):

```yaml
- id: psscriptanalyzer
  args: ["--severity", "All"]
```

That's it! 🎉

## Prerequisites

- Python 3.9+
- PowerShell (any version - we'll find it!)

Need PowerShell? Get it here:

- **Windows**: Already installed, or get [PowerShell Core](https://github.com/PowerShell/PowerShell/releases)
- **macOS**: `brew install powershell`
- **Linux**: [Installation guide](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux)

## Documentation

Full documentation at **[psscriptanalyzer-pre-commit.readthedocs.io](https://psscriptanalyzer-pre-commit.readthedocs.io/)**

## Contributing

See the [Development Guide](https://psscriptanalyzer-pre-commit.docs.thetestlabs.io/en/latest/development.html) in our docs.

## License

MIT - see [LICENSE](LICENSE) file.
