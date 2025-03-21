import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Cargar variables de entorno
load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada.")

# Inicializar el modelo de OpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key)

# Probar con un mensaje
prompt = "Dime un saludo en italiano"
response = llm.invoke(prompt)

# Imprimir respuesta
print("Respuesta del modelo:", response.content)
