import matplotlib.pyplot as plt

# --- 1. DATEN EINGEBEN ---
load_amps = [0.5, 0.8, 1, 1.4, 1.8, 2.5, 3.5, 5, 8, 12]

# Effizienz-Daten für die verschiedenen Eingangsspannungen
eff_6V  = [97.6, 98.0, 98.0, 97.9, 97.6, 97.1, 96.2, 94.8, 91.8, 87.8]
eff_12V = [93.18,95.5,96.2,97,97.3,97.5,97.4,97,95.8,94.1]
eff_36V = [79.5,86.5,89,91.9,93.5,95,96.1,96.7,96.9,96.4]

# Daten für Plot 2: Effizienz über die Eingangsspannung
vin_volts = [12, 14, 16]
efficiency_vin = [90, 91, 93]


# --- 2. PLOTS ERSTELLEN ---
plt.figure(figsize=(12, 5))

# Plot 1: Last vs. Effizienz (Vergleich der Eingangsspannungen)
plt.subplot(1, 2, 1)
plt.plot(load_amps, eff_6V,  marker='s', linestyle='-', label='Vin = 6V',  color='g', linewidth=2)
plt.plot(load_amps, eff_12V, marker='o', linestyle='-', label='Vin = 12V', color='orange', linewidth=2)
plt.plot(load_amps, eff_36V, marker='^', linestyle='-', label='Vin = 36V', color='b', linewidth=2)

plt.title('Effizienz vs. Laststrom (100kHz)', fontsize=12)
plt.xlabel('Laststrom $I_{out}$ [A]', fontsize=10)
plt.ylabel('Effizienz $\eta$ [%]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()      # Zeigt die Legende an
plt.ylim(65, 100) # Untergrenze auf 65 gesetzt wegen der 36V-Kurve

# Plot 2: Vin vs. Effizienz
plt.subplot(1, 2, 2)
plt.plot(vin_volts, efficiency_vin, marker='d', linestyle='-', color='r', linewidth=2)
plt.title('Effizienz vs. Eingangsspannung', fontsize=12)
plt.xlabel('Eingangsspannung $V_{in}$ [V]', fontsize=10)
plt.ylabel('Effizienz $\eta$ [%]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(85, 100)

# Layout optimieren und speichern
plt.tight_layout()
plt.savefig('effizienz_vergleich.png', dpi=300)
plt.show()

print("Diagramm wurde als 'effizienz_vergleich.png' gespeichert.")