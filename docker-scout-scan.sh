#!/bin/bash

echo "Building Docker image..."
docker build -t two-tier-flask-app .

echo "Scanning image with Docker Scout..."
docker scout cves two-tier-flask-app

echo "Generating recommendations..."
docker scout recommendations two-tier-flask-app

echo "Scan complete!"