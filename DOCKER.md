# Alura Space - Docker Setup

Projeto Django configurado para execução com Docker.

## Configuração Rápida

### 1. Clone ou configure o ambiente
```bash
cd alura_space
```

### 2. Crie um arquivo `.env` local (baseado no `.env.example`)
```bash
cp .env.example .env
```

Edite o arquivo `.env` e configure o `SECRET_KEY` com uma chave segura.

### 3. Execute com Docker Compose

**Primeira execução (com migrações):**
```bash
docker-compose up --build
```

**Próximas execuções:**
```bash
docker-compose up
```

### 4. Acesse a aplicação
- URL: `http://localhost:8000`
- Admin: `http://localhost:8000/admin`

## Comandos Úteis

### Parar os containers
```bash
docker-compose down
```

### Remover volumes (reseta o banco de dados)
```bash
docker-compose down -v
```

### Executar migrações manualmente
```bash
docker-compose exec web python manage.py migrate
```

### Criar superusuário
```bash
docker-compose exec web python manage.py createsuperuser
```

### Ver logs
```bash
docker-compose logs -f
```

## Build Manual (sem docker-compose)

### Build da imagem
```bash
docker build -t alura_space .
```

### Executar container
```bash
docker run -p 8000:8000 alura_space
```

## Estrutura dos Arquivos Docker

- **Dockerfile**: Define a imagem Docker
- **docker-compose.yml**: Configuração para orquestração
- **.dockerignore**: Arquivos ignorados no build
- **.env.example**: Exemplo de variáveis de ambiente
