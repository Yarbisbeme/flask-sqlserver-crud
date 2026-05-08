from flask import Flask, render_template, request, redirect, url_for, abort
import database as db

app = Flask(__name__) 

# Inicializa la base de datos al arrancar
with app.app_context():
    try:
        db.init_db()
    except Exception as e:
        print(f"Failed to initialize database: {e}")

# region READ
@app.route('/')
def index():
    conn = db.get_connection()
    if not conn:
        return "No se pudo establecer la conexión a la base de datos.", 500
        
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {db.TABLE}")
                colaboradores = cursor.fetchall()
                
                if not colaboradores:
                    print("No se encontraron colaboradores en la base de datos.")
                    colaboradores = []
                    
                return render_template('index.html', colaboradores=colaboradores)
    except Exception as e:
        print("Error al obtener los colaboradores:", e)
        return "Ocurrió un error al obtener los colaboradores.", 500
# endregion

# region CREATE
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        conn = db.get_connection()
        if not conn:
            return "No se pudo establecer la conexión a la base de datos.", 500
            
        try:
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            ciudad = request.form['ciudad']

            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO {db.TABLE} (nombre, apellido, ciudad) VALUES (?, ?, ?)", 
                        (nombre, apellido, ciudad)
                    )
                    conn.commit()
            print(f"Colaborador '{nombre} {apellido}' agregado exitosamente.")
            return redirect(url_for('index'))
        except Exception as e:
            print("Error al crear el colaborador:", e)
            return "Ocurrió un error al crear el colaborador.", 500
            
    # Bloque GET para renderizar los datos para creación
    try:     
        return render_template('create.html')
    except Exception as e:
        print("Error al renderizar la página de creación:", e)
        return "Ocurrió un error al cargar la página de creación.", 500
# endregion

# region UPDATE 
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = db.get_connection()
    if not conn:
        return "No se pudo establecer la conexión a la base de datos.", 500
        
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            ciudad = request.form['ciudad']
        
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE {db.TABLE} SET nombre=?, apellido=?, ciudad=? WHERE id=?", 
                        (nombre, apellido, ciudad, id)
                    )
                    conn.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print("Error al actualizar el colaborador:", e)
            return "Ocurrió un error al actualizar el colaborador.", 500

    # Bloque GET para renderizar los datos para edición
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {db.TABLE} WHERE id=?", (id,))
                colaborador = cursor.fetchone()
                
        if not colaborador:
            print(f"Colaborador con ID {id} no encontrado.")
            abort(404, description="Colaborador no encontrado.")
            
        return render_template('edit.html', colaborador=colaborador)
    except Exception as e:
        print("Error al obtener el colaborador para edición:", e)
        return "Ocurrió un error al cargar la página de edición.", 500
# endregion

# region DELETE 
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    conn = db.get_connection()
    if not conn:
        return "No se pudo establecer la conexión a la base de datos.", 500
        
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM {db.TABLE} WHERE id=?", (id,))
                conn.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print("Error al eliminar el colaborador:", e)
        return "Ocurrió un error al eliminar el colaborador.", 500
# endregion

if __name__ == '__main__':
    print("Iniciando aplicación CRUD...")
    app.run(debug=True, port=5000)