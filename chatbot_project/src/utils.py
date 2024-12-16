from PyPDF2 import PdfReader

# Extrai texto de um arquivo PDF
def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if not text.strip():
            raise ValueError("O PDF está vazio ou não contém texto extraível.")
        return text
    except Exception as e:
        raise RuntimeError(f"Erro ao processar o PDF: {e}")

    
# Divide o texto em chunks menores com sobreposição
def split_text(text, chunk_size=512, overlap=50):
    tokens = text.split()
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunks.append(" ".join(tokens[i:i + chunk_size]))
    return chunks
