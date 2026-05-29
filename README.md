# DevOps Intern Assessment

## Overview
This repository contains the solution for the DevOps Internship technical assessment.
It includes a Dockerized Python application with a CI pipeline using GitHub Actions.

## Repository Structure
devops-intern-app/
├── .github/
│   └── workflows/
│       └── CI.yaml        # GitHub Actions CI pipeline
├── bash-app/              # Bash application (provided)
├── java-app/              # Java application (provided)
├── python-app/            # Python application (selected)
│   ├── tests/             # Test suite
│   ├── app.py             # Application source code
│   ├── Dockerfile         # Multi-stage Dockerfile
│   └── pyproject.toml     # Project dependencies
└── README.md

## Task 1: Dockerfile

The Dockerfile uses a multi-stage build approach:

### Development Stage
- Based on `python:3.12-slim` official Docker image
- Installs all dependencies including pytest for testing
- Includes the `tests/` folder
- Accepts `NAME` as a build argument

### Production Stage
- Based on `python:3.12-slim` official Docker image
- Installs only production dependencies (no pytest)
- Excludes the `tests/` folder
- Minimal image size

### Build Instructions

```bash
# Build development image
docker build --target development --build-arg NAME=Intern -t python-app:dev ./python-app

# Build production image
docker build --target production --build-arg NAME=Intern -t python-app:prod ./python-app

# Run the app
docker run python-app:prod

# Run tests
docker run --rm --entrypoint python python-app:dev -m pytest tests/test_app.py -v
```

## Task 2: CI Pipeline

The GitHub Actions pipeline (`.github/workflows/CI.yaml`) automatically:

1. Triggers on every push or pull request to `main`
2. Checks out the repository
3. Builds the Docker image using the development stage
4. Runs the pytest test suite inside the container

### Pipeline Results
![CI Pipeline](https://github.com/PastBenjay/devops-intern-app/actions/workflows/CI.yaml/badge.svg)

## Running Locally

### Prerequisites
- Docker installed
- Git installed

### Steps
```bash
# Clone the repo
git clone https://github.com/PastBenjay/devops-intern-app
cd devops-intern-app

# Build and run
docker build --target production --build-arg NAME=Intern -t python-app ./python-app
docker run python-app
```

## Tech Stack
- **Language:** Python 3.12
- **Testing:** pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
