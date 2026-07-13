# AI Project Reporting Agent  — Contexto del Proyecto

## Qué hace este agente
Genera reportes ejecutivos de avance de proyecto adaptados a cada stakeholder,
leyendo el estado del proyecto desde archivos locales y enviándolos por mail.

## Stack técnico
- Lenguaje: Python 3.10+
- Modelo LLM: Gemini 3.5 Flash (Google AI Studio) — gratuito
- MCP: Filesystem MCP para leer archivos de config y datos
- Envío de mail: SMTP con Gmail

## Archivos clave
- `config/stakeholders.json` — lista de stakeholders y sus preferencias de comunicación
- `config/contexto_proyecto.md` — resumen ejecutivo y objetivos del proyecto
- `data/lakehouse_project.xlsx` — estado actual del proyecto (WBS, riesgos, cambios)
- `tools/` — tools individuales del agente
- `agents/` — lógica del agente principal
- `main.py` — punto de entrada

## Reglas para este proyecto
- Todo el código y comentarios en español
- No hardcodear API keys — usar archivo .env
- El agente decide qué tools invocar según el stakeholder
- Cada reporte debe adaptarse al nivel de detalle y formato del stakeholder