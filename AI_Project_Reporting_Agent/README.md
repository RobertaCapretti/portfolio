# 🤖 AI Project Reporting Agent  

Agente de IA que genera reportes ejecutivos de avance de proyecto adaptados a cada stakeholder a partir del estado del proyecto y los distribuye automáticamente por correo electrónico.

Proyecto desarrollado para aplicar IA a procesos de Project Management mediante automatización y generación inteligente de reportes.

---

## 🧠 ¿Qué hace?

A partir de la documentación del proyecto (WBS, riesgos, cambios) y la configuración de stakeholders, el agente:

1. Obtiene el estado actual del proyecto.
2. Identifica las preferencias de comunicación de cada stakeholder.
3. Genera un reporte personalizado mediante un LLM.
4. Distribuye automáticamente cada reporte por correo electrónico.

Cada reporte es distinto: el COO recibe un Executive Status Report de alto nivel, 
el equipo técnico recibe un Daily Stand-up operativo, los SMEs reciben un Showcase 
orientado a negocio.

---

## 🎯 Caso de uso

En un proyecto, cada stakeholder necesita un nivel de detalle diferente, aunque la información de origen sea la misma.

- Sponsors → visión ejecutiva
- Steering Committee → avance y riesgos
- Equipo técnico → tareas operativas
- Áreas de negocio → funcionalidades entregadas

Este agente automatiza ese proceso: transforma un único estado del proyecto en comunicaciones adaptadas al rol, nivel de detalle y necesidades de información de cada audiencia, reduciendo trabajo manual y mejorando la consistencia de la comunicación.

---

## 🏗️ Arquitectura

                +----------------------+
                | Estado del Proyecto  |
                | (WBS, Riesgos, etc.) |
                +----------+-----------+
                           |
                           |
                +----------v-----------+
                | Configuración de     |
                | Stakeholders         |
                +----------+-----------+
                           |
                           |
                +----------v-----------+
                | AI Project           |
                | Reporting Agent      |
                +----------+-----------+
                           |
                           |
                +----------v-----------+
                | Reportes             |
                | Personalizados       |
                +----------+-----------+
                           |
                           |
                +----------v-----------+
                | Email Distribution   |
                +----------------------+

---

## 👥 Stakeholders configurados (proyecto ficticio)

| ID | Rol | Frecuencia | Formato |
|---|---|---|---|
| S01 | Sponsor (COO) | Mensual | Executive Status Report |
| S02 | Steering Committee | Quincenal | Dashboard de avance |
| S03 | Equipo Técnico | Diaria | Daily Stand-up |
| S04 | SMEs (Ventas/Marketing/Finanzas) | Semanal | Showcase / Sprint Review |
| S05 | Organización | Por hito | Project Newsletter |

---

## 🔄 Comunicación automática

Cada stakeholder recibe el reporte correspondiente según la frecuencia configurada (diaria, semanal, quincenal, mensual o por hito), evitando generar manualmente múltiples versiones de un mismo estado del proyecto.

---

## 📦 Stack

- **Modelo:** Gemini 3.5 Flash (Google AI Studio — gratuito)
- **Lenguaje:** Python 3.13
- **Librerías:** google-generativeai · openpyxl · python-dotenv
- **Mail:** SMTP Gmail con App Password
- **Asistente de desarrollo:** Cursor (AI-powered IDE) para debugging y refactorización, manteniendo el criterio de diseño y la validación funcional

---

## 🚀 Roadmap

El agente fue diseñado con una arquitectura modular para facilitar su integración con herramientas de gestión utilizadas en proyectos reales.

Este proyecto representa el primer componente de una visión más amplia de automatización del Project Management mediante IA, donde múltiples agentes especializados colaboran para asistir diferentes procesos del ciclo de vida del proyecto bajo un orquestador central.

### Integraciones previstas

- **Jira MCP** → Obtener issues, épicas, sprints y estado del backlog en tiempo real.
- **Azure DevOps MCP** → Incorporar work items, boards y pipelines.
- **GitHub MCP** → Utilizar actividad de desarrollo, pull requests y releases como contexto del proyecto.
- **Confluence MCP** → Leer documentación funcional y técnica para enriquecer los reportes.
- **Slack MCP** → Publicar reportes automáticamente en canales según el stakeholder.
- **Microsoft Teams** → Distribuir comunicaciones ejecutivas (integración via webhook o Power Automate)
- **Gmail / Outlook MCP** → Incorporar correos relevantes como contexto adicional y automatizar el envío de reportes.

---

## 📄 Documentación del proyecto

El agente fue desarrollado sobre un proyecto ficticio de migración a Databricks 
(Data Lakehouse). La documentación completa de gestión del proyecto — charter, WBS, 
registro de riesgos y plan de comunicación — está disponible en `docs/`.

---

## 🗂️ Estructura del proyecto
AI_Project_Reporting_Agent/  
├── agents/  
│   └── generador_reporte.py    # Genera el reporte con Gemini (no incluido en el repo)  
├── config/    
│   ├── stakeholders.json       # Configuración de stakeholders y preferencias  
│   └── contexto_proyecto.md    # Resumen ejecutivo y objetivos del proyecto  
├── data/  
│   └── lakehouse_project.xlsx  # Estado del proyecto (WBS, riesgos, cambios)  
├── docs/  
│   ├── lakehouse_project_plan.pdf           # Documentación completa de gestión del proyecto  
│   └── ai_project_reporting_agent_demo.pdf  # Output de ejemplo: los 5 reportes generados   
├── tools/  
│   ├── leer_archivos.py        # Lee xlsx, JSON y markdown  
│   └── enviar_mail.py          # Envía mails via SMTP Gmail  
├── AGENTS.md                   # Contexto del proyecto para asistentes de IA  
├── main.py                     # Punto de entrada (no incluido en el repo)  
├── requirements.txt            # Dependencias  
└── .env                        # API keys (no incluido en el repo)  

> Este repositorio presenta la arquitectura, los componentes principales y el enfoque funcional del agente.
>
> Si te interesa conversar sobre la implementación o posibles aplicaciones en entornos reales de Project Management, podés contactarme por LinkedIn o correo electrónico.
