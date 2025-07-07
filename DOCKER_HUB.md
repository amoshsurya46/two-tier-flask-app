# Docker Hub Deployment Guide

## 🐳 **Docker Hub Repository**
**Image**: `amoshsurya46/todo-list-app`
**URL**: https://hub.docker.com/r/amoshsurya46/todo-list-app

## 📦 **Available Tags**
- `latest` - Latest stable version
- `v1.0-secure` - Secure Alpine Linux version

## 🚀 **Quick Start**

### Pull and Run
```bash
# Pull the image
docker pull amoshsurya46/todo-list-app:latest

# Run with MySQL
docker run -d --name mysql-db \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=todoapp \
  mysql:8.0

# Run the todo app
docker run -d --name todo-app \
  --link mysql-db:mysql-db \
  -p 5000:5000 \
  -e DB_HOST=mysql-db \
  -e DB_USER=root \
  -e DB_PASSWORD=password \
  -e DB_NAME=todoapp \
  amoshsurya46/todo-list-app:latest
```

### Using Docker Compose
```yaml
version: '3.8'
services:
  web:
    image: amoshsurya46/todo-list-app:latest
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=mysql-db
      - DB_USER=root
      - DB_PASSWORD=password
      - DB_NAME=todoapp
    depends_on:
      - mysql-db

  mysql-db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=todoapp
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

## 🔒 **Security Features**
- ✅ Alpine Linux base (minimal attack surface)
- ✅ Only 1 vulnerability (96% reduction)
- ✅ Latest secure dependencies
- ✅ Production-ready

## 📊 **Image Details**
- **Size**: 87 MB
- **Base**: Alpine Linux 3.22
- **Python**: 3.13
- **Packages**: 47 (minimal)
- **Architecture**: linux/amd64

## 🌐 **Access Application**
After running: http://localhost:5000

## 📝 **Features**
- Full CRUD todo operations
- Priority levels (High/Medium/Low)
- Status filtering
- Modern responsive UI
- Real-time statistics
- Mobile-friendly design