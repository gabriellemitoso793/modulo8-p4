import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega a chave da API
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configura o Gemini
genai.configure(api_key=GEMINI_API_KEY)

def query_gemini(prompt, model="gemini-pro"):
    """
    Envia um prompt para a API do Gemini e retorna a resposta.
    """
    try:
        # Inicializa o modelo Gemini
        model_gemini = genai.GenerativeModel(model)
        response = model_gemini.generate_content(prompt)
        return response.text.strip()  # Retorna apenas o texto da resposta
    except Exception as e:
        raise RuntimeError(f"Erro ao conectar com a API Gemini: {e}")
