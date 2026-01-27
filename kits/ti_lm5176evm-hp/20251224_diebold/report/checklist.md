# Reverse Engineering Checklist – Power Converter Evaluation Kit Analysis

> Goal: build a **digital twin** of the evaluation board, quantify
> currents, voltages, and losses over the operating range, and compare
> your theoretical results with vendor measurements.

Fill all sections. If something is not available (e.g., you cannot
measure a parameter in the lab), **write why** and how you would do it
in a real setup.

---

## 1. Documentation & understanding

- [] Download and read:
  - [ ] Controller / driver / MOSFET datasheets
  - [x] Evaluation board user guide (schematic, BOM, test conditions)
  - [x] Any application notes referenced by the board

- [ ] Identify and write down:
  - [x] Topology (flyback, buck, buck-boost, LLC, PSFB, ...)
  - [x] Input range (Vin min / typ / max)
  - [x] Output(s): voltage, current, rated power
  - [x] Switching frequency (fixed / variable, range)
  - [ ] Critical components:
    - Main power switches (MOSFET/IGBT/GaN/SiC)
    - Magnetic components (transformer, inductors)
    - Main capacitors (input, output)
    - Snubbers / clamp networks / SR controllers

---

## 2. Simulation model (PLECS / LTspice / other)

- [x ] Rebuild the **exact topology** of the eval board:
  - [x] Use correct Vin range, Vout, switching frequency
  - [x] Use realistic models for switches (Rds_on, Qg, parasitics if possible)
  - [x] Include approximate magnetics (L, turns ratio, leakage if known)
  - [x] Include output and input capacitors, ESR where relevant

- [x] Simulate at least these operating points:
  - [x] Vin_min, full load
  - [x] Vin_nominal, full load
  - [x] Vin_max, full load
  - [x] Vin_nominal, 50% load
  - [x] Vin_nominal, light load (if controller supports it)

- [x] For each operating point, export key waveforms:
  - [x] Switch voltage (e.g. Vds)
  - [x] Switch current (Ids)
  - [x] Transformer / inductor current
  - [x] Output voltage and ripple
  - [x] Input current

- [x] For each waveform, compute:
  - [x] Average value
  - [x] RMS value
  - [x] Peak and peak-to-peak

---

## 3. Stress & margin analysis

For each critical component:

- [ ] **Semiconductors (switches, diodes, SR):**
  - [ ] Compare simulated Vmax vs. datasheet V_rating
  - [ ] Compare simulated I_RMS / I_peak vs. current ratings
  - [ ] Check junction temperature estimate (if you have thermal info)

- [ ] **Magnetics (transformer, output inductor):**
  - [ ] Compute approximate flux density (Bmax) from L, N, current ripple
  - [ ] Estimate margin to B_sat from core datasheet
  - [ ] Compute area product or Kg and compare with known design curves

- [ ] **Capacitors:**
  - [ ] Check RMS ripple current vs. capacitor rating
  - [ ] Check DC bias (for ceramics) vs. effective capacitance
  - [ ] Estimate output voltage ripple vs. datasheet limits

---

## 4. Spectral analysis

- [ ] For at least:
  - Switch node voltage
  - Inductor / transformer current
  - Output voltage ripple

do:

  - [ ] Export time-domain data from simulation
  - [ ] Compute FFT / spectrum (Python, MATLAB, etc.)
  - [ ] Identify main harmonic components and switching-related spikes
  - [ ] Comment on potential EMC implications (qualitative is fine)

---

## 5. Loss and efficiency comparison

- [ ] Estimate **loss breakdown** from simulation:
  - [ ] Conduction vs. switching losses in main switches
  - [ ] Core and copper losses in magnetics (approximate models accepted)
  - [ ] Output diode / SR losses
  - [ ] Snubber / clamp losses

- [ ] Compare with vendor data:
  - [ ] Use efficiency curves from the board user guide or datasheet
  - [ ] Use a curve digitizer if necessary
  - [ ] Plot: your simulated efficiency vs. vendor efficiency vs. load

- [ ] Discuss differences:
  - [ ] Missing parasitics? Layout effects? Measurement conditions?
  - [ ] Device models too ideal?
  - [ ] Temperature assumptions?

---

## 6. Lab measurements (if available)

If you have access to the physical board and instruments:

- [ ] Measure:
  - [ ] Efficiency vs. load for at least 3 input voltages
  - [ ] Key waveforms on the switch, magnetics, and output
  - [ ] Temperatures of main components (by IR cam or thermocouples)

- [ ] Compare measured waveforms and values with:
  - [ ] Simulation results
  - [ ] Vendor plots

If you **cannot** run lab tests, explain:
- [ ] What you would measure
- [ ] Which instruments you would use
- [ ] What accuracy and safety constraints apply

---

## 7. Conclusions & (optional) improvement proposal

- [ ] Summarize:
  - [ ] Are component stresses within safe margins?
  - [ ] Are losses consistent with vendor efficiency?
  - [ ] Is the magnetic design tight or relaxed?

- [ ] (Optional, but highly encouraged) Propose one improvement:
  - [ ] E.g. alternative MOSFET, different inductor value, snubber tweak…
  - [ ] Support it with **simulation** (before/after comparison)
  - [ ] State clearly the trade-off (efficiency vs. cost vs. volume vs. complexity)

---

## 8. Repository hygiene

- [ ] `README.md` in your project folder filled
- [ ] Simulation files in `sim/`
- [ ] Measurement data in `meas/`
- [ ] Analysis scripts in `analysis/`
- [ ] Final report (PDF or Markdown) in `report/`
- [ ] No large binary blobs in git (scope screenshots compressed) store them in the cloud if needed
