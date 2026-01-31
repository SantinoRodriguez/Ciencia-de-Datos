from pathlib import Path
import pandas as pd
import os
os.system('cls')

# Encontar la ruta del archivo CSV desde el archivo PY
ActualRoot = Path(__file__).resolve().parent
ProyectRoot = ActualRoot.parent
FileRoot = ProyectRoot / 'data' / 'raw.csv'

# Asignar el csv a una variable
db = pd.read_csv(FileRoot)
tags = []
examples = []

# Encontrar valores descriptivos
for column in db:
    tags.append(column)
    if (column == "amount"):
        # En caso que sea un numero con coma asignarlo automaticamente
        examples.append(float(db.loc[0, column]))
    else:
        examples.append(db.loc[0, column])

print(f"Etiquetas\n{tags}\n")
print(f"Ejemplo con valores reales\n{examples}\n")