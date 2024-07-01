# Use uma imagem base do Alpine Linux
FROM alpine:latest

# Instale o SQLite
RUN apk update && \
    apk add sqlite && \
    rm -rf /var/cache/apk/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Comando padrão para iniciar o contêiner
CMD ["sqlite3", "/app/data.db"]