# TI TPS62932EVM Synchronous Buck Converter Evaluation Module

> Non-isolated, high-efficiency synchronous buck stage for embedded rails. Wide 3.8–30 V input, ~10 W class output.

## 1. Quick Summary

- **Topology:** Non-isolated synchronous buck (step-down)
- **Nominal Power / Output(s):** ~10 W class, typical rails 3.3 V / 5 V @ ~2 A
- **Input Range:** 3.8–30 V DC (wide VIN)
- **Target Use Case:** Point-of-load (POL) supply for digital logic, MCUs, sensors, and small embedded systems
- **Primary Learning Themes:** High-frequency synchronous buck design, efficiency optimization, compensation and stability, layout & EMI for fast switching

## 2. Official Documentation Links

List only authoritative vendor sources.

| Type | Link | Notes |
|------|------|-------|
| Product Page | https://www.ti.com/tool/TPS62932EVM | Board overview & ordering |
| User Guide / Eval Manual | https://www.ti.com/lit/pdf/snvu572 | Schematics, BOM, test setup, performance curves |
| Main Controller Datasheet | https://www.ti.com/lit/ds/symlink/tps62932.pdf | TPS62932 synchronous buck converter IC |
| Power Switch Datasheet | Integrated MOSFETs in TPS62932 | High-side/low-side FETs are inside controller |
| Secondary Controller / SR | n/a | Non-isolated single-stage buck |
| Application Note | See links on product page | Design tips, layout and EMI guidance |

## 3. Local Artifacts (Stored in This Folder)

Place small, text or PDF artifacts directly in this kit folder (avoid huge binaries). Add links once files are added.

- Board schematic: https://www.ti.com/lit/ug/slvuby1/slvuby1.pdf?ts=1763061645574
- Bill of materials: https://www.ti.com/lit/ug/slvuby1/slvuby1.pdf?ts=1763061645574
- PCB top/bottom render: https://www.ti.com/lit/ug/slvuby1/slvuby1.pdf?ts=1763061645574
- Vendor efficiency plot: not available
- Controller IC datasheet: https://www.ti.com/lit/ds/symlink/tps62932.pdf

> If redistribution is not allowed, link externally instead of storing the file.

## 4. Electrical Characteristics

> Values below are indicative; always confirm exact limits and test conditions from the user guide and datasheet.

| Parameter | Min | Typ | Max | Notes |
|-----------|-----|-----|-----|-------|
| Input Voltage | 3.8 V | 12 V | 30 V | Wide VIN DC input |
| Output Voltage(s) | configurable | 3.3 / 5.0 V | configurable | Set by feedback network; see user guide |
| Rated Output Power | - | ~10 W | - | Depends on Vout and cooling |
| Switching Frequency | - | see datasheet | - | Fixed / quasi-fixed, controller-defined |
| Efficiency | - | >90% (typ) | - | At nominal VIN and load, per curves |
| Isolation | No | - | - | Non-isolated buck topology |

## 5. Key Components

| RefDes / Part | Function | Key Specs / Reasons |
|---------------|----------|---------------------|
| U1 – TPS62932 | Synchronous buck controller + integrated FETs | Wide-VIN, integrated high/low-side MOSFETs, current-mode control, high efficiency |
| L1 – Output inductor | Energy storage / ripple shaping | Inductance chosen for desired ripple at max load and switching frequency; check saturation current margin |
| Cin – Input capacitors | Input decoupling and surge handling | Low-ESR ceramic/bulk caps to limit VIN ripple and switch current slew into the IC |
| Cout – Output capacitor bank | Output ripple and transient response | Combination of ceramics / bulk caps; ESR and total C dominate ripple and load-step behavior |
| Rfb network | Feedback / output setpoint | Sets Vout; also impacts loop gain and noise susceptibility |
| Snubber / damping network (if present) | Switch node ringing control | Damps SW-node ringing for lower EMI and more accurate stress estimates |

## 6. Block Diagram / Topology Notes

Simple non-isolated synchronous buck power stage:
```tikz
\begin{tikzpicture}[>=latex, thick, node distance=2cm]
  % Input and controller
  \node[draw, rectangle, fill=gray!10] (vin) {VIN};
  \node[draw, rectangle, fill=blue!5, right=of vin] (ic) {TPS62932\\Buck Controller};

  % Power path
  \node[draw, rectangle, fill=green!5, right=of ic] (l) {L1};
  \node[draw, rectangle, fill=yellow!10, right=of l] (cout) {C\_out};
  \node[right=1.5cm of cout] (vout) {V\_OUT};

  \draw[->] (vin) -- node[above]{VIN} (ic);
  \draw[->] (ic) -- node[above]{SW} (l);
  \draw[->] (l) -- (cout);
  \draw[->] (cout) -- (vout);

  % Input capacitor
  \node[draw, rectangle, fill=yellow!10, below=1.2cm of vin] (cin) {C\_in};
  \node[below=0.8cm of cin] (gnd1) {GND};
  \draw (vin.south) -- (cin.north);
  \draw (cin.south) -- (gnd1.north);

  % Feedback network
  \node[draw, rectangle, fill=orange!10, below=1.2cm of ic] (fb) {R\_fb network};
  \draw[->] (vout |- fb) -- node[right]{V\_OUT sense} (fb.east);
  \draw[->] (fb.north) -- (ic.south);
\end{tikzpicture}
```


Notes:
- Non-isolated step-down from a relatively high VIN to logic-level rails.
- Synchronous rectification (low-side FET) enables high efficiency at low VOUT.
- Fast switching edges and high di/dt on the SW node make layout and loop area minimization critical.

## 7. Educational Focus / Suggested Student Tasks

Students working on this kit should aim to:

1. Recreate the synchronous buck topology in simulation (PLECS / LTspice) with realistic parasitics on the inductor, MOSFETs, and capacitors.
2. Sweep operating points across VIN (3.8 V / mid-range / 30 V) and load (light, 50%, full load).
3. Extract waveforms for SW node, inductor current, input current, and VOUT ripple and compute average, RMS, and peak values.
4. Perform stress analysis on U1 (internal FETs), L1, Cin, and Cout versus their voltage, current, and temperature ratings.
5. Perform spectral (FFT) analysis of the SW node and output ripple to discuss EMI implications and how layout or filtering affects them.
6. Build a loss breakdown (inductor copper/core loss, MOSFET conduction/switching loss, capacitor ESR loss) and compare with vendor efficiency curves.
7. Propose at least one design improvement (e.g., alternative inductor, different Cout mix, altered switching conditions) and simulate the impact on efficiency and transient response.

Reference master checklist: `templates/STUDENT_CHECKLIST.md`.

## 8. Project / Analysis Progress Status

Use these checkboxes to track onboarding and student project completion phases.

### Kit Onboarding (Maintainer)
- [ ] Links verified (no 404s)
- [ ] Core datasheets present or externally linked
- [ ] BOM stub added
- [ ] Efficiency or performance plot available
- [ ] Schematic accessible (linked or local)

### Student Project (Per Group) - Mirror from checklist
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

## 9. Known Challenges / Caveats

- High switching frequency and fast edges make PCB layout and ground return paths critical for realistic modeling and EMI behavior.
- Exact inductor and capacitor parasitics (ESR, ESL, DCR) may not be fully documented; you may need to approximate or back-calculate from measurements.
- Thermal behavior of the small IC package and inductor can be difficult to predict accurately without detailed thermal data.

## 10. Data & Measurement Suggestions

If lab access is available, suggested priorities:

| Measurement | Instrument | Purpose | Notes |
|-------------|-----------|---------|-------|
| Efficiency vs. Load | Power analyzer / DMM pair | Validate loss model and datasheet curves | Sweep VIN and load; control temperature |
| Inductor current waveform | Current probe + scope | Validate inductor sizing and saturation margin | Check ripple and peak current at VIN max |
| SW node voltage | High-bandwidth probe + scope | Observe ringing and overshoot | Use proper probing (short ground lead / coax tip) |
| Output ripple | Scope (AC coupled) | Assess Cout network and ESR | Apply bandwidth limit to avoid noise overestimation |
| Thermal hotspots | IR camera / thermocouples | Estimate IC and inductor temperatures | Take data at steady-state full load |

## 11. Improvement Ideas (Brainstorm Parking Lot)

Capture raw ideas before selecting one to analyze:
- Try alternative inductors (different DCR / core material) to trade off efficiency vs. transient response and size.
- Optimize output capacitor mix (ceramic vs. bulk) for lower ripple while keeping good load transient behavior.
- Tune snubber or damping network (if present) to reduce SW-node overshoot and EMI.
- Explore operation at different VIN ranges and loads to understand efficiency sweet spots.

## 12. Revision History

| Date | Author | Change |
|------|--------|--------|
| 2025-11-14 | gpt-5.1 (assistant) | Initial TPS62932EVM kit README instantiation |


---

After populating this template further with concrete measured/simulated data, maintainers can refine characteristic tables, add local artifacts, and update the progress status.
