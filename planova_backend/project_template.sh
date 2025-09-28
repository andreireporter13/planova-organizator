#!/bin/bash

# Project folder name
PROJECT_NAME="whois-fastapi-project"

# Create project directories
mkdir -p $PROJECT_NAME/app/api
mkdir -p $PROJECT_NAME/app/core
mkdir -p $PROJECT_NAME/app/services
mkdir -p $PROJECT_NAME/app/models
mkdir -p $PROJECT_NAME/tests

# Create empty files inside the folders
touch $PROJECT_NAME/app/main.py
touch $PROJECT_NAME/app/api/__init__.py
touch $PROJECT_NAME/app/api/whois.py
touch $PROJECT_NAME/app/core/__init__.py
touch $PROJECT_NAME/app/core/config.py
touch $PROJECT_NAME/app/core/middleware.py
touch $PROJECT_NAME/app/services/__init__.py
touch $PROJECT_NAME/app/services/whois_service.py
touch $PROJECT_NAME/app/models/__init__.py
touch $PROJECT_NAME/app/models/whois_models.py
touch $PROJECT_NAME/tests/test_whois.py
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/Dockerfile
touch $PROJECT_NAME/README.md

# Print success message
echo "Project structure $PROJECT_NAME has been created successfully!"
