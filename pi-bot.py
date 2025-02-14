import mysql.connector
from config import DB_CONFIG  # Importamos la configuración segura
import ollama
from datetime import datetime
from tabulate import tabulate

# Conectar a MySQL y obtener viajes del día
def obtener_viajes_hoy():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    query = """
    SELECT numero_asignacion, fecha_cita, hora_cita, fecha_embarque, 
           nombre_operador, destino, transportista, sublinea 
    FROM sipisa.tb_viajes_oc 
    WHERE DATE(fecha_cita) = %s 
    ORDER BY fecha_cita DESC 
    LIMIT 10;
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (fecha_hoy,))
        viajes = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"❌ Error en la conexión a MySQL: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return viajes

# Mostrar viajes en tabla
def mostrar_viajes():
    viajes = obtener_viajes_hoy()
    
    if not viajes:
        return "❌ No hay viajes registrados para hoy."
    else:
        print("✅ Se encontraron viajes, ejemplo del primer resultado:")

    return tabulate(viajes, headers="keys", tablefmt="grid")


# Procesar consulta con IA
def procesar_consulta(user_input):
    mensaje_sistema = """
    Eres un asistente que ayuda a generar reportes de viajes desde una base de datos.
    El usuario puede pedir reportes con diferentes filtros como fecha, transportista, operador, etc.
    Si el usuario pide un "reporte", "viajes" o menciona algo relacionado, dile que estás generando el reporte y muestra los datos.
    """
    respuesta = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": mensaje_sistema},
            {"role": "user", "content": user_input}
            ]
    )

    contenido_ia = respuesta["message"]["content"].lower()
    print(f"\n🔍 Respuesta completa de la IA:\n{contenido_ia}\n")  # Muestra la respuesta original de la IA

    if "viajes" in contenido_ia.lower() or "reporte" in contenido_ia:
        print("\n📋 Reporte de Viajes del Día:")
        print(mostrar_viajes())
    else:
        print("\n🤖 IA: No entendí la solicitud, intenta ser más claro.")

# Chat interactivo
def chat():
    print("💬 Chatbot de Reportes - Escribe 'salir' para terminar.\n")
    
    while True:
        user_input = input("\n👤 Usuario: ")
        if user_input.lower() == "salir":
            print("👋 ¡Hasta luego!")
            break
        
        procesar_consulta(user_input)

if __name__ == "__main__":
    chat()
