from tools.leer_archivos import leer_stakeholders, leer_contexto, leer_proyecto
from tools.enviar_mail import enviar_mail
from agents.generador_reporte import generar_reporte
from datetime import date


def corresponde_enviar(frecuencia: str) -> bool:
    """Determina si corresponde enviar el reporte hoy según la frecuencia."""
    hoy = date.today()

    if frecuencia == "diaria":
        return True
    elif frecuencia == "semanal":
        return hoy.weekday() == 0  # Lunes
    elif frecuencia == "quincenal":
        return hoy.day in [1, 15]
    elif frecuencia == "mensual":
        return hoy.day == 1
    elif frecuencia == "por hito":
        return False  # Solo manual
    else:
        return True


def main():
    print("🚀 Iniciando PM Weekly Digest...\n")

    # Leer insumos
    print("📂 Leyendo archivos del proyecto...")
    config = leer_stakeholders()
    contexto = leer_contexto()
    estado_proyecto = leer_proyecto()
    print("✅ Archivos leídos correctamente.\n")

    # Procesar cada stakeholder
    stakeholders = config.get("stakeholders", [])

    for stakeholder in stakeholders:
        nombre = stakeholder["nombre"]
        mail = stakeholder["mail"]
        frecuencia = stakeholder["frecuencia"]

        # SCHEDULER: descomentá estas líneas para activar envío automático por fecha
        # if not corresponde_enviar(frecuencia):
        #     print(f"⏭️ {nombre} — no corresponde enviar hoy ({frecuencia}). Salteando.")
        #     continue

        print(f"📊 Generando reporte para {nombre} ({frecuencia})...")
        reporte = generar_reporte(stakeholder, contexto, estado_proyecto)
        asunto = f"[PM Digest] Avance del proyecto — {stakeholder['formato']}"
        enviar_mail(mail, asunto, reporte)
        print()

    print("✅ PM Weekly Digest completado.")


if __name__ == "__main__":
    main()