# Usage

## Basic Usage

Once installed, the PSScriptAnalyzer pre-commit hooks will automatically run on PowerShell files during git commits.

### Available Hooks

The package provides two main hooks:

1. **`psscriptanalyzer`** - Static analysis and linting
2. **`psscriptanalyzer-format`** - Code formatting

### Automatic Execution

When you commit PowerShell files (`.ps1`, `.psm1`, `.psd1`), the hooks will automatically:

1. **Analysis Hook**: Check for code quality issues, style violations, and potential bugs
2. **Format Hook**: Apply consistent formatting to your PowerShell code

```bash
git add MyScript.ps1
git commit -m "Add new PowerShell script"
# Hooks run automatically
```

### Manual Execution

You can also run the hooks manually:

#### Run All Hooks

```bash
# Run on all PowerShell files
pre-commit run --all-files

# Run on specific files
pre-commit run --files MyScript.ps1 MyModule.psm1
```

#### Run Specific Hooks

```bash
# Run only the analyzer
pre-commit run psscriptanalyzer --all-files

# Run only the formatter
pre-commit run psscriptanalyzer-format --all-files
```

## Hook Behavior

### PSScriptAnalyzer Hook

The analyzer hook will:

- Scan PowerShell files for issues based on PSScriptAnalyzer rules
- Report violations with rule name, severity, file, line number, and description
- Exit with code 1 if issues are found (blocking the commit)
- Exit with code 0 if no issues are found

**Example output:**

```text
Using PowerShell: pwsh
Analyzing 2 PowerShell file(s)...

Warning: MyScript.ps1: Line 15:1: PSAvoidUsingWriteHost
  File 'MyScript.ps1' uses Write-Host. Avoid using Write-Host because it might not work in all hosts, does not work when there is no host, and (prior to PS 5.0) cannot be suppressed, captured, or redirected. Instead, use Write-Output, Write-Verbose, or Write-Information.

Warning: MyScript.ps1: Line 8:1: PSUseSingularNouns
  The cmdlet 'Get-Files' uses a plural noun. A singular noun should be used instead.

Found 2 issue(s)
```

### PSScriptAnalyzer Format Hook

The formatter hook will:

- Apply consistent formatting to PowerShell code
- Automatically fix style issues when possible
- Modify files in-place with improved formatting
- Report which files were formatted

**Example output:**

```text
Using PowerShell: pwsh
Formatting 2 PowerShell file(s)...
Formatted: MyScript.ps1
Formatted: MyModule.psm1
```

## Integration with Git Workflow

### Pre-commit Integration

The hooks integrate seamlessly with your git workflow:

1. **Stage your changes**: `git add .`
2. **Attempt commit**: `git commit -m "Your message"`
3. **Hooks run automatically**:
   - If analysis finds issues → commit blocked, issues reported
   - If formatting changes files → commit blocked, files modified
   - If all checks pass → commit proceeds

### Handling Hook Failures

#### Analysis Failures

When the analyzer finds issues:

1. Review the reported violations
2. Fix the issues in your code
3. Stage the changes: `git add .`
4. Retry the commit: `git commit -m "Your message"`

#### Formatting Changes

When the formatter modifies files:

1. The modified files are automatically saved
2. Review the formatting changes: `git diff`
3. Stage the formatted files: `git add .`
4. Retry the commit: `git commit -m "Your message"`

## Command Line Options

### PSScriptAnalyzer Arguments

You can customize the analyzer behavior with arguments:

```yaml
hooks:
  - id: psscriptanalyzer
    args: ["--severity", "Error"]  # Only show errors
```

#### Available Severity Levels

- **`Information`** - All rules including informational suggestions
- **`Warning`** - Warnings and errors (default)
- **`Error`** - Only critical errors

### Examples

#### Strict Configuration (Errors Only)

```yaml
repos:
  - repo: https://github.com/thetestlabs/psscriptanalyzer-pre-commit
    rev: v0.1.0
    hooks:
      - id: psscriptanalyzer
        args: ["--severity", "Error"]
      - id: psscriptanalyzer-format
```

#### Comprehensive Configuration (All Issues)

```yaml
repos:
  - repo: https://github.com/thetestlabs/psscriptanalyzer-pre-commit
    rev: v0.1.0
    hooks:
      - id: psscriptanalyzer
        args: ["--severity", "All"]
      - id: psscriptanalyzer-format
```

## File Selection

The hooks automatically target PowerShell files with these extensions:

- `.ps1` - PowerShell scripts
- `.psm1` - PowerShell modules
- `.psd1` - PowerShell data files/manifests

Other files are ignored by the hooks.

## Bypassing Hooks

### Skip All Hooks

```bash
git commit --no-verify -m "Skip all pre-commit hooks"
```

### Skip Specific Hooks

```bash
# Skip only PSScriptAnalyzer hooks
SKIP=psscriptanalyzer,psscriptanalyzer-format git commit -m "Skip PowerShell hooks"
```

## CI/CD Integration

The hooks work well in CI/CD environments. You can use them either with pre-commit or directly:

### Using with Pre-commit

```yaml
# GitHub Actions example
- name: Run pre-commit
  run: |
    pip install pre-commit
    pre-commit run --all-files
```

### Using Package Directly

You can also install and use the package directly without pre-commit:

```yaml
name: PowerShell Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  powershell-quality:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.13'

    - name: Install PowerShell
      run: |
        # Install PowerShell on Ubuntu
        wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
        sudo dpkg -i packages-microsoft-prod.deb
        sudo apt-get update
        sudo apt-get install -y powershell

    - name: Install PSScriptAnalyzer Hook
      run: |
        pip install psscriptanalyzer-pre-commit

    - name: Run PowerShell Analysis
      run: |
        # Analyze PowerShell files with Warning level (default)
        psscriptanalyzer-hook --severity Warning src/**/*.ps1 src/**/*.psm1 src/**/*.psd1
      continue-on-error: true  # Don't fail build, just report issues

    - name: Run PowerShell Formatting Check
      run: |
        # Check if files need formatting
        psscriptanalyzer-hook --format src/**/*.ps1 src/**/*.psm1

        # Check for any formatting changes
        if [[ -n $(git status --porcelain) ]]; then
          echo "❌ Files need formatting. Please run 'psscriptanalyzer-hook --format' locally."
          echo "Files that need formatting:"
          git status --porcelain
          git diff
          exit 1
        else
          echo "✅ All PowerShell files are properly formatted."
        fi

    - name: Run Strict Analysis (Errors Only)
      run: |
        # Fail build on errors
        psscriptanalyzer-hook --severity Error src/**/*.ps1 src/**/*.psm1 src/**/*.psd1
```

### Cross-Platform Example

```yaml
name: Cross-Platform PowerShell Quality

on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        severity: [Error, Warning]

    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install PowerShell (Linux)
      if: runner.os == 'Linux'
      run: |
        sudo apt-get update
        sudo apt-get install -y powershell

    - name: Install PowerShell (macOS)
      if: runner.os == 'macOS'
      run: brew install powershell

    - name: Install PSScriptAnalyzer Hook
      run: pip install psscriptanalyzer-pre-commit

    - name: Test PowerShell Files
      run: |
        # Run analysis with matrix severity level
        psscriptanalyzer-hook --severity ${{ matrix.severity }} src/**/*.ps*
```

### Simple Validation Workflow

For basic validation without pre-commit:

```yaml
name: Validate PowerShell

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - run: |
        pip install psscriptanalyzer-pre-commit
        sudo apt-get update && sudo apt-get install -y powershell

        # Quick validation - errors only
        psscriptanalyzer-hook --severity Error **/*.ps1 **/*.psm1 **/*.psd1
```
