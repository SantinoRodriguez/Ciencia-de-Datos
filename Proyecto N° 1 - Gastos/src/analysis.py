from pathlib import Path
import pandas as pd
import os
os.system('cls')

ActualRoot = Path(__file__).resolve().parent
ProyectRoot = ActualRoot.parent
FileRoot = ProyectRoot / 'data' / 'transform.csv'

db = pd.read_csv(FileRoot)

#print(db.loc[0])

# A cada mes lo agrupamos con su monto sumado y ordenado por numero (Mes)
year = (db.groupby("year")["amount"].sum().sort_index())
month = (db.groupby("month")["amount"].sum().sort_index())
day = (db.groupby("day")["amount"].sum().sort_index())
hour = (db.groupby("hour")["amount"].sum().sort_index())
category = (db.groupby("category")["amount"].sum().sort_index())

# 1. Cálculos de Índices y Valores Máximos
yearGreaterPaid = year.idxmax()
yearMountGreaterPaid = year.max()

MonthGreaterPaid = month.idxmax()
MountGreaterPaid = month.max()

dayGreaterPaid = day.idxmax()
dayMountGreaterPaid = day.max()

hourGreaterPaid = hour.idxmax()
hourMountGreaterPaid = hour.max()

categoryGreaterPaid = category.idxmax()
categoryMountGreaterPaid = category.max()

# 2. Diccionario de Meses (ya proporcionado)
NamesMonths = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# 3. Reporte de Resultados
print(f"El año con mayores gastos es: {yearGreaterPaid} con un total de {yearMountGreaterPaid}")
print(year)

print(f"El mes con mayores gastos es: {NamesMonths[MonthGreaterPaid]} con un total de {MountGreaterPaid}")
print(month)

print(f"El día con mayores gastos es: {dayGreaterPaid} con un total de {dayMountGreaterPaid}")
print(day)

print(f"La hora con mayores gastos es: {hourGreaterPaid}:00 hs con un total de {hourMountGreaterPaid}")
print(hour)

print(f"La categoría con mayores gastos es: {categoryGreaterPaid} con un total de {categoryMountGreaterPaid}")
print(category)