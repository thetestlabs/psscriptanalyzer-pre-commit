#!/usr/bin/env python3
"""
Pre-commit hook for PSScriptAnalyzer.

This script runs PSScriptAnalyzer on PowerShell files and reports any issues found.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Sequence


def run_psscriptanalyzer(files: List[str], severity: str = "Warning", exclude_rules: Optional[List[str]] = None) -> int:
    """
    Run PSScriptAnalyzer on the specified files.
    
    Args:
        files: List of PowerShell files to analyze
        severity: Minimum severity level to report (Error, Warning, Information)
        exclude_rules: List of rules to exclude from analysis
    
    Returns:
        Exit code (0 for success, 1 for issues found)
    """
    if not files:
        return 0
    
    # Check if PowerShell is available
    try:
        result = subprocess.run(
            ["pwsh", "-Command", "Get-Module -ListAvailable PSScriptAnalyzer"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            print("Error: PSScriptAnalyzer module not found. Please install it using:")
            print("Install-Module -Name PSScriptAnalyzer -Force -Scope CurrentUser")
            return 1
    except FileNotFoundError:
        print("Error: PowerShell (pwsh) not found. Please install PowerShell Core.")
        return 1
    
    issues_found = False
    
    for file_path in files:
        print(f"Analyzing {file_path}...")
        
        # Build PowerShell command
        ps_command = f"Invoke-ScriptAnalyzer -Path '{file_path}' -Severity {severity}"
        
        if exclude_rules:
            exclude_rules_str = "'" + "','".join(exclude_rules) + "'"
            ps_command += f" -ExcludeRule @({exclude_rules_str})"
        
        ps_command += " | ConvertTo-Json -Depth 3"
        
        try:
            result = subprocess.run(
                ["pwsh", "-Command", ps_command],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(f"Error running PSScriptAnalyzer on {file_path}:")
                print(result.stderr)
                return 1
            
            # Parse JSON output
            if result.stdout.strip():
                try:
                    issues = json.loads(result.stdout)
                    if not isinstance(issues, list):
                        issues = [issues] if issues else []
                    
                    if issues:
                        issues_found = True
                        print(f"\nIssues found in {file_path}:")
                        for issue in issues:
                            severity_level = issue.get('Severity', 'Unknown')
                            rule_name = issue.get('RuleName', 'Unknown')
                            message = issue.get('Message', 'No message')
                            line = issue.get('Line', 'Unknown')
                            column = issue.get('Column', 'Unknown')
                            
                            print(f"  [{severity_level}] {rule_name} at line {line}, column {column}")
                            print(f"    {message}")
                        print()
                
                except json.JSONDecodeError:
                    # If JSON parsing fails, treat any output as potential issues
                    if result.stdout.strip():
                        issues_found = True
                        print(f"\nPSScriptAnalyzer output for {file_path}:")
                        print(result.stdout)
        
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return 1
    
    if issues_found:
        print("PSScriptAnalyzer found issues in your PowerShell files.")
        print("Please fix the issues above before committing.")
        return 1
    else:
        print("PSScriptAnalyzer: All files passed analysis!")
        return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main entry point for the pre-commit hook."""
    parser = argparse.ArgumentParser(
        description="Run PSScriptAnalyzer on PowerShell files"
    )
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames to check"
    )
    parser.add_argument(
        "--severity",
        choices=["Error", "Warning", "Information"],
        default="Warning",
        help="Minimum severity level to report (default: Warning)"
    )
    parser.add_argument(
        "--exclude-rule",
        action="append",
        dest="exclude_rules",
        help="PSScriptAnalyzer rules to exclude (can be specified multiple times)"
    )
    
    args = parser.parse_args(argv)
    
    # Filter for PowerShell files
    ps_files = []
    for filename in args.filenames:
        path = Path(filename)
        if path.suffix.lower() in ['.ps1', '.psm1', '.psd1']:
            ps_files.append(filename)
    
    if not ps_files:
        return 0
    
    return run_psscriptanalyzer(
        ps_files,
        severity=args.severity,
        exclude_rules=args.exclude_rules or []
    )


if __name__ == "__main__":
    sys.exit(main())
