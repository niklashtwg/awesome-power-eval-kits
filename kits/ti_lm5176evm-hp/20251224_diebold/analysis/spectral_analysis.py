import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = "BuckNoDamp"
type = "Vo"

# 1. Daten laden (Annahme: Spalte 0 ist Zeit, Spalte 1 ist Strom/Spannung)
data = pd.read_csv('/Users/niklas/Code/awesome-power-eval-kits/kits/ti_lm5176evm-hp/20251224_diebold/analysis/Data' + name + '/' + type +'.csv')
time = data.iloc[:, 0].values
signal = data.iloc[:, 1].values

# 2. Abtastrate bestimmen
dt = time[1] - time[0]
fs = 1 / dt  # Samplingfrequenz

# 3. FFT berechnen
n = len(signal)
f = np.fft.rfftfreq(n, d=dt)
fft_values = np.abs(np.fft.rfft(signal)) / n * 2 # Amplitude normalisieren

# 4. Plotten
plt.figure(figsize=(10, 5))
plt.semilogy(f, fft_values) # Logarithmisch, um kleine Spikes zu sehen
plt.title(name + ' ' + type +  ' Frequenzspektrum (FFT)')
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.grid(True, which="both")
plt.xlim(0, 2e6) # Fokus auf 0 - 2 MHz (relevant für Schalter)
plt.show()

