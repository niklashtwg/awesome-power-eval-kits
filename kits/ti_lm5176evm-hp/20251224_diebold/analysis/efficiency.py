import matplotlib.pyplot as plt

# --- 1. DATEN EINGEBEN ---

# Daten für Plot 1: Effizienz über den Laststrom (z.B. bei Vin = 24V)
# 12 V Data
#load_amps = [0.5, 0.8,1,1.4,1.8,2.5,3.5,5,8,12]      # Last in Ampere
#efficiency_load = [84.1,89.8,91.7, 93.7,94.8,95.7,96.1,96.1,95.25,93.7] # Effizienz in %

# 6 V Data
#load_amps = [0.5, 0.8,1,1.4,1.8,2.5,3.5,5,8,12]      # Last in Ampere
#efficiency_load = [97.6,98,98,97.9,97.6,97.1,96.2,94.8,91.8,87.8] # Effizienz in %

# 36 V Data
load_amps = [0.5, 0.8,1,1.4,1.8,2.5,3.5,5,8,12]      # Last in Ampere
efficiency_load = [67,79,83,87.8,90.3,92.8,94.4,95.5,96.1,95.9] # Effizienz in %



# Daten für Plot 2: Effizienz über die Eingangsspannung (z.B. bei 7A Last)
vin_volts = [12, 14, 16]         # Eingangsspannung in Volt
efficiency_vin = [90, 91, 93, ]    # Effizienz in %


# --- 2. PLOTS ERSTELLEN ---

# Erstelle eine Grafik mit zwei Diagrammen nebeneinander
plt.figure(figsize=(12, 5))

# Plot 1: Last vs. Effizienz
plt.subplot(1, 2, 1)
plt.plot(load_amps, efficiency_load, marker='o', linestyle='-', color='b', linewidth=2)
plt.title('Effizienz vs. Laststrom bei 36V', fontsize=12)
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