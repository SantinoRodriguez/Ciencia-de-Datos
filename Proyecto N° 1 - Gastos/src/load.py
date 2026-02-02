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

def info(data):
    """
    Este funcion permite al usuario visualizar los
    valores y secciones que componen la base de datos
    """
    examples = []

    examples.append(db.loc[0])
    print(f"Etiquetas\n{db.columns}\n")
    print(f"Ejemplo con valores reales\n{examples}\n")

info(db)