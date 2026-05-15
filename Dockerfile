# Usar a imagem oficial do Python
FROM python:3.12-slim

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivo de requisitos
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput || true

# Expor a porta
EXPOSE 8000

# Comando para executar a aplicação
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]
