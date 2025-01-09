# filepath: /API/Dockerfile
FROM python:3.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3 python3-pip

# Set the working directory
WORKDIR /API

# Copy requirements.txt
COPY requeriments.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requeriments.txt

# Copy the rest of the application code
COPY . .

COPY images/image_uploaded.jpg /API/images/image_uploaded.jpg

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "servico1.py"]  # Ensure this matches your main application file
