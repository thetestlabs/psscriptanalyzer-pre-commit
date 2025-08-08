# Example PowerShell script for testing the pre-commit hook

function Test-Example {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,

        [Parameter(Mandatory = $false)]
        [int]$Count = 1
    )

    for ($i = 1; $i -le $Count; $i++) {
        Write-Output "Hello, $Name! (Iteration $i)"
    }
}

# Call the function
Test-Example -Name "World" -Count 3
