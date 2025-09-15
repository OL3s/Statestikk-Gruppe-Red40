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

for i in range(len(x)):
    print(f"x: {x[i]}, y: {y[i]}")

a, b, = np.polyfit(x, y, 1)
y_pred = a * x + b

print(f"Regresjonslinje: {a:.2f}x + {b:.2f}")

plt.scatter(x, y)
plt.plot(x, y_pred, color="red", label="Regresjonslinje")
plt.xlabel(COL_X)
plt.ylabel(COL_Y)
plt.legend()
plt.grid(True)

plt.savefig(output_pdf_path)

plt.show()