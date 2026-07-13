import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
modelo = genai.GenerativeModel("gemini-3.5-flash")

def generar_reporte(stakeholder: dict, contexto: str, estado_proyecto: dict) -> str:
    """Genera un reporte personalizado para un stakeholder usando Gemini."""

    wbs = estado_proyecto.get("Seguimiento WBS", [])
    riesgos = estado_proyecto.get("Registro de Riesgos", [])
    cambios = estado_proyecto.get("Registro de Cambios", [])

    prompt = (
        "Sos un Project Manager experto generando un reporte de avance de proyecto.\n\n"
        "## Contexto del proyecto\n"
        f"{contexto}\n\n"
        "## Estado actual del proyecto\n\n"
        "### WBS (tareas y avance)\n"
        f"{wbs}\n\n"
        "### Riesgos activos\n"
        f"{riesgos}\n\n"
        "### Cambios registrados\n"
        f"{cambios}\n\n"
        "## Instrucciones para este reporte\n"
        f"- Destinatario: {stakeholder['nombre']} ({stakeholder['rol']})\n"
        f"- Formato: {stakeholder['formato']}\n"
        f"- Nivel de detalle: {stakeholder['nivel_detalle']}\n"
        f"- Instrucciones específicas: {stakeholder['instrucciones']}\n\n"
        "## Tu tarea\n"
        "Generá el reporte siguiendo exactamente las instrucciones del destinatario.\n"
        "Usá un tono apropiado para su rol. No incluyas información innecesaria.\n"
        "Escribí en español. No uses markdown complejo, solo texto plano con saltos de línea."
    )

    respuesta = modelo.generate_content(prompt)
    return respuesta.text