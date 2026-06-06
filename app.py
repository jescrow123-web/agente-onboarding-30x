import streamlit as st
import pypdf
import os
import cohere

# =================================================================
# CONFIGURACIÓN
# =================================================================
from dotenv import load_dotenv
load_dotenv()
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))


# =================================================================
# LEER LOS PDFs
# =================================================================
@st.cache_resource
def cargar_documentos():
    texto_total = ""
    archivos_pdf = [
        "30X_Doc1_Organizacion.pdf",
        "30X_Doc2_Programas_Operacion.pdf",
        "30X_Doc3_Equipo_Herramientas.pdf"
    ]
    for archivo in archivos_pdf:
        if os.path.exists(archivo):
            reader = pypdf.PdfReader(archivo)
            for pagina in reader.pages:
                texto_total += pagina.extract_text() + "\n"
    return texto_total

documentos = cargar_documentos()

SYSTEM_PROMPT = f"""Eres el Agente de Onboarding de 30X. Respondes ÚNICAMENTE basándote en los documentos internos de la empresa.

REGLAS:
1. Solo usa la información de los documentos. No inventes nada.
2. Si la respuesta no está en los documentos, di: "No tengo esa información en los manuales. Te recomiendo escribirle al Chief of Staff."
3. Responde siempre en español.

DOCUMENTOS INTERNOS DE 30X:
{documentos}
"""

# =================================================================
# INTERFAZ
# =================================================================
st.set_page_config(page_title="30X Onboarding Agent", page_icon="🤖")
st.title("🤖 Agente de Onboarding 30X")
st.write("Hola! Soy tu asistente de onboarding. Pregúntame lo que necesites sobre 30X.")

if "historial" not in st.session_state:
    st.session_state.historial = []

for msg in st.session_state.historial:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if pregunta := st.chat_input("Escribe tu pregunta aquí..."):
    st.session_state.historial.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)

    mensajes = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.historial:
        mensajes.append({"role": msg["role"], "content": msg["content"]})

    try:
        respuesta = co.chat(
            model="command-a-03-2025",
            messages=mensajes
        )
        respuesta_final = respuesta.message.content[0].text
    except Exception as e:
        respuesta_final = f"Error: {str(e)}"

    st.session_state.historial.append({"role": "assistant", "content": respuesta_final})
    with st.chat_message("assistant"):
        st.write(respuesta_final)