# Usa a imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt requirements.txt
COPY .env .env
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente necessária para Streamlit
ENV STREAMLIT_SERVER_HEADLESS true

# Expõe a porta usada pelo Streamlit
EXPOSE 8501

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "app.py"]
