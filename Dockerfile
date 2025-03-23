# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for Flask (5000) and Streamlit (8501)
EXPOSE 5000
EXPOSE 8501

# Start both Flask API and Streamlit app using a process manager
CMD ["sh", "-c", "python api.py & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
