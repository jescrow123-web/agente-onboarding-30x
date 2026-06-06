# 🤖 Agente de Onboarding 30X

Agente conversacional que responde preguntas sobre la organización 30X basándose 
exclusivamente en los documentos internos de onboarding.

## ¿Cómo correrlo?

### 1. Requisitos
- Python 3.10 o superior
- Una API key de Cohere (gratis en cohere.com)

### 2. Instalar dependencias
pip install -r requirements.txt

### 3. Configurar API key
Abre app.py y reemplaza en esta línea tu API key de Cohere:
co = cohere.ClientV2("aqui-tu-key-de-cohere")

### 4. Correr la aplicación
streamlit run app.py

Se abrirá automáticamente en tu navegador en http://localhost:8501

## ¿Cómo actualizar los documentos?

Cuando cambie un documento de onboarding:
1. Reemplaza el PDF correspondiente en la carpeta raíz del proyecto
2. Asegúrate de que el nombre del archivo sea exactamente igual:
   - 30X_Doc1_Organizacion.pdf
   - 30X_Doc2_Programas_Operacion.pdf
   - 30X_Doc3_Equipo_Herramientas.pdf
3. Reinicia la aplicación con streamlit run app.py
El sistema carga los documentos automáticamente al arrancar.

## Credenciales necesarias

| Credencial | Dónde obtenerla | Costo |
|------------|-----------------|-------|
| Cohere API Key | dashboard.cohere.com | Gratis |

## Estructura del proyecto

30X/
├── app.py                          # Código principal
├── requirements.txt                # Dependencias
├── README.md                       # Este archivo
├── 30X_Doc1_Organizacion.pdf       # Documento de organización
├── 30X_Doc2_Programas_Operacion.pdf # Documento de programas
└── 30X_Doc3_Equipo_Herramientas.pdf # Documento de equipo

## Gaps identificados en los documentos

Durante la construcción se identificó que falta información importante:
- No existe ningún documento que indique el nombre ni contacto del Chief of Staff.
  Los documentos dicen "escríbele al Chief of Staff" pero nunca dicen quién es 
  ni cómo contactarlo. Esto debería agregarse para que el agente pueda dar 
  una respuesta completa.