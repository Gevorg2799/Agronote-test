FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

CMD ["python", "src/app/main.py"]
