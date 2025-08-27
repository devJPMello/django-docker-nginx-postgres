FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências Python
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copiar o projeto
COPY app /app
COPY templates /templates
COPY entrypoint.sh /entrypoint.sh

# Configurar permissões
RUN chmod +x /entrypoint.sh

# Criar diretórios de volumes com permissões corretas
RUN mkdir -p /vol/static /vol/media && \
    chmod -R 777 /vol

EXPOSE 8000

CMD ["/entrypoint.sh"]
