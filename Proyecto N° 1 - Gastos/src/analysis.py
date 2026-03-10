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

# Promedio mensual en el año con más gasto
db_max_year = db[db["year"] == yearGreaterPaid]
avg_month_max_year = db_max_year.groupby("month")["amount"].sum().mean()

# Promedio diario en el mes con más gasto
db_max_month = db[db["month"] == MonthGreaterPaid]
avg_day_max_month = db_max_month.groupby("day")["amount"].sum().mean()
max_category_month = db_max_month.groupby("category")["amount"].sum().idxmax()
max_category_month_amount = db_max_month.groupby("category")["amount"].sum().max()

# Promedio horario en el día con más gasto
db_max_day = db[db["day"] == dayGreaterPaid]
avg_hour_max_day = db_max_day.groupby("hour")["amount"].sum().mean()

# Promedio por transacción en la hora con más gasto
avg_transaction_max_hour = db[db["hour"] == hourGreaterPaid]["amount"].mean()

# Promedio por transacción en la categoría con más gasto
avg_transaction_max_category = db[db["category"] == categoryGreaterPaid]["amount"].mean()
count_transaction_max_category = db[db["category"] == categoryGreaterPaid]["amount"].count()

# 2. Diccionario de Meses
NamesMonths = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# 3. Reporte de Resultados
def report_year():
    print(
        f"El año con mayores gastos es: {yearGreaterPaid} "
        f"con un total de ${yearMountGreaterPaid:,.2f}. "
        f"Promedio mensual ese año: ${avg_month_max_year:,.2f}"
    )
    print(year)


def report_month():
    print(
        f"El mes con mayores gastos es: {NamesMonths[MonthGreaterPaid]} "
        f"con un total de ${MountGreaterPaid:,.2f}. "
        f"Promedio diario ese mes: ${avg_day_max_month:,.2f}. "
        f"Máxima categoría: {max_category_month} con ${max_category_month_amount:,.2f}"
    )
    print(month)


def report_day():
    print(
        f"El día con mayores gastos es: {dayGreaterPaid} "
        f"con un total de ${dayMountGreaterPaid:,.2f}. "
        f"Promedio por hora ese día: ${avg_hour_max_day:,.2f}"
    )
    print(day)


def report_hour():
    print(
        f"La hora con mayores gastos es: {hourGreaterPaid}:00 hs "
        f"con un total de ${hourMountGreaterPaid:,.2f}. "
        f"Promedio por transacción esa hora: ${avg_transaction_max_hour:,.2f}"
    )
    print(hour)


def report_category():
    print(
        f"La categoría con mayores gastos es: {categoryGreaterPaid} "
        f"con un total de ${categoryMountGreaterPaid:,.2f}. "
        f"Promedio por transacción en esa categoría: "
        f"${avg_transaction_max_category:,.2f}, "
        f"con {count_transaction_max_category} compras"
    )
    print(category)

def inspect(column, value):
    data = db[db[column] == value]

    if data.empty:
        print(f"No hay datos para {column} = {value}")
        return

    total = data["amount"].sum()
    avg = data["amount"].mean()
    count = data["amount"].count()

    top_category = data.groupby("category")["amount"].sum().idxmax()
    top_category_amount = data.groupby("category")["amount"].sum().max()

    print(f"\n--- Análisis para {column} = {value} ---")
    print(f"Total gastado: ${total:,.2f}")
    print(f"Promedio por compra: ${avg:,.2f}")
    print(f"Cantidad de compras: {count}")
    print(f"Categoría con más gasto: {top_category} (${top_category_amount:,.2f})")

    print("\nDistribución por categoría:")
    print(data.groupby("category")["amount"].sum().sort_values(ascending=False))


#report_year()
#report_month()
#report_day()
#report_hour()
#report_category()
#inspect("hour", 17)
#inspect("day", 26)
#inspect("month", 7)
#inspect("year", 2024)
#inspect("category", "Restuarant")