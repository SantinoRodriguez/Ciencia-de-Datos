# Bitácora del Proyecto

---

## 31-01-2026
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

## 02-02-2026
### Trabajo realizado
- Se implemento el modulo `transform.py` con el fin de modificar el dataframe, obteniendo fechas mas precisas y logrando limpiar los datos.
- Se creó un sistema para crear y colocar el nuevo dataframe junto con el original en la carpeta de `data`.
- Se implemento un sistema capaz de eliminar las filas que contengan un elemento de fecha o monto erroneo o nulo.

### Problemas encontrados
- Complejidad para hallar los valores erroneo o nulos.
- Fue necesario comprender cules son y como funcionan las funciones relacionadas con los nulls en `pandas`.

### Próximo paso
- Implementar el módulo `analysis.py` para poder entender la información recopilada y conseguir conclusiones a partir de ellas.

---

## 09-02-2026
### Trabajo realizado
- Se implemento el modulo `analysis.py` con el fin de hacer los calculos pertinentes al analisis del dataframe.
- Se alcanzo a responder cuales eran los maximos gastos de cada columna (año, mes, dia, hora y categoria)

### Problemas encontrados
- Complejidad para analizar dos columnas al mismo tiempo.
- Fue necesario comprender el funcionamiento de la función `groupby`.

### Próximo paso
- Complejizar el módulo `analysis.py` con el fin de poder responder preguntas mas profundas y complejas.