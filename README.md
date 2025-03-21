# LangChain LLM Chain Tutorial

Este repositorio contiene la implementación de un LLM Chain con LangChain y OpenAI.

## Descripción
El proyecto utiliza LangChain para generar respuestas a partir de una cadena de modelo de lenguaje (LLM). Se usa un prompt template para estructurar la entrada y obtener respuestas en función de un tema específico.

## Estructura del Proyecto
```
📁 langchain-llm-chain/
│── 📄 index_llm.py
│── 📄 requirements.txt
│── 📄 .env.example
│── 📄 README.md
```

## Instalación y Configuración

1. Clonar el repositorio
   ```
   git clone https://github.com/jhonSsosa/Introduction-to-Creating-RAGs-Retrieval-Augmented-Generators-with-OpenAI.git
   cd Introduction-to-Creating-RAGs-Retrieval-Augmented-Generators-with-OpenAI
   ```

2. Crear un entorno virtual y activarlo
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias
   ```
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno  
   Copia el archivo `.env.example` como `.env` y agrega tu API Key de OpenAI:
   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```

## Uso
Ejecuta el script:
```
python index_llm.py
```
Ingresa un tema y obtendrás una respuesta generada por el modelo de lenguaje.
