# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000  
EXPOSE 8501  
# Command to run the Flask backend
CMD ["python", "appi.py"]