from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ActualRoot = Path(__file__).resolve().parent
ProyectRoot = ActualRoot.parent
FileRoot = ProyectRoot / 'data' / 'transform.csv'
PlotsRoot = ProyectRoot / 'docs' / 'plots'

# Cargar los datos transformados
db = pd.read_csv(FileRoot)

def ensure_plots_dir():
    PlotsRoot.mkdir(parents=True, exist_ok=True)

def plot_expenses_by_month(save=False):
    month = db.groupby("month")["amount"].sum().sort_index()
    
    NamesMonths = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    month.index = month.index.map(NamesMonths)
    
    plt.figure(figsize=(10, 6))
    plt.bar(month.index, month.values, color='skyblue', edgecolor='black')
    plt.title('Gastos por Mes', fontsize=16)
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Gasto Total ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if save:
        ensure_plots_dir()
        plt.savefig(PlotsRoot / 'gastos_por_mes.png')
        print(f"Gráfico guardado en: {PlotsRoot / 'gastos_por_mes.png'}")
    else:
        plt.show()
    plt.close()

def plot_expenses_by_category(save=False):
    # Ordenamos de mayor a menor para una mejor visualización de categorías
    category = db.groupby("category")["amount"].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    plt.bar(category.index, category.values, color='salmon', edgecolor='black')
    plt.title('Gastos por Categoría', fontsize=16)
    plt.xlabel('Categoría', fontsize=12)
    plt.ylabel('Gasto Total ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if save:
        ensure_plots_dir()
        plt.savefig(PlotsRoot / 'gastos_por_categoria.png')
        print(f"Gráfico guardado en: {PlotsRoot / 'gastos_por_categoria.png'}")
    else:
        plt.show()
    plt.close()

def plot_expenses_by_hour(save=False):
    hour = db.groupby("hour")["amount"].sum().sort_index()
    
    # Formatear el eje X para que muestre horas como "08:00"
    hours = [f"{int(h):02d}:00" for h in hour.index]
    
    plt.figure(figsize=(12, 6))
    plt.bar(hours, hour.values, color='lightgreen', edgecolor='black')
    plt.title('Gastos por Hora', fontsize=16)
    plt.xlabel('Hora del Día', fontsize=12)
    plt.ylabel('Gasto Total ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if save:
        ensure_plots_dir()
        plt.savefig(PlotsRoot / 'gastos_por_hora.png')
        print(f"Gráfico guardado en: {PlotsRoot / 'gastos_por_hora.png'}")
    else:
        plt.show()
    plt.close()

def show_all_visualizations():
    plot_expenses_by_month()
    plot_expenses_by_category()
    plot_expenses_by_hour()

def save_all_visualizations():
    plot_expenses_by_month(save=True)
    plot_expenses_by_category(save=True)
    plot_expenses_by_hour(save=True)

if __name__ == "__main__":
    show_all_visualizations()
