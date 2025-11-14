# <Article Title> – Reproduction Project

> Replace placeholders with actual paper info. Goal: reproduce simulations/measurements from published work.

## 1. Article Metadata

- **Title:** <Full paper title>
- **Authors:** <Author list>
- **Publication:** <e.g., IEEE Trans. Power Electronics, APEC 2024>
- **DOI / Link:** <https://doi.org/...>
- **Year:** <YYYY>
- **Keywords:** <Topology, Application, Method>

## 2. Reproduction Scope

What are you reproducing from this paper?

- [ ] Simulation model (specify tool: PLECS / LTspice / Python / Octave / etc.)
- [ ] Key waveforms from Figure(s): <list figure numbers>
- [ ] Efficiency curves
- [ ] Loss breakdown analysis
- [ ] Experimental measurements (if hardware available)
- [ ] Comparative analysis with alternative approach

**Limitations / Out of Scope:**
- <e.g., proprietary controller firmware not modeled>
- <e.g., thermal FEA not reproduced>

## 3. Paper Summary

Brief (3–5 sentence) summary of the paper's contribution:
- What topology/technique is presented?
- What problem does it solve?
- What is the claimed improvement vs. prior art?

## 4. Key Specifications from Paper

Extract design parameters directly from the paper:

| Parameter | Value | Source (Table/Figure) |
|-----------|-------|----------------------|
| Topology | <e.g., DAB, PSFB, LLC> | Section X |
| Input Voltage | <e.g., 400 V DC> | Table I |
| Output Voltage | <e.g., 48 V> | Table I |
| Rated Power | <e.g., 3 kW> | Abstract |
| Switching Frequency | <e.g., 100 kHz> | Section III |
| Efficiency Claim | <e.g., 97.5% @ full load> | Fig. 12 |
| Main Components | <e.g., SiC MOSFET C3M0065090D> | Section IV |

## 5. Reproduction Checklist

Track your progress reproducing the paper.

### Model Building
- [ ] Circuit topology built in simulation tool
- [ ] Component values match paper spec
- [ ] Control strategy implemented (e.g., phase-shift, PWM)
- [ ] Parasitic elements included (Lk, Coss, ESR where relevant)

### Waveform Validation
- [ ] Simulated waveforms match Fig. <X> qualitatively
- [ ] Peak/RMS values within ±5% of paper claims
- [ ] Switching transitions consistent with paper description

### Performance Metrics
- [ ] Efficiency curve generated
- [ ] Loss breakdown calculated (switching, conduction, magnetics)
- [ ] Comparison table: Paper vs. Reproduction

### Analysis Extensions (Optional)
- [ ] Sensitivity analysis on key parameters
- [ ] Alternative component selection explored
- [ ] Improvement proposal with simulation support

## 6. Results Comparison

| Metric | Paper Claim | Your Reproduction | Δ (%) | Notes |
|--------|-------------|-------------------|-------|-------|
| Efficiency @ Full Load | <e.g., 97.5%> | <e.g., 97.2%> | −0.3% | Good match |
| Peak Switch Voltage | <e.g., 650 V> | <e.g., 655 V> | +0.8% | Within tolerance |
| RMS Inductor Current | <e.g., 12 A> | <e.g., 12.3 A> | +2.5% | Slight model difference |

**Discrepancies Explained:**
- <e.g., Paper uses proprietary transformer model; approximated with datasheet values>
- <e.g., Deadtime not specified in paper; assumed 200 ns>

## 7. Local Artifacts

Store paper PDF, simulation files, plots in this folder.

- `./paper.pdf` – Original article (if redistribution permitted; else link only)
- `./sim/` – PLECS / LTspice / MATLAB files
- `./plots/` – Reproduced figures (PNG/SVG)
- `./data/` – Exported waveform data (CSV)
- `./analysis/` – Scripts for loss calculation, FFT, plotting
- `./report/` – Summary report (Markdown or PDF)

## 8. Simulation Tool Setup

Document what's needed to run your reproduction:

**Software:**
- <Tool name & version, e.g., PLECS 4.7, LTspice XVII>
- <Any special libraries or component models>

**Key Files:**
- `sim/main_model.plecs` – Primary circuit
- `analysis/plot_efficiency.py` – Generates efficiency curve
- `README_sim.md` – Instructions to run simulation

**Run Instructions:**
```bash
# Example for Python-based post-processing
cd analysis
python plot_efficiency.py
```

## 9. Known Challenges / Assumptions

List what you had to approximate or couldn't fully replicate:
- <e.g., Deadtime not given → assumed typical 200 ns>
- <e.g., Gate driver propagation delay unknown → used datasheet min/max>
- <e.g., Thermal model not reproduced; electrical only>

## 10. Educational Value

What did you learn from reproducing this paper?
- <e.g., Insight into ZVS transition tuning>
- <e.g., Importance of leakage inductance on efficiency>
- <e.g., Practical limits of component selection for cost vs. performance>

## 11. References

List additional papers or datasheets used:
1. <Original paper citation>
2. <Component datasheets>
3. <Related work cited by paper>

## 12. Progress Status

- [ ] Article metadata filled
- [ ] Paper summary written
- [ ] Key specs extracted
- [ ] Simulation model complete
- [ ] Waveforms reproduced
- [ ] Efficiency/loss comparison done
- [ ] Discrepancies analyzed
- [ ] Final report written
- [ ] Code & data uploaded

## 13. Revision History

| Date | Author | Change |
|------|--------|--------|
| YYYY-MM-DD | <name> | Initial template instantiation |
| YYYY-MM-DD | <name> | Added simulation results |
| YYYY-MM-DD | <name> | Finalized efficiency comparison |

---

> After completing, submit a PR with label `article-reproduction` + year tag.

