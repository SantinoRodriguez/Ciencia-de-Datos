from src import analysis
from src import transform
from src import load
from src import visualization

transform.transform_data()

analysis.report_year()
analysis.report_month()
analysis.report_day()
analysis.report_hour()
analysis.report_category()
analysis.inspect("hour", 17)
analysis.inspect("day", 26)
analysis.inspect("month", 7)
analysis.inspect("year", 2024)
analysis.inspect("category", "Restuarant")

print("\nGuardando visualizaciones...")
visualization.save_all_visualizations()