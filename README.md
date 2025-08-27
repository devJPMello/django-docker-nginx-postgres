# 🚀 Sistema de Upload de Arquivos com Django + Docker

## 📋 Descrição do Projeto

Este é um sistema completo de upload e gerenciamento de arquivos desenvolvido com **Django**, **Docker**, **Nginx** e **PostgreSQL**, atendendo aos requisitos da Atividade #1.

## 🏗️ Arquitetura

O projeto está estruturado com **3 containers Docker**:

1. **🐍 Container Django (Web)**: Aplicação principal com Gunicorn
2. **🌐 Container Nginx**: Proxy reverso e servidor de arquivos estáticos/mídia
3. **🗄️ Container PostgreSQL**: Banco de dados para persistência

## ✨ Funcionalidades

- ✅ **Upload de arquivos** com validação de tipo e tamanho
- ✅ **Persistência em volumes Docker** (arquivos não se perdem)
- ✅ **Interface moderna e responsiva** com drag & drop
- ✅ **Sistema de busca** por nome, descrição ou tipo
- ✅ **Paginação** dos arquivos enviados
- ✅ **Estatísticas** de uso (total de arquivos e espaço)
- ✅ **Validações** de segurança e formato
- ✅ **Mensagens de feedback** para o usuário

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2 + Gunicorn
- **Frontend**: HTML5 + CSS3 + JavaScript (Vanilla)
- **Banco**: PostgreSQL 15
- **Web Server**: Nginx
- **Containerização**: Docker + Docker Compose
- **Volumes**: Persistência de dados e arquivos

## 📁 Estrutura do Projeto

```
django-docker-nginx-postgres/
├── app/                          # Aplicação Django
│   ├── core/                     # App principal
│   │   ├── models.py            # Modelo de arquivos
│   │   ├── views.py             # Views da aplicação
│   │   ├── forms.py             # Formulários
│   │   └── urls.py              # URLs do app
│   ├── myproject/               # Configurações do projeto
│   │   ├── settings.py          # Configurações Django
│   │   └── urls.py              # URLs principais
│   └── manage.py                # Comando Django
├── docker/                       # Configurações Docker
│   └── nginx/                   # Configuração Nginx
│       └── nginx.conf           # Configuração do servidor
├── templates/                    # Templates HTML
│   └── upload.html              # Interface principal
├── Dockerfile                    # Imagem Django
├── Dockerfile.nginx             # Imagem Nginx
├── docker-compose.yml           # Orquestração dos containers
├── entrypoint.sh                # Script de inicialização
├── requirements.txt              # Dependências Python
└── .env                         # Variáveis de ambiente
```

## 🚀 Como Executar

### Pré-requisitos

- Docker Desktop instalado e rodando
- Git (para clonar o repositório)

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd django-docker-nginx-postgres
```

### 2. Execute a aplicação

```bash
# Construir e iniciar todos os containers
docker-compose up --build

# Ou em background
docker-compose up -d --build
```

### 3. Acesse a aplicação

- **URL Principal**: http://localhost
- **Admin Django**: http://localhost/admin
  - **Usuário**: admin
  - **Senha**: admin123

## 🔧 Configurações

### Variáveis de Ambiente (.env)

```env
POSTGRES_DB=django_files
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password_2024
DEBUG=True
SECRET_KEY=django-insecure-production-key-change-this-2024
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
```

### Volumes Docker

- **postgres_data**: Dados do banco PostgreSQL
- **static_volume**: Arquivos estáticos do Django
- **media_volume**: Arquivos enviados pelos usuários

## 📊 Funcionalidades da Aplicação

### Upload de Arquivos
- Suporte a múltiplos formatos (PDF, DOC, XLS, imagens, etc.)
- Validação de tamanho (máximo 100MB)
- Validação de extensões permitidas
- Campo de descrição opcional

### Gerenciamento
- Lista paginada de arquivos
- Busca por nome, descrição ou tipo
- Estatísticas de uso
- Download direto dos arquivos

### Segurança
- Validação CSRF
- Sanitização de uploads
- Headers de segurança no Nginx
- Usuário não-root nos containers

## 🐳 Comandos Docker Úteis

```bash
# Ver logs em tempo real
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f web
docker-compose logs -f nginx
docker-compose logs -f db

# Parar todos os serviços
docker-compose down

# Parar e remover volumes (⚠️ CUIDADO: apaga dados)
docker-compose down -v

# Reconstruir um serviço específico
docker-compose build web
docker-compose up web

# Acessar container em execução
docker-compose exec web bash
docker-compose exec db psql -U django_user -d django_files
```

## 🔍 Monitoramento

### Health Checks
- **PostgreSQL**: Verificação de conectividade
- **Nginx**: Endpoint `/health` para verificação
- **Django**: Verificação automática de dependências

### Logs
- Todos os serviços logam para stdout/stderr
- Logs podem ser visualizados com `docker-compose logs`

## 🚨 Solução de Problemas

### Container não inicia
```bash
# Verificar logs
docker-compose logs <nome-do-servico>

# Verificar status dos containers
docker-compose ps

# Reconstruir containers
docker-compose down
docker-compose up --build
```

### Problemas de permissão
```bash
# Verificar permissões dos volumes
docker-compose exec web ls -la /vol

# Corrigir permissões se necessário
docker-compose exec web chown -R django:django /vol
```

### Banco não conecta
```bash
# Verificar se PostgreSQL está rodando
docker-compose exec db pg_isready -U django_user

# Verificar logs do banco
docker-compose logs db
```

## 📈 Melhorias Futuras

- [ ] Autenticação de usuários
- [ ] Compressão de arquivos
- [ ] Backup automático dos volumes
- [ ] Monitoramento com Prometheus
- [ ] HTTPS com Let's Encrypt
- [ ] Cache Redis para performance
- [ ] API REST para integração

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

## 👨‍💻 Autor

Desenvolvido para a Atividade #1 - Sistema de Upload com Docker.

---

**🎯 Objetivo Alcançado**: Sistema completo com 3 containers Docker, upload de arquivos, volumes persistentes e interface moderna!
