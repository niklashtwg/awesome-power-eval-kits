import matplotlib.pyplot as plt

# --- 1. DATEN EINGEBEN ---

# Daten für Plot 1: Effizienz über den Laststrom (z.B. bei Vin = 24V)
load_amps = [0.5, 7.0, 12.0, 24.0]      # Last in Ampere
efficiency_load = [90.1, 97.8, 96.5, 94.2] # Effizienz in %

# Daten für Plot 2: Effizienz über die Eingangsspannung (z.B. bei 7A Last)
vin_volts = [12.0, 24.0, 36.0]         # Eingangsspannung in Volt
efficiency_vin = [94.8, 97.8, 97.2]    # Effizienz in %


# --- 2. PLOTS ERSTELLEN ---

# Erstelle eine Grafik mit zwei Diagrammen nebeneinander
plt.figure(figsize=(12, 5))

# Plot 1: Last vs. Effizienz
plt.subplot(1, 2, 1)
plt.plot(load_amps, efficiency_load, marker='o', linestyle='-', color='b', linewidth=2)
plt.title('Effizienz vs. Laststrom', fontsize=12)
plt.xlabel('Laststrom $I_{out}$ [A]', fontsize=10)
plt.ylabel('Effizienz $\eta$ [%]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(85, 100) # Passt den Bereich der Y-Achse an

# Plot 2: Vin vs. Effizienz
plt.subplot(1, 2, 2)
plt.plot(vin_volts, efficiency_vin, marker='s', linestyle='-', color='g', linewidth=2)
plt.title('Effizienz vs. Eingangsspannung', fontsize=12)
plt.xlabel('Eingangsspannung $V_{in}$ [V]', fontsize=10)
plt.ylabel('Effizienz $\eta$ [%]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(85, 100)

# Layout optimieren und speichern
plt.tight_layout()
plt.savefig('effizienz_auswertung.png', dpi=300)
plt.show()

print("Diagramme wurden als 'effizienz_auswertung.png' gespeichert.")