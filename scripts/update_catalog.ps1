#!/usr/bin/env pwsh
# Update kit catalog from YAML
# Usage: .\scripts\update_catalog.ps1

Write-Host "Updating kit catalog from YAML..." -ForegroundColor Cyan

python scripts/generate_kit_catalog.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nSuccess! Generated and updated:" -ForegroundColor Green
    Write-Host "  ✓ kits/kits_catalog.md (complete table)" -ForegroundColor Gray
    Write-Host "  ✓ kits/kit_catalog_section.md (section content)" -ForegroundColor Gray
    Write-Host "  ✓ README.md (Kit Catalog section)" -ForegroundColor Gray
    Write-Host "`nKit catalog is up to date!" -ForegroundColor Green
} else {
    Write-Host "`nError: Script failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}
