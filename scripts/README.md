# Scripts

Automation scripts for the awesome-power-eval-kits repository.

## generate_kit_catalog.py

Generates markdown documentation from the YAML kit catalog and automatically updates README.md.

### What it does

1. Reads `kits/kits_catalog.yml` (master data source)
2. Generates `kits/kits_catalog.md` - comprehensive table of all kits
3. Generates `kits/kit_catalog_section.md` - categorized sections
4. **Automatically updates** `README.md` Kit Catalog section

### Requirements

```bash
pip install pyyaml
```

Or install all requirements:

```bash
pip install -r requirements.txt
```

### Usage

From the repository root:

```bash
python scripts/generate_kit_catalog.py
```

Or use the PowerShell helper script:

```powershell
.\scripts\update_catalog.ps1
```

### Output

- **kits/kits_catalog.md**: Full table with all kit details
- **kits/kit_catalog_section.md**: Categorized sections (Easy/Medium/Advanced)
- **README.md**: Kit Catalog section automatically updated

## insert_catalog.ps1

PowerShell script to manually insert the catalog section into README.md (if needed).

### Usage

```powershell
.\scripts\insert_catalog.ps1
```

**Note:** The main `generate_kit_catalog.py` script already updates README.md automatically, so this is only needed for manual fixes.

## insert_catalog_into_readme.py

Python script to manually insert the catalog section into README.md (if needed).

### Usage

```bash
python scripts/insert_catalog_into_readme.py
```

**Note:** The main `generate_kit_catalog.py` script already updates README.md automatically.

### Workflow

1. Update `kits/kits_catalog.yml` with new kits or changes
2. Run `python scripts/generate_kit_catalog.py` (or `.\scripts\update_catalog.ps1`)
3. **Done!** All files are automatically generated and README.md is updated
4. Commit all changes together

### Kit Categories

Kits are automatically categorized based on difficulty level:

- **Easy (Entry-Level)**: `Low`, `Low-Medium` difficulty
- **Medium**: `Medium`, `Medium-High` difficulty
- **Advanced / High Power**: `High` difficulty
