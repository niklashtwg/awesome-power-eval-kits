import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = "BuckNoDamp"
type = "SW2"

# 1. Daten laden
data = pd.read_csv('/Users/niklas/Code/awesome-power-eval-kits/kits/ti_lm5176evm-hp/20251224_diebold/analysis/Data' + name + '/' + type +'.csv')
time = data.iloc[:, 0].values
signal = data.iloc[:, 1].values

# 2. Abtastrate & Nyquist-Check
dt = time[1] - time[0]
fs = 1 / dt
print(f"Maximal sichtbare Frequenz: {fs/2e6:.2f} MHz")

# 3. FFT berechnen
n = len(signal)
f = np.fft.rfftfreq(n, d=dt)
fft_values = np.abs(np.fft.rfft(signal)) / n * 2 

# 4. Zoom-Plot: Fokus auf 12.7 MHz
plt.figure(figsize=(10, 6))
plt.semilogy(f, fft_values, label='FFT Spektrum', color='blue')

# Fokus-Bereich: 5 MHz bis 25 MHz
plt.xlim(5e6, 25e6) 

# Markante Punkte markieren
srf_induktor = 12.7e6
plt.axvline(x=srf_induktor, color='red', linestyle='--', linewidth=1.5, label=f'Inductor SRF ({srf_induktor/1e6} MHz)')

# Kosmetik
plt.title(f'Zoom: Resonanz-Analyse bei {srf_induktor/1e6} MHz', fontsize=14)
plt.xlabel('Frequenz [Hz]', fontsize=12)
plt.ylabel('Amplitude (log)', fontsize=12)
plt.grid(True, which="both", linestyle=':', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()