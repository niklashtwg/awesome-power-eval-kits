# <KIT NAME> Evaluation Board

> Replace placeholders thoroughly. Keep sections even if info is TBD; mark unknowns clearly.

## 1. Quick Summary

- **Topology:** <e.g., QR Flyback, Synchronous Buck, LLC Half-Bridge>
- **Nominal Power / Output(s):** <e.g., 19 V @ 3.42 A (65 W)>
- **Input Range:** <e.g., 90–264 VAC / 36–57 V PoE>
- **Target Use Case:** <e.g., USB-C PD adapter, Telecom isolated DC/DC>
- **Primary Learning Themes:** <e.g., Primary-side regulation / GaN switching / PD negotiation>

## 2. Official Documentation Links

List only authoritative vendor sources.

| Type | Link | Notes |
|------|------|-------|
| Product Page | <URL> | Overview & ordering |
| User Guide / Eval Manual | <URL> | Schematics, BOM, test setup |
| Main Controller Datasheet | <URL> | PWM / regulation IC |
| Power Switch Datasheet | <URL> | MOSFET / GaN / SiC |
| Secondary Controller / SR | <URL> | (If applicable) |
| Application Note | <URL> | (Optional) |

## 3. Local Artifacts (Stored in This Folder)

Place small, text or PDF artifacts directly in this kit folder (avoid huge binaries). Add links once files are added.

- `./schematic.pdf` – Board schematic (if license permits)
- `./bom.csv` – Bill of materials
- `./layout.png` – PCB top/bottom render
- `./efficiency_curve.png` – Vendor efficiency plot
- `./datasheet_controller.pdf` – Controller IC datasheet
- `./datasheet_switch.pdf` – MOSFET/GaN device datasheet

> If redistribution is not allowed, link externally instead of storing the file.

## 4. Electrical Characteristics

| Parameter | Min | Typ | Max | Notes |
|-----------|-----|-----|-----|-------|
| Input Voltage | < > | < > | < > | |
| Output Voltage(s) | < > | < > | < > | List rails / PD profiles |
| Rated Output Power | — | < > | — | Continuous |
| Switching Frequency | < > | variable? | < > | Include modulation method |
| Efficiency | — | < >% | — | At full load, nominal input |
| Isolation | Yes/No | — | — | If isolated topology |

## 5. Key Components

| RefDes / Part | Function | Key Specs / Reasons |
|---------------|----------|---------------------|
| <U1, Part No> | Controller | PSR, valley switching, etc. |
| <Q1, Part No> | Primary switch | Rds_on, Vds rating |
| <T1/L1> | Transformer / Inductor | Inductance, turns ratio |
| <D1 / SR IC> | Rectification | Diode Vf / SR control |
| <Cout> | Output cap bank | ESR, ripple current |
| <Cin> | Input bulk cap | Hold-up / EMI |
| <Snubber parts> | Clamp network | Limits Vds overshoot |

## 6. Block Diagram / Topology Notes

Add an ASCII sketch or embed an image (`./topology.png`).

```
[Input] -- EMI -- [Primary Switch + Controller] -- [XFMR] -- [SR / Diode] -- [Output Regulation / PD]
```

Summarize any special modes (burst, valley, frequency foldback, synchronous rectification strategy, etc.).

## 7. Educational Focus / Suggested Student Tasks

Students working on this kit should aim to:

1. Recreate topology in simulation (PLECS / LTspice) with realistic parasitics.
2. Sweep operating points: Vin min/typ/max × load levels.
3. Extract waveforms: primary current, switch voltage, magnetics current, output ripple.
4. Perform stress analysis vs. datasheet limits (voltage, current, temperature).
5. FFT spectral analysis of switch node & output ripple (EMC discussion).
6. Loss breakdown (switching vs. conduction, core vs. copper, diode/SR, clamp).
7. Efficiency comparison vs. vendor curve & explain discrepancies.
8. Propose at least one design improvement and simulate impact.

Reference master checklist: [`templates/STUDENT_CHECKLIST.md`](../../templates/STUDENT_CHECKLIST.md)

## 8. Project / Analysis Progress Status

Use these checkboxes to track onboarding and student project completion phases.

### Kit Onboarding (Maintainer)
- [ ] Links verified (no 404s)
- [ ] Core datasheets present or externally linked
- [ ] BOM stub added
- [ ] Efficiency or performance plot available
- [ ] Schematic accessible (linked or local)

### Student Project (Per Group) — Mirror from checklist
- [ ] Topology + input/output specs documented
- [ ] Simulation model builds & runs
- [ ] Operating point sweep results exported
- [ ] Stress margins table compiled
- [ ] Spectral analysis (FFT) performed
- [ ] Loss breakdown estimated
- [ ] Efficiency comparison plotted
- [ ] Improvement proposal with before/after data
- [ ] Final report placed in `report/`
- [ ] README updated with summary & key findings

> Consider copying this section into the group's `README.md` and updating progress there.

## 9. Known Challenges / Caveats

List early pitfalls (e.g., difficult to model transformer leakage; proprietary PD firmware; EMI filter details missing).

- <Example: Transformer datasheet unavailable — approximate leakage inductance from ringing frequency>
- <Example: PD negotiation timings hidden — treat as black box>

## 10. Data & Measurement Suggestions

If lab access is available, suggest measurement priorities:

| Measurement | Instrument | Purpose | Notes |
|-------------|-----------|---------|-------|
| Efficiency vs. Load | Power analyzer / DMM pair | Validate loss model | Control temperature |
| Primary current waveform | Current probe + scope | Peak/RMS validation | Watch saturation near Vin_max |
| Output ripple | Scope (AC coupled) | Capacitor ESR assessment | Use proper bandwidth limit |
| Thermal hotspots | IR camera / thermocouples | Junction temp estimate | Steady-state after 10–15 min |

## 11. Improvement Ideas (Brainstorm Parking Lot)

Capture raw ideas before selecting one to analyze:
- Replace primary MOSFET with lower Qg part
- Optimize snubber network to reduce switching loss
- Adjust transformer turns ratio for better light-load efficiency
- Move to synchronous rectification (if currently diode)

## 12. Revision History

| Date | Author | Change |
|------|--------|--------|
| YYYY-MM-DD | <name> | Initial template instantiation |
| YYYY-MM-DD | <name> | Added local artifact links |
| YYYY-MM-DD | <name> | Updated electrical characteristics |

---

> After populating this template, remove instructional quotes and placeholder brackets `<like this>`.

