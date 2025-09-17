# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt, if it exists
# If you have a requirements.txt, uncomment the next two lines:
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Install Flask (since app.py uses Flask)
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
