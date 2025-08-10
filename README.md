[![codecov](https://codecov.io/github/thetestlabs/psscriptanalyzer-pre-commit/graph/badge.svg?token=TNARPWYQDS)](https://codecov.io/github/thetestlabs/psscriptanalyzer-pre-commit)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8a0abedfefc04e2c8cd015eac0aa8f63)](https://app.codacy.com/gh/thetestlabs/psscriptanalyzer-pre-commit/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![docs](https://app.readthedocs.org/projects/psscriptanalyzer-pre-commit/badge/?version=latest)](https://readthedocs.org/projects/psscriptanalyzer-pre-commit/)
[![PyPI version](https://badge.fury.io/py/psscriptanalyzer-pre-commit.svg)](https://badge.fury.io/py/psscriptanalyzer-pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python Compatibility](https://img.shields.io/pypi/pyversions/psscriptanalyzer-pre-commit)](https://pypi.org/project/psscriptanalyzer-pre-commit/)
[![Test PSScriptAnalyzer Hook](https://github.com/thetestlabs/psscriptanalyzer-pre-commit/actions/workflows/test-psscriptanalyzer-hook.yaml/badge.svg)](https://github.com/thetestlabs/psscriptanalyzer-pre-commit/actions/workflows/test-psscriptanalyzer-hook.yaml)

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
✅ **GitHub Actions ready** - with standard error annotations

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

Full documentation can be found **[here](https://psscriptanalyzer-pre-commit.thetestlabs.io/)**

## Contributing

See the **[Development Guide](https://psscriptanalyzer-pre-commit.thetestlabs.io/en/latest/development.html)** in our docs.

## License

MIT - see [LICENSE](LICENSE) file.
