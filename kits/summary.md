| # | Vendor | Kit (link) | Topology | Isolated | Vin (typical) | Vout (typical) | Power ≈ [W] | Difficulty | Application domain |
|---|--------|------------|----------|----------|---------------|----------------|-------------|------------|--------------------|
| 1 | TI | [TPS23753AEVM-004](https://www.ti.com/tool/TPS23753AEVM-004) | PoE flyback | Yes | PoE / adapter, ~37–57 V | 3.3 / 5 / 12 V (configurable) | ~10 | Medium | Telecom / networking (PoE PD) |
| 2 | TI | [UCC28740EVM-525](https://www.ti.com/tool/UCC28740EVM-525) | Flyback DCM | Yes | 85–265 VAC | 5 V @ 2.1 A | 10 | Medium | Offline charger / adapter |
| 3 | TI | [LM5118EVAL](https://www.ti.com/tool/LM5118EVAL) | Buck–boost | No | 5–75 V | 12 V @ 3 A | ~36 | Medium | Automotive / industrial wide-VIN |
| 4 | TI | [LM5176EVM-HP](https://www.ti.com/tool/LM5176EVM-HP) | Buck–boost synchronous | No | 6–36 V | 12 V @ 12 A | ~144 | Medium–High | Automotive 12/24/48 V bus |
| 5 | TI | [TPS62932EVM](https://www.ti.com/tool/TPS62932EVM) | Buck synchronous | No | 3.8–30 V | 3.3 / 5 V @ ~2 A | ~10 | Low | POL for digital / embedded |
| 6 | TI | [TPS563212EVM](https://www.mouser.com/ProductDetail/Texas-Instruments/TPS563212EVM) | Buck synchronous | No | 4.2–18 V | 3.3 V @ 3 A | ~10 | Low | Small aux supply / logic rails |
| 7 | TI | [TPS6213xEVM](https://www.ti.com/lit/pdf/slvuai7) | Buck synchronous | No | 3–17 V | 3.3 / 5 V @ 3–4 A | ~15 | Low | POL for FPGA / CPU |
| 8 | TI | [LM5576EVAL](https://www.ti.com/tool/LM5576EVAL) | Buck | No | 6–75 V | e.g. 5 V @ 3 A | ~15 | Medium | Industrial / telecom front-end |
| 9 | ST | [EVLSTACF01-65WU](https://www.st.com/en/evaluation-tools/evlstacf01-65wu.html) | Active-clamp flyback (ACF) | Yes | 90–264 VAC | 5–20 V (USB-PD) | 65 | Medium–High | USB-PD / high-density charger |
|10 | ST | [STEVAL-VP12201F](https://www.st.com/en/evaluation-tools/steval-vp12201f.html) | Flyback | Yes | 85–265 VAC | 12 V @ 5 W | 5 | Low | Small offline SMPS |
|11 | ST | [STEVAL-ISA201V1](https://www.mouser.com/ProductDetail/STMicroelectronics/STEVAL-ISA201V1) | Buck (L5987) | No | up to ~24–25 V | e.g. 5 V @ 3 A | ~15 | Low | Industrial / automotive (non-isolated) |
|12 | ST | [STEVAL-QUADV01](https://www.st.com/en/evaluation-tools/steval-quadv01.html) | Multi-output buck + LDO | No | 3.5–38 / 60 V | multiple rails (A, B, C, LDO) | ~10–20 | Medium | Power tree for digital / industrial |
|13 | ST | [STEVAL-DPSLLCK1](https://www.st.com/en/evaluation-tools/steval-dpsllck1.html) | LLC full-bridge | Yes | DC bus ~350–400 V | e.g. 3 kW @ low-V | 3000 | High | Server / EV isolated DC-DC |
|14 | onsemi | [NCP1060FLBKGEVB](https://www.digikey.com/en/products/detail/onsemi/NCP1060FLBKGEVB/5892476) | Flyback | Yes | 85–265 VAC | 12 V @ 0.6 A | ~7 | Low | Utility meter / low-power offline |
|15 | onsemi | [NCP1076FLBKGEVB](https://www.we-online.com/en/components/icref/onsemi/NCP1076B-NCP1076FLBKGEVB-Flyback) | Flyback | Yes | 85–265 VAC | 12 V @ 1.2 A | ~18 | Low–Med | Industrial aux supply |
|16 | Infineon | [EVAL_5BR2280BZ_700MA1](https://www.mouser.com/ProductDetail/Infineon-Technologies/EVAL5BR2280BZ700MA1TOBO1) | High-voltage buck | No | 85–264 VAC | 15 V @ 0.7 A | 10.5 | Medium | Aux supply for SMPS / drives |
|17 | Infineon | [EVAL_3KW_50V_PSU](https://www.infineon.com/evaluation-board/EVAL-3KW-50V-PSU) | PFC + LLC | Yes | 178–275 VAC | 50 V DC | 3000 | High | Server / telecom rectifier |
|18 | Infineon | [REF-1KW-PSU-5G-SIC](https://www.infineon.com/evaluation-board/REF-1KW-PSU-5G-SIC) | Totem-pole PFC + HB-LLC | Yes | mains AC | ~48–54 V | 1000 | High | 5G / telecom PSU |
|19 | Infineon | [EVAL_1K6W_PSU_CFD7_QD](https://www.infineon.com/evaluation-board/EVAL-1K6W-PSU-CFD7-QD) | PFC + LLC | Yes | mains AC | 12 / 48 V | 1600 | High | Server titanium PSU |
|20 | Infineon | [EVAL_3K3W_BIDI_PSFB](https://www.infineon.com/evaluation-board/EVAL-3K3W-BIDI-PSFB) | Bidirectional PSFB | Yes | HV bus ↔ 54 V | 3300 | High | BESS, telecom, battery testing |
|21 | ROHM | [BD7F100EFJ-EVK-001](https://www.rohm.com/reference-designs/refflbk001) | Flyback | Yes | 24 V DC | 5 V @ 0.8 A | 4 | Low–Med | Isolated aux for industrial / medical instruments |
|22 | Skyworks / Silicon Labs | [Si34061 Isolated Flyback 12 V PoE Kit](https://www.skyworksinc.com/en/Products/Power/Evaluation-Kits/si34061-isolated-flyback-12v-class-4-evaluation-kit) | PoE flyback | Yes | PoE 37–57 V | 12 V | ~25–30 | Medium | Industrial PoE (automation, control) |
|23 | Adafruit | [Verter 5 V USB Buck-Boost – 2190](https://www.adafruit.com/product/2190) | Buck–boost | No | 3–12 V | 5 V USB | 2.5–5 | Low | Maker / embedded gadgets |
|24 | MPS | [EVQ3369-R-01A](https://www.monolithicpower.com/en/evq3369-r-01a.html) | Boost LED driver | No | ~4.5–36 V | LED strings (multi-channel) | ~10–20 | Medium | Lighting / display backlight |
|25 | TI | [LMG1210EVM-012](https://www.ti.com/lit/pdf/snvu572) | Half-bridge GaN stage | No | up to ~300 V DC bus | configurable | 10–100+ (by design) | High | Advanced half-bridge / GaN switching lab |
