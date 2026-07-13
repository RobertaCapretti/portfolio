# Contexto del Proyecto — Data Lakehouse en Databricks

## 1. Resumen Ejecutivo

El proyecto busca migrar y centralizar las fuentes de datos dispersas (CRM, ERP, Google Analytics) 
hacia una arquitectura Lakehouse unificada en Databricks. La fragmentación actual impide realizar 
análisis avanzados y genera una demora de 5 días en la producción de reportes críticos. La solución 
automatizará el procesamiento de datos bajo una arquitectura medallion (Bronze/Silver/Gold), 
proveyendo una única fuente de verdad escalable, con gobernanza centralizada y preparada para 
analítica avanzada.

---

## 2. Objetivos del Proyecto

| # | Objetivo | Métrica de éxito | Plazo |
|---|---|---|---|
| O1 | Reducir el tiempo de procesamiento de datos en un 80% | Tiempo de pipeline < 60 min/día | Q2 2026 |
| O2 | Centralizar el 100% de los KPIs comerciales en una única fuente de verdad | 0 discrepancias entre Ventas y Finanzas en cierre mensual | Q2 2026 |
| O3 | Estandarizar transformaciones en Spark SQL/PySpark para reducir errores de lógica en un 30% | Tasa de error en tablas Gold < 0,1% | Q2 2026 |
| O4 | Implementar gobernanza de datos con Unity Catalog garantizando trazabilidad y control de accesos | 100% de tablas con linaje documentado y permisos asignados por rol | Q2 2026 |

---

## 3. Caso de Negocio

| | |
|---|---|
| **Problema** | Los procesos actuales dependen de scripts locales y consultas directas a sistemas de origen, generando silos de información donde Ventas y Finanzas no coinciden en sus cierres mensuales. El costo operativo es de 40 horas/mes de analistas dedicadas a limpieza manual de datos. |
| **Riesgo de inacción** | Imposibilidad de escalar hacia analítica predictiva o Machine Learning por baja calidad y desorden de los datos. Dependencia creciente de procesos no auditables y no replicables. |
| **Oportunidad** | Reducción de costos de infraestructura mediante auto-escalado de clusters en Databricks. Mejora en agilidad del negocio con datos confiables disponibles en tiempo near-real. |
| **ROI esperado** | Liberación de 40 hs/mes de trabajo analítico de bajo valor → reasignación a análisis estratégico. Reducción estimada del 30% en errores de lógica en reportes críticos. |