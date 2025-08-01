# Example PowerShell script for testing PSScriptAnalyzer hook

function Test-Function {
    <#
    .SYNOPSIS
    A test function to demonstrate PSScriptAnalyzer
    
    .DESCRIPTION
    This function demonstrates various PowerShell constructs that PSScriptAnalyzer can analyze
    
    .PARAMETER Name
    The name parameter
    
    .EXAMPLE
    Test-Function -Name "Test"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    Write-Output "Hello, $Name!"
    
    # This would trigger PSAvoidUsingWriteHost if uncommented:
    # Write-Host "This is not recommended"
    
    return $Name.ToUpper()
}
