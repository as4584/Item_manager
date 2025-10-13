# DonXEra Inventory Manager - Docker Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables for demo mode
ENV DEMO_MODE=true
ENV PORT=8080
ENV FLASK_ENV=production

# Expose port
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]
