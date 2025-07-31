# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Telegram bot
CMD ["python", "bot.py"]