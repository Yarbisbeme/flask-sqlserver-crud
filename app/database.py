import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
UID = os.getenv('UID')
PWD = os.getenv('PWD')
TABLE = os.getenv('TABLE')

def get_connection():
    try:
        conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD};TrustServerCertificate=yes'
        return pyodbc.connect(conn_str)
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise

def init_db():
    conn = get_connection()
    if not conn:
        return "No se pudo establecer la conexión a la base de datos.", 500
    try:
        cursor = conn.cursor()
        cursor.execute(f'''
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{TABLE}' AND xtype='U')
            CREATE TABLE {TABLE} (
                id INT IDENTITY(1,1) PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                ciudad VARCHAR(50)
            )
        ''')
        conn.commit()
    except Exception as e:
        print("Error al inicializar la base de datos:", e)
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()