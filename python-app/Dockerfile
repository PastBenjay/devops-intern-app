FROM python:3.12-slim AS base

WORKDIR /app
COPY pyproject.toml .
COPY app.py .
COPY tests/ tests/
RUN pip install --no-cache-dir ".[dev]"

FROM base AS test
RUN python -m pytest tests/test_app.py -v

FROM base AS final
ENV NAME=Intern
CMD ["python", "app.py"]
