#!/bin/bash
set -e

echo "Building Docker image..."
docker build -t my-docker-app:latest .

echo "Build completed successfully!"