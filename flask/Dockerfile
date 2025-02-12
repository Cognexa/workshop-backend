# Use official Python image as the base image
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
