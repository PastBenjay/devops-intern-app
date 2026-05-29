# =============================================================
# Stage 1: Development
# Using official Python 3.12 slim image from Docker Official Images
# Includes development and testing dependencies
# =============================================================
FROM python:3.12-slim AS development

# Set working directory inside container
WORKDIR /app

# Build argument with default value
ARG NAME=Intern

# Set NAME as environment variable
ENV NAME=${NAME}

# Copy dependency definition first for better Docker caching
COPY pyproject.toml .

# Install application + development dependencies
RUN pip install --no-cache-dir ".[dev]"

# Copy application source code
COPY app.py .

# Copy tests for development/testing stage
COPY tests/ tests/

# Default command to run the application
CMD ["python", "app.py"]

# =============================================================
# Stage 2: Production
# Lightweight production image without test dependencies
# =============================================================
FROM python:3.12-slim AS production

# Set working directory
WORKDIR /app

# Build argument
ARG NAME=Intern

# Environment variable
ENV NAME=${NAME}

# Copy dependency file
COPY pyproject.toml .

# Install only production dependencies
RUN pip install --no-cache-dir .

# Copy only required application file
COPY app.py .

# Run application
CMD ["python", "app.py"]
```
