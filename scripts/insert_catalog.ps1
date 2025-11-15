#!/usr/bin/env pwsh
# Insert kit catalog section into README.md
# This script replaces the Kit Catalog section in README with the generated content

$ErrorActionPreference = "Stop"

$catalogSection = "kits\kit_catalog_section.md"
$readme = "README.md"

if (-not (Test-Path $catalogSection)) {
    Write-Host "Error: $catalogSection not found" -ForegroundColor Red
    Write-Host "Run generate_kit_catalog.py first" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path $readme)) {
    Write-Host "Error: $readme not found" -ForegroundColor Red
    exit 1
}

Write-Host "Reading catalog section from: $catalogSection" -ForegroundColor Cyan

# Read the catalog section content
$catalogContent = Get-Content $catalogSection -Raw

# Read README
$readmeContent = Get-Content $readme -Raw

# Define the regex pattern to match the Kit Catalog section
# Match from "## Kit Catalog" to the next "---" or "##"
$pattern = '(?s)(---\s*\n\s*)## Kit Catalog.*?(?=\n---|$)'

# Create the replacement
$replacement = "`$1$catalogContent`n`n"

# Perform the replacement
$newContent = $readmeContent -replace $pattern, $replacement

if ($newContent -eq $readmeContent) {
    Write-Host "Warning: No changes made. Kit Catalog section may not have been found." -ForegroundColor Yellow
    exit 1
}

# Write back to README
Set-Content -Path $readme -Value $newContent -NoNewline

Write-Host "✓ Successfully updated Kit Catalog section in $readme" -ForegroundColor Green
