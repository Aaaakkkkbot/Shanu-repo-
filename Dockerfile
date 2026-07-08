FROM python:3.11-slim-bullseye

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install git, gcc and other needed build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends git gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools wheel

# Copy application code
COPY . /app/

# Set working directory
WORKDIR /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python3", "-m", "TEAMZYRO"]
