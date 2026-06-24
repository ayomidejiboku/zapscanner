FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app and bad.py
COPY . .

# Run the vulnerable app
CMD ["python", "app.py"]
