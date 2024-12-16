import streamlit as st
from gemini_handler import query_gemini
from utils import extract_text_from_pdf, split_text

# Configurações
PDF_PATH = "/home/inteli/modulo8-p4/chatbot_project/data/Engineering-workshop-health-and-safety-guidelines-catalog.pdf"

# Inicializa a sessão do Streamlit
if "chunks" not in st.session_state:
    st.session_state.chunks = []  # Inicializa os chunks vazios

def main():
    st.title("Industrial Safety Chatbot")
    st.sidebar.title("Configurações")
    
    # Botão para carregar o PDF
    if st.sidebar.button("Carregar PDF"):
        try:
            with st.spinner("Carregando e processando o PDF..."):
                pdf_text = extract_text_from_pdf(PDF_PATH)
                st.session_state.chunks = split_text(pdf_text)  # Divide em chunks
                st.sidebar.success("PDF carregado e processado!")
        except Exception as e:
            st.sidebar.error(f"Erro ao carregar o PDF: {e}")

    # Input do usuário
    st.subheader("Faça uma pergunta")
    user_input = st.text_input("Digite sua pergunta aqui:")

    # Gera a resposta do Gemini
    if st.button("Enviar"):
        if not user_input.strip():
            st.warning("Por favor, insira uma pergunta.")
        elif not st.session_state.chunks:
            st.warning("Por favor, carregue o PDF antes de fazer perguntas.")
        else:
            with st.spinner("Consultando o modelo..."):
                # Usa apenas o primeiro chunk como contexto
                context = st.session_state.chunks[0] if st.session_state.chunks else ""
                prompt = f"Contexto: {context}\n\nPergunta: {user_input}"
                try:
                    response = query_gemini(prompt)
                    st.success("Resposta:")
                    st.write(response)
                except Exception as e:
                    st.error(f"Erro ao gerar a resposta: {e}")

if __name__ == "__main__":
    main()
