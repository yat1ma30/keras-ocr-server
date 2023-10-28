# Choose the base image
FROM python:3.11-slim

# Install the necessary libraries
RUN apt-get update
RUN apt-get install -y libgl1 libglib2.0-0
RUN update-ca-certificates --fresh
ENV SSL_CERT_DIR=/etc/ssl/certs

# Set the working directory
WORKDIR /app

# Install the necessary libraries
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN sed -i '/tensorflow-intel==/d' /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the server code and model data
COPY server.py /app

# Run the Flask application
CMD ["python", "server.py"]
