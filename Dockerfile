# 1. Usar uma imagem Python oficial e leve como base.
FROM python:3.12-slim

# 2. Definir o diretório de trabalho dentro do container.
WORKDIR /app

# 3. Copiar o arquivo de dependências PRIMEIRO para aproveitar o cache do Docker.
COPY requirements.txt .

# 4. Instalar as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o conteúdo do projeto (respeitando o .dockerignore).
# Ele irá copiar .py, .parquet, mas irá ignorar .venv, content/, etc.
COPY . .

# 6. Expor a porta que a nossa API FastAPI irá usar.
EXPOSE 8000

# 7. O comando para executar a aplicação quando o container iniciar.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]