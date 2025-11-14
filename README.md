# Awesome Power Eval Kits

A curated collection of power electronics evaluation kits, student projects, and academic paper reproductions—with simulations, measurements, and digital twin models.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Three Content Types](#three-content-types)
- [Getting Started](#getting-started)
- [Workflow for Students](#workflow-for-students)
- [Kit Catalog](#kit-catalog)
- [Contributing](#contributing)

## Overview

This repository is a **learning museum** for power electronics:
- **Kits**: Reverse-engineering of real evaluation boards (hardware-based)
- **Projects**: Original student designs and proposals (concept/simulation-based)
- **Articles**: Reproduction of published IEEE/journal papers

**Educational Goals:**
- Build digital twin models in PLECS/LTspice/MATLAB
- Quantify currents, voltages, losses, and component stresses
- Compare simulation results with vendor data or published results
- Perform spectral analysis, efficiency measurements, and margin checks
- Propose evidence-based design improvements

## Repository Structure

```
awesome-power-eval-kits/
├─ README.md                        # This file
├─ kits/                            # Real eval boards (vendor hardware)
│  ├─ ti_ucc28740evm_525/
│     ├─ README.md                  # Board specs, datasheet links
│     ├─  docs/                    # Additional documentation (optional)
│     │  ├─ schematic.pdf              # (optional, if distributable)
│     │  ├─ bom.csv                    # Bill of materials
│     │  ├─ efficiency_curve.png       # Vendor plots
│     └─ 20250115_group_alpha/      # Student analysis (YYYYMMDD_name)
│        ├─ README.md
│        ├─ sim/
│        ├─ meas/
│        ├─ analysis/
│        └─ report/
├─ projects/                        # Student original designs/proposals
│  ├─ 20250120_bidirectional_dcdc_sic/  # YYYYMMDD_project_name
│  │  ├─ README.md                  # Project summary
│  │  ├─ sim/                       # Simulation files
│  │  ├─ analysis/                  # Scripts, Jupyter notebooks
│  │  └─ report/                    # Final PDF/Markdown report
│  └─ 20250210_llc_resonant_charger/
│     └─ README.md
├─ articles/                        # IEEE/journal paper reproductions
│  ├─ 20250115_smith2023_gan_totem_pfc/  # YYYYMMDD_author_year_topic
│  │  ├─ README.md                  # Paper metadata, reproduction scope
│  │  ├─ paper.pdf                  # (if allowed) or link
│  │  ├─ sim/                       # Replicated model
│  │  ├─ plots/                     # Reproduced figures
│  │  └─ report/                    # Comparison & analysis
│  └─ 20250201_lee2022_totem_pfc/
│     └─ README.md
├─ templates/                       # Starter templates
│  ├─ STUDENT_CHECKLIST.md          # Analysis checklist (for kits)
│  ├─ KIT_README_TEMPLATE.md        # Template for kits/
│  ├─ PROJECT_README_TEMPLATE.md    # Template for projects/
│  ├─ ARTICLE_README_TEMPLATE.md    # Template for articles/
│  └─ REPORT_TEMPLATE.md            # General report structure
└─ .github/
   └─ PULL_REQUEST_TEMPLATE.md
```

## Three Content Types

### 1. `kits/` – Real Evaluation Boards

**What:** Reverse-engineering of **existing vendor hardware** (TI, ST, Infineon, etc.).

**Structure:** Each kit folder uses the same template as the board itself:
- `README.md` with specs, datasheet links, component list
- Optionally: schematics, BOM, efficiency plots (stored locally or linked)
- Student analysis folders **inside the kit folder** with naming: `YYYYMMDD_groupname/`
  - Example: `kits/ti_ucc28740evm_525/20250115_group_alpha/`

**Template:** [`templates/KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md)

### 2. `projects/` – Student Original Designs

**What:** **Student-proposed converters** not tied to a specific eval board. These are original designs, thesis projects, or hypothetical topologies.

**Naming Convention:** `YYYYMMDD_project_description/`
- Example: `projects/20250120_bidirectional_dcdc_sic/`
- Example: `projects/20250315_llc_resonant_ev_charger/`

**Examples:**
- Bidirectional DC/DC with SiC for energy storage
- Custom LLC resonant charger for EVs
- Multi-phase buck for server VRM

**Template:** [`templates/PROJECT_README_TEMPLATE.md`](templates/PROJECT_README_TEMPLATE.md)

### 3. `articles/` – Academic Paper Reproductions

**What:** **Reproduction of published work** from IEEE, APEC, ECCE, journals, etc. Goal: replicate simulations, validate claims, understand techniques.

**Naming Convention:** `YYYYMMDD_firstauthor_year_topic/`
- Example: `articles/20250115_smith_2023_gan_totem_pfc/`
- Example: `articles/20250201_lee_2022_llc_zerocurrent/`

**Template:** [`templates/ARTICLE_README_TEMPLATE.md`](templates/ARTICLE_README_TEMPLATE.md)

---

---

## Getting Started

### For Instructors

**Adding content:**
1. **Kits:** Create folder in `kits/` using [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md)
2. **Projects:** Direct students to `projects/YYYY/` with appropriate template
3. **Articles:** Use [`ARTICLE_README_TEMPLATE.md`](templates/ARTICLE_README_TEMPLATE.md) for paper reproductions

**Managing submissions:** Review PRs, check completeness via checklist, merge to main, apply labels.

### For Students

Pick your activity type and follow the corresponding workflow below.

## Workflow for Students

We use a **fork-based workflow**. All work happens in your fork; submit a PR when complete.

### Common Steps (All Types)

1. **Fork** this repository (click Fork button on GitHub)
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/awesome-power-eval-kits.git
   cd awesome-power-eval-kits
   ```

### Type A: Analyzing a Real Eval Board (`kits/`)

3. Navigate to the kit folder (e.g., `kits/ti_ucc28740evm_525/`)
4. Read the kit `README.md` and linked datasheets
5. Create your analysis folder **inside the kit folder** using `YYYYMMDD_groupname`:
   ```bash
   cd kits/ti_ucc28740evm_525
   mkdir 20250115_group_alpha
   cd 20250115_group_alpha
   ```
6. Copy templates:
   ```bash
   cp ../../../templates/PROJECT_README_TEMPLATE.md README.md
   ```
7. Build your simulation model, follow [`STUDENT_CHECKLIST.md`](templates/STUDENT_CHECKLIST.md)
8. Structure your work:
   ```
   20250115_group_alpha/
   ├─ README.md
   ├─ sim/          # PLECS, LTspice
   ├─ meas/         # CSV, scope data
   ├─ analysis/     # Scripts
   └─ report/       # Final PDF/Markdown
   ```

### Type B: Original Student Project (`projects/`)

3. Create a project folder with `YYYYMMDD_description` naming:
   ```bash
   cd projects
   mkdir 20250120_bidirectional_dcdc_sic
   cd 20250120_bidirectional_dcdc_sic
   ```
4. Copy template:
   ```bash
   cp ../../templates/PROJECT_README_TEMPLATE.md README.md
   ```
5. Develop your design, simulation, and analysis

### Type C: Paper Reproduction (`articles/`)

3. Create article folder using `YYYYMMDD_author_year_topic` naming:
   ```bash
   cd articles
   mkdir 20250115_smith_2023_gan_totem_pfc
   cd 20250115_smith_2023_gan_totem_pfc
   ```
4. Copy template:
   ```bash
   cp ../../templates/ARTICLE_README_TEMPLATE.md README.md
   ```
5. Reproduce simulations/measurements from the paper
6. Document discrepancies and lessons learned

### Final Steps (All Types)

9. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add [kit/project/article]: YYYYMMDD_description"
   git push origin main
   ```

10. **Open Pull Request:**
    - Go to your fork on GitHub
    - Click **Pull Request** → **New Pull Request**
    - Base: `tinix84/awesome-power-eval-kits` (main)
    - Head: `YOUR-USERNAME/awesome-power-eval-kits` (main)
    - Fill PR template, add labels: `kit-xxx` / `project` / `article-reproduction`

**Important:**
- No large binaries (>10 MB). Use compressed images (PNG/JPG).
- Export scope data as CSV.
- Follow the appropriate checklist/template.

---

## Kit Catalog

Browse available evaluation boards in `kits/`. Entries with links have detailed documentation.

### Easy (Entry-Level)

Non-isolated DC/DC and low-power offline boards.

- **TI TPS62932EVM** · synchronous buck, 3.8–30 V in, ~10 W  
- **TI TPS563212EVM** · synchronous buck, 4.2–18 V in, 3.3 V / 3 A  
- **TI TPS6213xEVM** · synchronous buck, 3–17 V in, 3.3 / 5 V @ 3–4 A  
- **ST STEVAL-VP12201F** · 5 W flyback offline, 85–265 VAC → 12 V  
- **onsemi NCP1060FLBKGEVB** · universal-mains flyback, ~7 W  
- **ROHM BD7F100EFJ-EVK-001** · 24 V → 5 V isolated flyback  
- **Adafruit Verter 5V USB Buck-Boost (2190)** · 3–12 V → 5 V USB

### Medium

Intermediate power, more complex control or wide-VIN.

- **[TI TPS23753AEVM-004](kits/ti_tps23753aevm_004/)** · PoE flyback PD board  
- **[TI UCC28740EVM-525](kits/ti_ucc28740evm_525/)** · 65 W offline flyback with PSR  
- **TI LM5118EVAL** · wide-VIN buck-boost (5–75 V)  
- **TI LM5576EVAL** · 6–75 V buck  
- **ST STEVAL-ISA201V1** · L5987 buck evaluation board  
- **ST STEVAL-QUADV01** · quad-power tree demo  
- **Infineon EVAL_5BR2280BZ_700MA1** · 10.5 W HV buck offline  
- **Skyworks/Silabs Si34061** · 12 V PoE isolated flyback PD  
- **MPS EVQ3369-R-01A** · multi-channel LED boost driver

### Advanced / High Power

kW-class boards with complex topologies (LLC, PSFB, bidirectional, PFC+LLC).

- **[ST EVLSTACF01-65WU](kits/st_evlstacf01_65wu/)** · 65 W USB-C PD adapter with GaN  
- **ST STEVAL-DPSLLCK1** · 3 kW LLC full-bridge DC/DC  
- **Infineon EVAL_3KW_50V_PSU** · PFC + LLC 3 kW telecom PSU  
- **Infineon REF-1KW-PSU-5G-SIC** · SiC totem-pole PFC + LLC 1 kW  
- **Infineon EVAL_1K6W_PSU_CFD7_QD** · 1.6 kW server PSU reference  
- **Infineon EVAL_3K3W_BIDI_PSFB** · 3.3 kW bidirectional PSFB  
- **TI LMG1210EVM-012** · GaN half-bridge stage demo

> **Note:** Not all kits have folders yet. Contributions welcome! Use [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md) to add one.

---

## Contributing

### Content Types

1. **Kits (`kits/`)** – Add new eval boards with docs and specs
2. **Projects (`projects/`)** – Submit original student designs
3. **Articles (`articles/`)** – Reproduce published papers

### Submission Guidelines

**Before submitting a PR:**
- [ ] Use the appropriate template (`KIT_README_TEMPLATE.md`, `PROJECT_README_TEMPLATE.md`, or `ARTICLE_README_TEMPLATE.md`)
- [ ] Complete all required sections (no placeholder `<text>` left)
- [ ] Follow checklist: [`STUDENT_CHECKLIST.md`](templates/STUDENT_CHECKLIST.md) for kits
- [ ] Simulation model included and functional
- [ ] No large binaries (>10 MB); use links or compressed files
- [ ] Analysis/report section complete with conclusions

**PR Process:**
1. Fork → create branch → commit changes
2. Open PR to `tinix84/awesome-power-eval-kits:main`
3. Fill out PR template
4. Add labels:
   - Type: `kit`, `project`, `article-reproduction`
   - Kit (if applicable): `kit-ti-ucc28740`, `kit-st-evlstacf01`
   - Topic: `topic-efficiency`, `topic-magnetics`, `topic-emi`

**Rejection Criteria:**

PRs lacking the following will be politely rejected:
- Working simulation model
- Basic loss breakdown or efficiency analysis
- Written conclusions (even if brief)

### Improving Templates

Found a better way to structure reports? Submit a PR to `templates/` with explanation.

---

## License

This repository is for **educational purposes**. 

- Student submissions: work of respective authors
- Vendor documentation: property of manufacturers (linked for reference)
- Reproduced papers: cite original authors and DOI

---

**Maintainer:** [tinix84](https://github.com/tinix84)  
**Questions?** Open an issue or contact the course instructor.
