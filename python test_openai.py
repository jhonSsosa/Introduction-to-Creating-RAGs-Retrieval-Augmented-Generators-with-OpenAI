import os
import openai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la API Key desde el .env
openai_api_key = os.getenv("OPENAI_API_KEY")

# Validar que la API Key está configurada
if not openai_api_key:
    raise ValueError("No se encontró la clave de OpenAI. Verifica tu archivo .env")

# Crear un cliente de OpenAI
client = openai.OpenAI(api_key=openai_api_key)

# Hacer una consulta al modelo GPT-3.5-turbo
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Dime un chiste corto"}]
)

# Imprimir la respuesta
print("Respuesta de OpenAI:", response.choices[0].message.content)
