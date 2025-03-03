# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt to the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . /app

EXPOSE 8080

CMD ["gunicorn", "-b", ":8080", "app.main:app", "-k", "uvicorn.workers.UvicornWorker"]

