import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG  # Importamos la configuración segura

def probar_conexion():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("✅ Conexión exitosa a MySQL")
        conn.close()
    except Error as e:
        print(f"❌ Error al conectar con MySQL: {e}")

if __name__ == "__main__":
    probar_conexion()
