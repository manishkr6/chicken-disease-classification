FROM python:3.11.9-slim

WORKDIR /app

# Copy requirements file first for better cache on build
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python3", "app.py"]
