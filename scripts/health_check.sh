#!/usr/bin/env bash
set -e

echo "=== Vision Board Health Check ==="

if command -v docker >/dev/null 2>&1; then
    echo "Docker: OK"
else
    echo "Docker: NOT INSTALLED"
    exit 1
fi

if docker ps --format '{{.Names}}' | grep -q "vision-board"; then
    echo "Container: OK"
else
    echo "Container: NOT RUNNING"
    exit 1
fi

if curl -fsS http://localhost:5000/health >/dev/null; then
    echo "Application: OK"
else
    echo "Application: UNHEALTHY"
    exit 1
fi

echo "Overall health: HEALTHY"
