# Two-Tier Flask Application with Docker

A containerized two-tier web application using Flask and MySQL, orchestrated with Docker Compose and secured with Docker Scout scanning.

## Architecture

- **Frontend**: Flask web application
- **Backend**: MySQL database
- **Containerization**: Docker & Docker Compose
- **Security**: Docker Scout vulnerability scanning

## Prerequisites

- Docker
- Docker Compose
- Docker Scout (for vulnerability scanning)

## Quick Start

1. **Clone and navigate to project:**
```bash
git clone https://github.com/amoshsurya46/two-tier-flask-app.git
cd two-tier-flask-app
```

2. **Run the application:**
```bash
docker-compose up --build
```

3. **Access the application:**
   - Open http://localhost:5000 in your browser

## Docker Scout Security Scanning

**Scan for vulnerabilities:**
```bash
chmod +x docker-scout-scan.sh
./docker-scout-scan.sh
```

**Manual scanning:**
```bash
# Build image
docker build -t two-tier-flask-app .

# Scan for CVEs
docker scout cves two-tier-flask-app

# Get recommendations
docker scout recommendations two-tier-flask-app
```

## Project Structure

```
two-tier-flask-app/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container definition
├── docker-compose.yml    # Multi-container orchestration
├── init.sql              # Database initialization
├── docker-scout-scan.sh  # Security scanning script
├── templates/
│   └── index.html        # Web interface
└── README.md
```

## Features

- **User Management**: Add and view users
- **Database Persistence**: MySQL data storage
- **Container Networking**: Secure inter-container communication
- **Security Scanning**: Automated vulnerability detection
- **Production Ready**: Optimized Docker images

## Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs

# Stop services
docker-compose down

# Remove volumes
docker-compose down -v
```

## Security Best Practices

- Non-root user in containers
- Minimal base images
- Environment variable secrets
- Network isolation
- Regular vulnerability scanning