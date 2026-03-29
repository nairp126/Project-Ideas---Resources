# Docker Cheatsheet

A quick reference for Docker commands, Dockerfile syntax, and Docker Compose.

## Table of Contents
- [Images](#images)
- [Containers](#containers)
- [Volumes & Networks](#volumes--networks)
- [Dockerfile Reference](#dockerfile-reference)
- [Docker Compose](#docker-compose)
- [Registry & Hub](#registry--hub)
- [Debugging & Inspection](#debugging--inspection)

---

## Images

Build, list, and manage Docker images.

```bash
# List local images
docker images
docker image ls

# Pull an image from Docker Hub
docker pull nginx
docker pull node:18-alpine

# Build an image from a Dockerfile
docker build -t my-app:1.0 .
docker build -t my-app:latest -f Dockerfile.prod .

# Tag an image
docker tag my-app:latest myrepo/my-app:1.0

# Remove an image
docker rmi my-app:1.0
docker image rm nginx

# Remove all unused images
docker image prune
docker image prune -a   # remove all not used by a container

# Inspect image metadata
docker inspect nginx

# Show image history (layers)
docker history my-app:latest
```

---

## Containers

Run, stop, and manage containers.

```bash
# Run a container (foreground)
docker run nginx

# Run in detached (background) mode
docker run -d nginx

# Run with a name
docker run -d --name my-nginx nginx

# Run with port mapping (host:container)
docker run -d -p 8080:80 nginx

# Run with environment variables
docker run -d -e NODE_ENV=production my-app

# Run with a volume mount
docker run -d -v /host/path:/container/path nginx

# Run interactively with a shell
docker run -it ubuntu bash
docker run -it --rm node:18 node   # --rm removes container on exit

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop my-nginx

# Start a stopped container
docker start my-nginx

# Restart a container
docker restart my-nginx

# Remove a container
docker rm my-nginx
docker rm -f my-nginx   # force remove running container

# Remove all stopped containers
docker container prune

# Execute a command in a running container
docker exec -it my-nginx bash
docker exec my-nginx ls /etc/nginx

# Copy files to/from a container
docker cp file.txt my-nginx:/etc/nginx/
docker cp my-nginx:/etc/nginx/nginx.conf ./
```

---

## Volumes & Networks

Persist data and connect containers.

```bash
# Create a named volume
docker volume create my-data

# List volumes
docker volume ls

# Inspect a volume
docker volume inspect my-data

# Remove a volume
docker volume rm my-data

# Remove all unused volumes
docker volume prune

# Run container with named volume
docker run -d -v my-data:/app/data my-app

# Create a network
docker network create my-network

# List networks
docker network ls

# Connect a container to a network
docker network connect my-network my-container

# Run container on a specific network
docker run -d --network my-network my-app

# Inspect a network
docker network inspect my-network

# Remove a network
docker network rm my-network
```

---

## Dockerfile Reference

Common Dockerfile instructions.

```dockerfile
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy dependency files first (layer caching)
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application source
COPY . .

# Set environment variable
ENV NODE_ENV=production
ENV PORT=3000

# Expose port (documentation only)
EXPOSE 3000

# Create non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/health || exit 1

# Default command
CMD ["node", "server.js"]

# Alternative: use ENTRYPOINT for fixed commands
ENTRYPOINT ["node"]
CMD ["server.js"]
```

```dockerfile
# Multi-stage build example
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```

---

## Docker Compose

Define and run multi-container applications.

```yaml
# docker-compose.yml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres-data:
```

```bash
# Start all services (detached)
docker compose up -d

# Start and rebuild images
docker compose up -d --build

# Stop all services
docker compose down

# Stop and remove volumes
docker compose down -v

# View logs
docker compose logs
docker compose logs -f web   # follow specific service

# Scale a service
docker compose up -d --scale web=3

# Run a one-off command
docker compose run web npm run migrate

# List running services
docker compose ps

# Restart a service
docker compose restart web
```

---

## Registry & Hub

Push and pull images from registries.

```bash
# Log in to Docker Hub
docker login

# Log in to a private registry
docker login registry.example.com

# Push an image
docker push myrepo/my-app:1.0

# Pull from a private registry
docker pull registry.example.com/my-app:latest

# Log out
docker logout

# Search Docker Hub
docker search nginx
```

---

## Debugging & Inspection

Troubleshoot containers and images.

```bash
# View container logs
docker logs my-container
docker logs -f my-container        # follow
docker logs --tail 100 my-container # last 100 lines

# Inspect container details (JSON)
docker inspect my-container

# View resource usage stats
docker stats
docker stats my-container

# View running processes inside container
docker top my-container

# Check container events
docker events

# Show system-wide info
docker info

# Show disk usage
docker system df

# Clean up everything unused
docker system prune
docker system prune -a --volumes   # aggressive cleanup
```
