from pathlib import Path
import pandas as pd

# Encontar la ruta del archivo CSV desde el archivo PY
ActualRoot = Path(__file__).resolve().parent
ProyectRoot = ActualRoot.parent
FileRoot = ProyectRoot / 'data' / 'raw.csv'

# Asignar el csv a una variable
db = pd.read_csv(FileRoot)