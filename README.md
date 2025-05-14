# Proyecto: Integración de Gemini con FastAPI
## Descripción

Este proyecto consiste en la integración del modelo de lenguaje Gemini (de Google AI) utilizando Python y el framework FastAPI para crear una API REST que permite consumir los servicios de Gemini mediante una clave de autenticación.

## 📦 Dependencias
 
* Python 3.10+
* FastAPI
* Google Generative AI SDK (google-generativeai)
* Pydantic (para validación de datos)
* dotenv (para la carga de variables de entorno)

## 📁 Estructura del proyecto:

  📁 (root)/

 ┣ 📁 models           `Esquemas de datos (Pydantic)`

 ┣ 📄 main.py             `Punto de entrada de la aplicación FastAPI`

 ┣ 📄 .env                 `Archivo de variables de entorno, aquí puede ingresar la API Key`

 ┣ 📄 requirements.txt     `Dependencias del proyecto`


## 💫 Cómo utilizar:
1. Clonar el repositorio: `git clone https://github.com/dfontalv20/fastapi_ai.git`
2. Acceder a la carpeta del proyecto: `cd fastapi_ai`
3. Activar el entorno virtual: `.venv/scripts/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Agregar la API Key. Crea un archivo .env en la raíz del proyecto y añade tu clave de Gemini:
`API_KEY=***********`
4. Ejecutar el servidor: `fastapi dev main.py`. El servidor por defecto se ejecuta en el puerto 8000, puede acceder a la documentación de los endpoints mediante la ruta [localhost:8000/docs](http:localhost:8000/docs)