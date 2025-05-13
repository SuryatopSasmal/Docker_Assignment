# Use the official Python image
FROM python:3.9

# Install Flask
RUN pip install flask

# Set working directory and copy files
WORKDIR /app
COPY main.py /app/main.py

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
