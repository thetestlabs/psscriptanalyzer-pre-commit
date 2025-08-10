# Examples

## Test Files Overview

The `examples/` directory contains PowerShell files with intentional errors that demonstrate various PSScriptAnalyzer rules and violations. These examples serve multiple purposes:

- **Learning Tool**: Understand what PSScriptAnalyzer detects
- **Testing**: Verify the pre-commit hooks work correctly
- **Reference**: See examples of common PowerShell issues

## File Structure

```text
examples/
├── README.md                    # This file
├── scripts/                     # Script examples with various issues
│   ├── BadScript.ps1            # Basic scripting mistakes
│   ├── MixedSeverity.ps1        # All severity levels demonstrated
│   ├── AdvancedIssues.ps1       # Complex rule violations
│   ├── ConfigurationIssues.ps1   # Configuration-related problems
│   ├── InformationIssues.ps1    # Information-level violations
│   ├── EdgeCases.ps1            # Edge case scenarios
│   └── test.ps1                 # Simple test script
├── modules/                     # Module examples
│   ├── BadModule.psm1           # Module with security/performance issues
│   └── BadModule.psd1           # Module manifest with errors
├── functions/                   # Function examples
│   └── BadFunctions.psm1        # Function-specific violations
└── classes/                     # Class examples
    └── BadClasses.ps1           # PowerShell class issues
```

## Error Categories by Severity

### Error Level Issues (Red) 🔴

Critical problems that should always be fixed:

- **PSAvoidUsingPlainTextForPassword**: Plain text passwords in code
- **PSAvoidUsingInvokeExpression**: Dangerous `Invoke-Expression` usage
- **PSAvoidUsingConvertToSecureStringWithPlainText**: Insecure string conversion

### Warning Level Issues (Orange) 🟡

Important issues that affect code quality:

- **PSUseApprovedVerbs**: Non-approved verbs in function names
- **PSUseSingularNouns**: Plural nouns in function names
- **PSAvoidUsingWriteHost**: Using `Write-Host` inappropriately
- **PSUseDeclaredVarsMoreThanAssignments**: Variables assigned but never used
- **PSUseShouldProcessForStateChangingFunctions**: Missing ShouldProcess support

### Information Level Issues (Cyan) 🔵

Style and best practice suggestions:

- **PSAvoidUsingDoubleQuotesForConstantString**: Unnecessary double quotes
- **PSUseCorrectCasing**: Incorrect cmdlet casing
- **PSProvideCommentHelp**: Missing comment-based help

## Example Files Breakdown

### Scripts Directory

**`BadScript.ps1`** - Demonstrates basic scripting issues:
- Variable naming problems
- Unused parameters and variables  
- Plain text password handling
- Missing ShouldProcess support

**`MixedSeverity.ps1`** - Shows all three severity levels:
- Error: Security vulnerabilities
- Warning: Code quality issues
- Information: Style suggestions

**`AdvancedIssues.ps1`** - Complex rule violations:
- Advanced security concerns
- Performance anti-patterns
- Module design issues

### Modules Directory

**`BadModule.psm1`** - Module-specific problems:
- Security vulnerabilities in authentication
- Performance issues
- Module design violations

**`BadModule.psd1`** - Manifest validation errors:
- Missing required fields
- Invalid field values
- Encoding issues

### Functions Directory

**`BadFunctions.psm1`** - Function design issues:
- Parameter validation problems
- Function naming violations
- Help documentation issues

### Classes Directory

**`BadClasses.ps1`** - PowerShell class problems:
- Class design violations
- Property and method issues
- Inheritance problems

## Running Examples

### Test All Examples

Run PSScriptAnalyzer on all example files:

```bash
# Using pre-commit (will fail as expected)
pre-commit run psscriptanalyzer --files examples/**/*.ps*

# Direct PowerShell analysis
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/ -Recurse"
```

### Test Specific Categories

Run analysis on specific file types:

```bash
# Test all scripts
pre-commit run psscriptanalyzer --files examples/scripts/*.ps1

# Test module issues
pre-commit run psscriptanalyzer --files examples/modules/BadModule.psm1

# Test manifest problems
pre-commit run psscriptanalyzer --files examples/modules/BadModule.psd1

# Test function issues
pre-commit run psscriptanalyzer --files examples/functions/BadFunctions.psm1

# Test class issues
pre-commit run psscriptanalyzer --files examples/classes/BadClasses.ps1
```

### Test with Different Severity Levels

```bash
# Only show errors (critical issues)
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/ -Recurse -Severity Error"

# Show warnings and errors (recommended)
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/ -Recurse -Severity Warning"

# Show all issues including information
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/ -Recurse -Severity Information"
```

## Expected Output

When running PSScriptAnalyzer on these examples, you should see output similar to:

```text
examples/scripts/BadScript.ps1:15:5: PSAvoidUsingPlainTextForPassword: Parameter 'password' should use SecureString, otherwise this will expose passwords.

examples/scripts/BadScript.ps1:6:10: PSUseApprovedVerbs: The cmdlet 'Download-File' uses the verb 'Download' which is not in the list of approved verbs.

examples/modules/BadModule.psm1:8:9: PSAvoidUsingUserNameAndPasswordParams: Function 'Connect-ToService' has both Username and Password parameters.
```

## Using Examples for Development

### Pre-commit Hook Testing

These examples are perfect for testing pre-commit hook functionality:

```bash
# Install hooks
pre-commit install

# Test on examples (should fail)
git add examples/
git commit -m "Test commit"  # Will be blocked by hooks

# Run formatting (may fix some issues)
pre-commit run psscriptanalyzer-format --files examples/**/*.ps1
```

### GitHub Actions Integration

The examples work great with GitHub Actions annotations. When run in CI/CD, you'll see:

- **Error annotations** appear as red error markers
- **Warning annotations** appear as orange warning markers  
- **Information annotations** appear as blue notice markers

### Learning PowerShell Best Practices

Each file demonstrates what NOT to do:

1. **Read the comments**: Each violation is documented in the code
2. **Run analysis**: See what PSScriptAnalyzer reports
3. **Fix the issues**: Practice correcting common problems
4. **Compare results**: See how the analysis output changes

## Severity Level Testing

Use the `MixedSeverity.ps1` file to test different severity configurations:

```bash
# Test Error only (should show 2-3 issues)
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/scripts/MixedSeverity.ps1 -Severity Error"

# Test Warning and above (should show 5-7 issues)
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/scripts/MixedSeverity.ps1 -Severity Warning"

# Test All levels (should show 10+ issues)
pwsh -Command "Invoke-ScriptAnalyzer -Path ./examples/scripts/MixedSeverity.ps1 -Severity Information"
```

## Contributing New Examples

To add new example violations:

1. **Identify the rule**: Find a PSScriptAnalyzer rule not covered
2. **Choose the right directory**: Scripts, modules, functions, or classes
3. **Create minimal reproduction**: Write the smallest code that triggers the rule
4. **Add comments**: Explain what the violation demonstrates
5. **Test thoroughly**: Ensure PSScriptAnalyzer detects the issue
6. **Update this README**: Document the new example

### Example Template

```powershell
# Example: Rule Name (PSRuleName)
# This demonstrates [what the violation is]
# PSScriptAnalyzer should report: [expected message]

# Violating code here
function Bad-Example {
    # This violates PSRuleName because...
    Write-Host "This is problematic"
}

# Correct version (commented)
# function Good-Example {
#     Write-Output "This is better"
# }
```

## Integration with Documentation

These examples are referenced throughout the project documentation:

- **Installation Guide**: Used to verify hook installation works
- **Usage Examples**: Demonstrate different hook behaviors
- **Configuration Guide**: Show how settings affect output
- **Troubleshooting**: Help diagnose hook issues

## Summary

The examples directory provides a comprehensive test suite organized by PowerShell construct type (scripts, modules, functions, classes). Each file contains intentionally flawed code that demonstrates specific PSScriptAnalyzer rules across all severity levels. They serve as both a learning resource for PowerShell best practices and a validation tool for the pre-commit hook implementation.
