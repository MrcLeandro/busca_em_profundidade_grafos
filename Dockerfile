# Usa uma imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto para o diretório de trabalho no container
COPY rede_social.py app.py entradas.csv resultados.csv README.md /app/

# Expondo a porta 8501 para publicação de serviços
EXPOSE 8501

# Comando padrão para executar a aplicação Python
CMD ["python", "app.py"]
