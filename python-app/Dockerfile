FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY app.py .
COPY tests/ tests/

RUN pip install --no-cache-dir ".[dev]"

ENV NAME=Intern

CMD ["python", "app.py"]