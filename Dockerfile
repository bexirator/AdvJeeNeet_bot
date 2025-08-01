# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all local files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for UTF-8 encoding
ENV PYTHONUNBUFFERED=1

# Run the Telegram bot
CMD ["python", "bot.py"]
