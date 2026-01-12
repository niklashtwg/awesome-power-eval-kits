# report
Kit URL: "https://www.ti.com/tool/LM5176EVM-HP"

# 1. Documentation & Understanding

[LM5176EVM-HP User Guide + BOM](../docs/snvu547.pdf) 

[LM5176 (Logic) User Guide + BOM](../docs/lm5176.pdf)

## 1.1 Properties

| Category     | Value      |
| ------------- | ------------- |
| Topology | Buck-Boost |
| Input Range (VIN) | 6-36V DC|
| Output Voltage | 12 V (adjustable)|
| Output Current | 12 A |
| Output Power | 144 W |
| Default Switching Frequency | 250 kHZ (programmable via resistor)|
| Board Size | 9.14 cm x 9.14 cm |

**Efficiency according to TI:**

"Ultra high (>98%) peak power conversion efficiency"

![schematic](../media/LM5176EVM-HP_efficiency.png)

## 1.2 Critical Components

### 1.2.1 Selection Switches

| Switch    | Position     | Result |
| ------------- | ------------- | ------------- |
| S1 MODE | 2 | Hiccup mode enabled and CCM |
| | 3 | Hiccup disabled and CCM |
| S2 ENABLE | 1 | LM5176 disabled |
| | 2 | EN pin along resistor divider network to set LM5176 UVLO threshold (Choose R to set at which level of VIN the EN-pin reaches 1.2 Volt and starts the LM5176 starts)|
| | 3 | LM5176 enabled |
| S3 DITHER | 1 | frequency dithering feature disabled | 
| | 2 | frequency dithering feature enabled | 

### 1.2.2 Switches

Q1,Q2,Q3: [CSD18532Q5B 60-V N-Channel](../docs/BOM/Switches/csd18532q5b.pdf) 
RDS(on) 3.3 mOhm @ VGS=4.5V and 2.5 mOhm @ VGS=10V

Q5,Q7: [CSD17573Q5B 30-V N-Channel](../docs/BOM/Switches/csd17573q5b.pdf)
RDS(on) 1.19 mOhm @ VGS=4.5V and 0.84 mOhm @ VGS=10V

### 1.2.3 Inductors

L1: [XAL1510-472MEB](../docs/BOM/Inductors/xal1510.pdf)
DCR 3.35-3.8mOhm, SRF yp 12.7Mhz, Isat 39A, Irms 21-29A (rise 20-40C)


**Berechnung der parasitären Kapazität $C_p$** 

Die Kapazität wird aus der Resonanzbedingung abgeleitet:

$$C_p = \frac{1}{(2\pi \cdot f_{SRF})^2 \cdot L}$$

Parameter für XAL1510-472:
* Induktivität ($L$): $4,7 \cdot 10^{-6}H$
* Resonanzfrequenz ($f_{SRF}$):$12,7\text{ MHz}$

**Rechnung:**
$$C_p = \frac{1}{(2\pi \cdot 12,7 \cdot 10^6\text{ Hz})^2 \cdot 4,7 \cdot 10^{-6}\text{ H}} \approx 33,4\text{ pF}$$

L1 Alternate part: [Würth Elektronik 74439370047](../docs/BOM/Inductors/74439370047.pdf)



# 2. Simulation Model

LM5176EVM-HP schematic provided in the Documentation  ...

![schematic](../media/LM5176EVM-HP_schematic.png)

... The LM5176 schematic can bee seen in the following block diagram:

![schematic](../media/LM5176_func_block_diagram.png)

## 2.1 Buckmode

![schematic](../media/Buckmode/schematic_b001.png)




# 3. Stress & Margin Analysis

# 4. Spectral Analysis

# 5. Loss And Efficiency Comparison

# 6. Lab Measurements (if possible)

# 7. Conclusion & (optional) Improvement Proposal


# Notes

![FSBB Topology](../media/FBSS.png)

![FSBB Topology](../media/FBSS_buckmode.png)

![FSBB Topology](../media/FBSS_boostmode.png)

Source: https://youtu.be/I6fQurZZ5Ac?si=0BYR1ho-uJuIPpQX




- Isolated (Yes/No): "No"
- Control Mode: "Current-mode PWM"
- Primary Semiconductor Type(s): "Synchronous MOSFETs + controller"
- Load Profile / Special Features: "High-current automotive rail converter"
- Measurement Data Available (Yes/No): "Yes"
- Application Domain: "Automotive 12/24/48 V bus"