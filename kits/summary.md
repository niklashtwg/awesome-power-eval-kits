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


[
  {
    "ID": "KIT-A01",
    "Vendor": "Texas Instruments",
    "Kit Part Number": "LM5146-Q1-EVM12V",
    "Kit URL": "https://www.ti.com/lit/pdf/snvu591",
    "Topology": "Synchronous Buck",
    "Isolated": "No",
    "Vin Range": "15-85 V", 
    "Vout Range": "12 V (adjustable 8-15 V)",
    "Pout Range": "~12 V × up to ~8 A = ~96 W",
    "Control Mode": "Voltage-mode PWM (controller LM5146-Q1) :contentReference[oaicite:0]{index=0}",
    "Switching Frequency (Fs)": "400 kHz typical (synchronizable) :contentReference[oaicite:1]{index=1}",
    "Evaluation Board Number": "EVM12V",
    "Primary Semiconductor Type(s)": "Integrated MOSFETs + synchronous rectification",
    "Load Profile / Special Features": "Wide-VIN non-isolated buck for industrial/automotive rail",
    "Measurement Data Available": "Yes (user guide includes spec) :contentReference[oaicite:2]{index=2}",
    "Difficulty": "Medium",
    "Application Domain": "Industrial / Automotive",
    "Status": "",
    "Contributor": "",
    "Link to Analysis": ""
  },
  {
    "ID": "KIT-A02",
    "Vendor": "Infineon Technologies",
    "Kit Part Number": "EVAL_5BR2280BZ_700MA1",
    "Kit URL": "https://www.infineon.com/dgdl/Infineon-Engineering_Report_Evaluation_board_EVAL_5BR2280BZ_700mA1-ApplicationNotes-v01_00-EN.pdf?fileId=8ac78c8c80f4d329018189e3ae35157a3ae379d",
    "Topology": "High-Voltage Buck (non-isolated) ",
    "Isolated": "No",
    "Vin Range": "85-264 VAC input (for internals) → DC bus high voltage? (Refer doc) :contentReference[oaicite:3]{index=3}",
    "Vout Range": "15 V @ 0.7 A (~10.5 W) typical",
    "Pout Range": "~10 W",
    "Control Mode": "PWM current-mode (?) – high-voltage buck internal switch",
    "Switching Frequency (Fs)": "Need to check doc (not explicit in quick scan)",
    "Evaluation Board Number": "700mA1",
    "Primary Semiconductor Type(s)": "High-voltage MOSFET + controller",
    "Load Profile / Special Features": "Non-isolated offline buck to supply aux rails",
    "Measurement Data Available": "Yes (application note includes specs) :contentReference[oaicite:4]{index=4}",
    "Difficulty": "Low–Medium",
    "Application Domain": "Industrial / Aux supply",
    "Status": "",
    "Contributor": "",
    "Link to Analysis": ""
  },
  {
    "ID": "KIT-A03",
    "Vendor": "Analog Devices (Linear Technology)",
    "Kit Part Number": "DC2781A (LT8316 non-isolated buck demo)",
    "Kit URL": "https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/dc2781a.html",
    "Topology": "Non-isolated Buck (quasi-resonant boundary mode) ",
    "Isolated": "No",
    "Vin Range": "19–600 V DC input range :contentReference[oaicite:5]{index=5}",
    "Vout Range": "12 V @ up to 200 mA",
    "Pout Range": "~2.4 W",
    "Control Mode": "Quasi-resonant boundary mode (specialized) :contentReference[oaicite:6]{index=6}",
    "Switching Frequency (Fs)": "Not explicitly given in summary page; variable per qr mode",
    "Evaluation Board Number": "DC2781A",
    "Primary Semiconductor Type(s)": "Integrated switch + buck controller",
    "Load Profile / Special Features": "Ultra-wide input, non-isolated buck for demo applications",
    "Measurement Data Available": "Yes (demo board documents included) :contentReference[oaicite:7]{index=7}",
    "Difficulty": "Low",
    "Application Domain": "Aerospace / High-voltage industrial",
    "Status": "",
    "Contributor": "",
    "Link to Analysis": ""
  },
  {
    "ID": "KIT-A04",
    "Vendor": "ROHM",
    "Kit Part Number": "BM2P141X-EVK-001 (non-isolation buck converter) ",
    "Kit URL": "https://www.rohm.com/products/power-management/ac-dc-converters-ics/ac-dc-converters-ics-pwm-qr/bm2p141x-z-product.html",
    "Topology": "Non-isolated Buck (PWM current mode) ",
    "Isolated": "No",
    "Vin Range": "12–15 V (drain max 650 V but EVK is low power) :contentReference[oaicite:8]{index=8}",
    "Vout Range": "14 V (10 W output) :contentReference[oaicite:9]{index=9}",
    "Pout Range": "~10 W",
    "Control Mode": "PWM current-mode (per datasheet) :contentReference[oaicite:10]{index=10}",
    "Switching Frequency (Fs)": "Up to ~65 kHz indicated in spec sheet “SW frequency(Max.)[kHz] 65” :contentReference[oaicite:11]{index=11}",
    "Evaluation Board Number": "EVK-001",
    "Primary Semiconductor Type(s)": "Integrated MOSFET + controller",
    "Load Profile / Special Features": "Small non-isolated buck converter reference design",
    "Measurement Data Available": "Yes (application page) :contentReference[oaicite:12]{index=12}",
    "Difficulty": "Low",
    "Application Domain": "Embedded / Low-power aux supply",
    "Status": "",
    "Contributor": "",
    "Link to Analysis": ""
  },
  {
    "ID": "KIT-A05",
    "Vendor": "Texas Instruments",
    "Kit Part Number": "TPS55287-Q1EVM-085",
    "Kit URL": "https://www.ti.com/lit/pdf/slvucz5",
    "Topology": "Buck-boost synchronous",
    "Isolated": "No",
    "Vin Range": "3–36 V :contentReference[oaicite:13]{index=13}",
    "Vout Range": "0.8–22 V (programmable) :contentReference[oaicite:14]{index=14}",
    "Pout Range": "Up to 2 A output current (~ up to ~44 W at 22 V) :contentReference[oaicite:15]{index=15}",
    "Control Mode": "Cycle-by-cycle peak current limit, I2C programmable modes (PFM/FPWM) :contentReference[oaicite:16]{index=16}",
    "Switching Frequency (Fs)": "Default 400 kHz, programmable up to ~2.2 MHz :contentReference[oaicite:17]{index=17}",
    "Evaluation Board Number": "EVM-085",
    "Primary Semiconductor Type(s)": "Integrated MOSFETs (buck-boost) + controller",
    "Load Profile / Special Features": "Automotive USB/PD rails, flexible output, non-isolated",
    "Measurement Data Available": "Yes (user guide) :contentReference[oaicite:18]{index=18}",
    "Difficulty": "Medium",
    "Application Domain": "Automotive / USB PD / Flex power rails",
    "Status": "",
    "Contributor": "",
    "Link to Analysis": ""
  }
]
