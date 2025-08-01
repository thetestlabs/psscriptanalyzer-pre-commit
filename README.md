# psscriptanalyzer-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer), the PowerShell static code analyzer.

This hook runs PSScriptAnalyzer on your PowerShell files (`.ps1`, `.psm1`, `.psd1`) before each commit to ensure code quality and adherence to PowerShell best practices.

## Prerequisites

Before using this hook, you need:

1. **PowerShell Core** (pwsh) installed on your system
   - **macOS**: `brew install powershell`
   - **Linux**: Follow [Microsoft's installation guide](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux)
   - **Windows**: Download from [PowerShell releases](https://github.com/PowerShell/PowerShell/releases)

2. **PSScriptAnalyzer module** installed in PowerShell:
   ```powershell
   Install-Module -Name PSScriptAnalyzer -Force -Scope CurrentUser
   ```

3. **pre-commit** installed:
   ```bash
   pip install pre-commit
   ```

## Installation

Add this hook to your `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/thetestlabs/psscriptanalyzer-pre-commit
    rev: v1.0.0  # Use the latest version
    hooks:
      - id: psscriptanalyzer
```

Then install the git hook scripts:

```bash
pre-commit install
```

## Configuration

### Basic Usage

The hook will run with default settings (Warning severity and above) on all PowerShell files.

### Advanced Configuration

You can customize the hook behavior by adding arguments:

```yaml
repos:
  - repo: https://github.com/thetestlabs/psscriptanalyzer-pre-commit
    rev: v1.0.0
    hooks:
      - id: psscriptanalyzer
        args:
          - --severity=Error  # Only show errors
          - --exclude-rule=PSAvoidUsingWriteHost
          - --exclude-rule=PSAvoidUsingInvokeExpression
```

### Available Arguments

- `--severity`: Minimum severity level to report
  - `Error`: Only show errors
  - `Warning`: Show warnings and errors (default)
  - `Information`: Show all issues including informational

- `--exclude-rule`: Exclude specific PSScriptAnalyzer rules (can be used multiple times)
  - Example: `--exclude-rule=PSAvoidUsingWriteHost`

### File Types

The hook automatically runs on files with these extensions:
- `.ps1` - PowerShell scripts
- `.psm1` - PowerShell modules  
- `.psd1` - PowerShell data files

## Example Output

When PSScriptAnalyzer finds issues, you'll see output like this:

```
Analyzing scripts/Deploy.ps1...

Issues found in scripts/Deploy.ps1:
  [Warning] PSAvoidUsingWriteHost at line 15, column 5
    Avoid using Write-Host because it might not work in all hosts, does not work when there is no host, and (starting with Windows PowerShell 2.0) does not work in the PowerShell ISE. Instead, use Write-Output, Write-Verbose, or Write-Information.
  [Error] PSAvoidUsingInvokeExpression at line 23, column 1
    Avoid using Invoke-Expression, or if you must use Invoke-Expression, ensure that the text being evaluated does not come from a user-provided input.

PSScriptAnalyzer found issues in your PowerShell files.
Please fix the issues above before committing.
```

## Common PSScriptAnalyzer Rules

Some commonly encountered rules that you might want to exclude:

- `PSAvoidUsingWriteHost`: Warns against using `Write-Host`
- `PSAvoidUsingInvokeExpression`: Warns against using `Invoke-Expression`
- `PSUseShouldProcessForStateChangingFunctions`: Requires `ShouldProcess` for functions that change state
- `PSProvideCommentHelp`: Requires comment-based help for functions

## Development

To work on this hook locally:

```bash
git clone https://github.com/thetestlabs/psscriptanalyzer-pre-commit.git
cd psscriptanalyzer-pre-commit

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

This project uses modern Python packaging with `pyproject.toml`. The development dependencies include tools like `black`, `isort`, `mypy`, and `pytest` for code formatting, type checking, and testing.

## Testing

You can test the hook manually:

```bash
psscriptanalyzer-hook path/to/your/script.ps1
```

Or run it on all PowerShell files in your repository:

```bash
pre-commit run psscriptanalyzer --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
