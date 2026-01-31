# Decisiones de Diseño

---

## Decisión 1
**Fecha:** 2026-01-31

**Decisión tomada:**  
- Utilizar archivos CSV como fuente de datos y Pandas como herramienta principal de manipulación y análisis.

**Alternativas consideradas:**  
- Uso de una base de datos relacional (MySQL).
- Carga de datos en memoria sin estructura tabular.

**Motivo:**  
- El volumen de datos es reducido y no requiere persistencia ni consultas concurrentes.
- Pandas permite un flujo de trabajo rápido y adecuado para análisis exploratorio.

**Consecuencias:**  
- El proyecto se mantiene simple y portable.
- No es necesario gestionar conexiones ni esquemas de base de datos.

---

## Decisión 2
**Fecha:** 2026-01-31

**Decisión tomada:**  
- Separar el procesamiento de datos en módulos independientes: carga, transformación y análisis.

**Alternativas consideradas:**  
- Un único script monolítico.
- Uso de notebooks sin separación clara de responsabilidades.

**Motivo:**  
- Facilitar el mantenimiento y la comprensión del flujo de datos.
- Evitar mezclar inspección, transformación y análisis en un mismo archivo.

**Consecuencias:**  
- Mayor claridad en el proyecto.
- Posibilidad de reutilizar etapas sin ejecutar todo el flujo.

---

## Decisión 3
**Fecha:** 2026-01-31

**Decisión tomada:**  
- Mantener el archivo CSV original sin modificaciones y tratarlo como fuente de verdad.

**Alternativas consideradas:**  
- Limpiar y sobrescribir el archivo original.
- Modificar los datos durante la carga.

**Motivo:**  
- Preservar la integridad del dataset original.
- Facilitar la reproducibilidad y auditoría del análisis.

**Consecuencias:**  
- Todas las transformaciones se realizan en memoria o en datasets derivados.
- Se reduce el riesgo de pérdida de información original.

---
