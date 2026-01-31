# Bitácora del Proyecto

---

## 31-01-2026-__
### Trabajo realizado
- Se seleccionó un dataset de gastos personales con el objetivo de trabajar sobre datos transaccionales reales.
- Se implementó un sistema de rutas robustas para garantizar que el archivo CSV pueda ser localizado independientemente del directorio de ejecución.
- Se realizó una inspección inicial del dataset para comprender su estructura, columnas y tipos de datos antes de aplicar cualquier transformación.

### Problemas encontrados
- Dificultad inicial para leer el archivo CSV debido a problemas con las rutas relativas.
- Fue necesario comprender cómo funciona el directorio de ejecución en Python y aprender a construir rutas robustas utilizando `pathlib`.

### Próximo paso
- Implementar el módulo `transform.py` para procesar la columna de fecha, separándola en componentes temporales (año, mes, día y hora) y preparar el dataset para el análisis exploratorio.

---