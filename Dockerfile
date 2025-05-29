FROM python:3.11

WORKDIR /app

# Install Redis server and dependencies
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose ports
EXPOSE 3000

ENTRYPOINT ["/entrypoint.sh"]
