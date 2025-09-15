import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

excel_path = Path("../skostr_hoyde.xlsx")
COL_X = "skostr"
COL_Y = "hoyde"
output_pdf_path = Path("../output.pdf")

df = pd.read_excel(excel_path)
data = df[[COL_X, COL_Y]].dropna().astype(float)

x = data[COL_X].to_numpy()
y = data[COL_Y].to_numpy()

print("Datasett fra forsøk:")
for i in range(len(x)):
    print(f"Skostr (x): {x[i]}, Høyde (y): {y[i]}")

a, b, = np.polyfit(x, y, 1)
y_pred = a * x + b

print(f"\nRegresjonslinje: {a:.2f}x + {b:.2f}")

# Utregninger
n = len(x)

# Standardavvik for sko og høyde (utvalg, n-1 i nevneren)
std_sko = np.std(x, ddof=1)
std_hoyde = np.std(y, ddof=1)

# Standardavvik for punktene (x,y) samlet
x_bar, y_bar = np.mean(x), np.mean(y)
dist_sq = (x - x_bar)**2 + (y - y_bar)**2
std_points = np.sqrt(np.sum(dist_sq) / (n-1))

print(f"\nStandardavvik for sko: {std_sko:.2f}")
print(f"Standardavvik for høyde: {std_hoyde:.2f}")
print(f"Standardavvik for punktene: {std_points:.2f}")

# Forventningsverdi (gjennomsnitt)
print(f"Forventningsverdi for sko: {x_bar:.2f}")
print(f"Forventningsverdi for høyde: {y_bar:.2f}")

plt.scatter(x, y)
plt.plot(x, y_pred, color="red", label="Regresjonslinje")
plt.xlabel(COL_X)
plt.ylabel(COL_Y)
plt.legend()
plt.grid(True)

plt.savefig(output_pdf_path)

plt.show()