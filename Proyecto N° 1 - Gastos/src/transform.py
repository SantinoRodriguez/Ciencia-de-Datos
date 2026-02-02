from load import db, ProyectRoot
import pandas as pd

# Esto convierte cualquier error (texto raro, fechas imposibles) en NaT o NaN
db['date'] = pd.to_datetime(db['date'], errors='coerce')
db['amount'] = pd.to_numeric(db['amount'], errors='coerce')

for attr in ['year','month','day','hour']:
    db[attr] = getattr(db['date'].dt, attr)

# Usamos subset para no borrar filas que tengan otros datos útiles pero sí fecha válida
db = db.dropna(subset=['date', 'amount'])

OutputRoot = ProyectRoot / 'data' / 'transform.csv'
db.to_csv(OutputRoot)