# Mini Proyecto – Análisis de Gastos

## Descripción General

Este proyecto consiste en el análisis exploratorio de un conjunto de datos de gastos almacenados en un archivo CSV. El objetivo es construir un pipeline de datos simple pero robusto que permita transformar datos crudos en información útil, identificando patrones de gasto a lo largo del tiempo y por categoría.

El proyecto sigue un enfoque estructurado, separando claramente las etapas de ingesta, transformación, limpieza y análisis, con el fin de facilitar su mantenimiento y escalabilidad.

## Preguntas a Resolver

Este proyecto busca responder preguntas exploratorias sobre los patrones de gasto registrados en el dataset, entre ellas:

- ¿En qué períodos de tiempo se registra el mayor gasto total?
- ¿Cómo se distribuye el gasto a lo largo del año y del mes?
- ¿Qué categorías concentran la mayor parte del gasto?
- ¿Existen patrones horarios en los gastos registrados?
- ¿El gasto presenta tendencias crecientes o decrecientes a lo largo del tiempo?
- ¿El gasto está distribuido uniformemente o concentrado en pocos eventos?

## Alcance del Proyecto

El proyecto contempla las siguientes etapas:

- Lectura de datos desde un archivo CSV
- Validación de tipos de datos (fechas y montos)
- Limpieza de datos inválidos o incompletos
- Transformación y enriquecimiento del dataset (variables temporales)
- Almacenamiento del dataset transformado
- Análisis exploratorio básico de los datos
- Generación de conclusiones a partir del análisis

### Fuera de alcance

- Modelos predictivos
- Técnicas de machine learning
- Imputación avanzada de datos faltantes
- Análisis estadístico inferencial

### Ingesta
Lectura del archivo CSV original sin modificaciones.

### Transformación y Limpieza

- Conversión de fechas a formato datetime
- Conversión de montos a valores numéricos
- Eliminación de filas con valores inválidos en columnas críticas
- Generación de variables derivadas (año, mes, día, hora)

### Almacenamiento
Escritura del dataset limpio en un nuevo archivo CSV para su posterior análisis.

## Estructura del Proyecto
```
PROYECTO N°1 - GASTOS/
├── data/
│   ├── raw.csv              # Datos originales sin modificar
│   └── transform.csv        # Datos limpios y transformados
├── src/
│   ├── load.py              # Ingesta y carga de datos
│   ├── transform.py         # Limpieza y transformación
│   └── analysis.py          # Análisis exploratorio
├── docs/                    # Documentación adicional
├── logs/                    # Registros de ejecución (opcional)
└── README.md
```

## Estado del Proyecto

- ✅ Ingesta de datos
- ✅ Validación y limpieza
- ✅ Transformación del dataset
- ⬜ Análisis exploratorio
- ⬜ Almacenamiento en base de datos (opcional)
- ⬜ Generación de reportes

## Limitaciones

- El dataset puede no representar gastos reales personales.
- El análisis se basa exclusivamente en los datos disponibles.
- La falta de información horaria completa puede limitar ciertos análisis temporales.

## Ejecución

La forma de ejecución del proyecto será documentada una vez finalizada la etapa de análisis, detallando los pasos necesarios para reproducir el pipeline completo desde la ingesta hasta la generación de conclusiones.