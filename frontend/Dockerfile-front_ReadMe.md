# FROM python:3.11.7

# # Copy requirements file
# COPY requirements_docker_api.txt .

# # Update pip
# RUN pip --timeout=30000 install --no-cache-dir --upgrade pip

# # Install dependecies
# RUN pip --timeout=30000 install --no-cache-dir -r requirements_docker_api.txt

# # Copy API
# RUN mkdir /src/
# COPY ./src /src

# # Set workdir
# WORKDIR /

# # Expose app port
# EXPOSE 9000

# # Start application
# CMD ["uvicorn", "src/api.api:app", "--host", "0.0.0.0", "--port", "9000"]





# Use the official Python image from the Docker Hub
FROM python:3.11.7


# Copy the requirements file into the container at /app
COPY requirements_docker_streamlit.txt /tmp/requirements.txt

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip

# Install the dependencies from the requirements file
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the API source code into the container at 
COPY . /app

# Set the working directory in the container
WORKDIR /app

# # Create a directory for the API source code
# RUN mkdir /app/src


# Expose the application port
EXPOSE 3030

# Start the application
CMD ["streamlit", "run", "main.py", "--server.port=8501"]
