#!/bin/bash

echo "Deploying System Monitor..."

# Остановить существующий контейнер
docker stop system-monitor || true
docker rm system-monitor || true

# Запустить новый контейнер
docker run -d \
  --name system-monitor \
  --restart unless-stopped \
  -v $(pwd)/config:/app/config \
  speedy-solutions/system-monitor:latest

echo "System Monitor deployed successfully!"
