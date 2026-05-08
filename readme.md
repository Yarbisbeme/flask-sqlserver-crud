# 🚀 Mini CRUD - Flask & SQL Server

Aplicación web desarrollada para aprender sobre Flask que implementa las operaciones básicas (Create, Read, Update, Delete) utilizando **Python**, **Flask** y **SQL Server**. Puedes usar este proyecto como gustes y hacer los cambios que quieras.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, Flask
* **Base de Datos:** SQL Server (ODBC Driver 18)
* **Librerías:** `pyodbc`, `python-dotenv`
* **Pruebas Automatizadas (E2E):** Cypress, Node.js (Patrón Page Object Model y Fixtures)
* **Integración Continua (CI):** GitHub Actions (Pruebas automáticas con base de datos en la nube)
* **Frontend:** HTML5, Jinja2, Bootstrap 5 (CDN)
* **Arquitectura:** Patrón MVC (Separación de rutas, lógica de base de datos y vistas)

## ⚙️ Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalado:
* [Python 3.x](https://www.python.org/)
* [Node.js](https://nodejs.org/) (Necesario para ejecutar las pruebas de Cypress)
* [SQL Server](https://www.microsoft.com/es-es/sql-server/sql-server-downloads)
* [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/es-es/sql/connect/odbc/download-odbc-driver-for-sql-server)

---------
## 🚀 Instalación y Uso

Sigue estos pasos para desplegar el proyecto en tu entorno local:

**1. Clonar el repositorio:**

Si usas Vscode puedes pegar la url directamente al seleccionar clonar repositorio.

**2. Crear y activar un entorno virtual:**
```
# En Windows
python -m venv env
.\env\Scripts\activate
```
**3. Instalar las dependencias:**
```
pip install flask pyodbc
```
**4. Configurar las Variables de Entorno (.env):**

Crea un archivo llamado `.env` en la raíz del proyecto (al mismo nivel que `app/`) y define tus credenciales de SQL Server de la siguiente manera:

```
SERVER=TuServidorSQL       # Ej: localhost o HD-02
DATABASE=TuBaseDeDatos     # Ej: test
UID=TuUsuario              # Ej: sa
PWD=TuContraseña           # Ej: tu_password
TABLE=colaboradores        # El nombre que tendrá la tabla
```

*Nota:* La aplicación creará automáticamente la tabla configurada al ejecutarse por primera vez gracias a la función `init_db()`. Asegúrate de que el usuario configurado tenga permisos de creación de tablas (`db_owner`).


**5. Ejecutar la aplicación:**
```
python .\app\app.py
```

El servidor se iniciará en http://localhost:5000/.

---------
## 🧪 Pruebas Automatizadas (Cypress E2E)

Este proyecto incluye una suite de pruebas de extremo a extremo (E2E) desarrollada con Cypress, implementando el patrón de diseño Page Object Model (POM) y el uso de Fixtures para desacoplar el código de los datos de prueba.

#### Configuración e Instalación:
**1. Instalar dependencias de Node.js:**
Asegúrate de estar en la raíz del proyecto y ejecuta:
```
npm install
```

**2. Ejecutar las pruebas en modo interactivo (GUI):**
Para abrir la interfaz gráfica de Cypress, ver el navegador interactuar solo y debugear en tiempo real:

```
npx cypress open
```

**3. Ejecutar las pruebas en modo consola (Headless):**
Para ejecutar las pruebas en segundo plano de manera rápida:
```
npx cypress run
```

---------
## 🔄 Integración Continua (CI Pipeline)

El repositorio cuenta con un pipeline de Integración Continua automatizado mediante **GitHub Actions (`.github/workflows/ci.yml`)**.

Cada vez que se realiza un `push` o un `Pull Request` hacia la rama `main` o `dev`, el pipeline se dispara automáticamente en la nube realizando el siguiente flujo de calidad:

1. Levanta un contenedor con un servicio temporal de **SQL Server 2022**.

2. Configura el entorno de Python e instala las dependencias necesarias.

3. Configura los drivers oficiales de ** (`msodbcsql18`) en el entorno de Linux de GitHub.

4. Levanta la aplicación de **Flask** en segundo plano.

5. Descarga e inicia **Cypress** para correr toda la suite de pruebas E2E.

6. Si alguna prueba falla o el servidor de **Flask** arroja un error de base de datos, el pipeline marcará el build como fallido, protegiendo la rama principal de código roto.

---------
## 📂 Estructura del Proyecto

```
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline de CI/CD de GitHub Actions
├── app/                        # Carpeta de la aplicación web Flask
│   ├── app.py                  # Controlador principal y rutas (CRUD) 
│   ├── database.py             # Lógica de conexión e inicialización de SQL Server
│   └── templates/              # Vistas renderizadas con Jinja2
│       ├── layout.html         # Plantilla maestra con Bootstrap 5
│       ├── index.html          # Lista de registros (Read / Delete)
│       ├── create.html         # Formulario de inserción (Create)
│       └── edit.html           # Formulario de edición (Update)
├── cypress/                    # Carpeta de pruebas automatizadas Cypress
│   ├── e2e/
│   │   └── colaboradores.cy.js # Test principal que ejecuta el ciclo CRUD
│   ├── fixtures/
│   │   └── colaborador_prueba.json # Datos de prueba estáticos (Fixtures)
│   └── support/
│       ├── e2e.js              # Archivo de configuración global de Cypress
│       └── page_objects/       # Clases del patrón Page Object Model (POM)
│           ├── indexPage.js    # Selectores y acciones del listado principal
│           └── formPage.js     # Selectores y acciones del formulario
├── .env                        # Variables de entorno (No subir a GitHub)
├── package.json                # Dependencias de Node.js (Cypress)
└── README.md                   # Documentación del proyecto
```

<div align="center">
  <h1>👨‍💻 Acerca del Desarrollador</h1>
  </br>
  <img src="https://github.com/Yarbisbeme/CieloObs/raw/main/assets/images/yarbis.png" width="150" height="150" style="border-radius: 20%; object-fit: cover; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  
  ### Yarbis Beltré Mercedes
  **FullStack Developer & QA Engineer**

  Desarrollador enfocado en crear soluciones eficientes, automatizadas y escalables. Apasionado por la mejora continua, la automatización de procesos y el aseguramiento de calidad (QA). Cuando no estoy codeando, probablemente me encuentres en el piano. 🎹

  <br/>

  [![Contact Me](https://img.shields.io/badge/✉️_Contact_Me-673AB7?style=for-the-badge)](mailto:yarbisbeme@gmail.com)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://do.linkedin.com/in/yarbis-beltre-mercedes)
  [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)]([github.com/tu-usuario](https://github.com/Yarbisbeme))
</div>