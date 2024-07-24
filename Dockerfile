# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# Define the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
