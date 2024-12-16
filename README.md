# Industrial Safety Chatbot

Este é um chatbot desenvolvido para responder perguntas relacionadas a normas de segurança e uso de equipamentos em oficinas industriais. Ele utiliza a **Google Gemini API** para gerar respostas precisas e contextualizadas com base em um documento de referência.

## Funcionalidades

- **Carregamento de Documentos**: Processa o conteúdo de um PDF contendo regras e diretrizes de segurança.
- **Geração de Respostas**: Responde perguntas baseadas no contexto do PDF carregado.
- **Interface Intuitiva**: Desenvolvido com **Streamlit**, fornecendo uma interface amigável para interação.
- **Divisão de Texto**: O texto do PDF é dividido em chunks menores para um contexto otimizado.

## Pré-requisitos

Certifique-se de ter instalado:

- **Python 3.8+**
- **Google Cloud API Key** com acesso à **Generative Language API (Gemini)**.

## Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/gabriellemitoso793/modulo8-p4.git
cd modulo8-p4
cd chatbot_project
```

### 2. Instalar Dependências
Instale as dependências listadas no arquivo requirements.txt:
```bash
pip install -r src/requirements.txt
```

### 3. Configurar a API Key
1. Crie um arquivo .env na raiz do projeto:

```bash
touch .env
```
2. Adicione sua chave de API ao arquivo .env:
```bash
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

### 4. Organizar os Dados
Coloque o arquivo PDF de referência na pasta data/. Por exemplo:
```bash
data/Engineering-workshop-health-and-safety-guidelines-catalog.pdf
```

## Como Executar
1. Inicie o chatbot com Streamlit:
```bash
streamlit run src/chatbot.py
```

2. Interaja com o Chatbot:
- Carregue o PDF na barra lateral.
- Digite sua pergunta no campo de entrada e clique em "Enviar".

3. Exemplo de perguntas 
- Sobre Regras de Segurança
What is the appropriate attire for working in the workshop?
Which personal protective equipment (PPE) is mandatory when operating a wood lathe?
- Sobre Operação de Máquinas
Who is authorized to operate the portable welding machine?
What are the risks associated with using a scroll saw?
- Sobre Avaliação de Riscos
How is the risk matrix calculated for specific machines, such as a miter saw?