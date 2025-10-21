# DonXEra Inventory Manager - Docker Image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry==1.7.1

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Configure Poetry to not create a virtual environment in Docker
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-root --only main

# Copy application files
COPY . .

# Set Python path to include src/
ENV PYTHONPATH=/app/src

# Set environment variables for demo mode
ENV DEMO_MODE=true
ENV PORT=8000
ENV FLASK_ENV=production

# Expose port
EXPOSE 8000

# Run with gunicorn via Poetry
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "--chdir", "/app/scripts", "run_local:app"]
