# =============================================================
# Stage 1: Development
# Using official Python 3.12 slim image - lightweight but full
# featured, sourced from Docker Official Image on DockerHub
# =============================================================
FROM python:3.12-slim AS development

# Set working directory inside the container
WORKDIR /app

# Accept NAME as a build argument with default value of Intern
ARG NAME=Intern

# Set NAME as an environment variable so the app can access it
ENV NAME=${NAME}

# Copy dependency file first for better layer caching
COPY pyproject.toml .

# Install all dependencies including dev/test dependencies (pytest)
RUN pip install --no-cache-dir ".[dev]"

# Copy application source code
COPY app.py .

# Copy tests folder - needed in development for running tests
COPY tests/ tests/

# Run the application using Python
CMD ["python", "app.py"]

# =============================================================
# Stage 2: Production
# Builds on development stage but excludes tests
# Uses slim image for minimal size
# =============================================================
FROM python:3.12-slim AS production

# Set working directory
WORKDIR /app

# Accept and set NAME build argument
ARG NAME=Intern
ENV NAME=${NAME}

# Copy only the dependency file
COPY pyproject.toml .

# Install only production dependencies, no dev/test packages
RUN pip install --no-cache-dir .

# Copy only the application code - NO tests folder
COPY app.py .

# Run the application
CMD ["python", "app.py"]
