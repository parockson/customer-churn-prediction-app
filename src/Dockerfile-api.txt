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



# FROM python:3.11.7

# # Install Rust and Cargo
# RUN apt-get update && apt-get install -y curl \
#     && curl https://sh.rustup.rs -sSf | sh -s -- -y \
#     && echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc \
#     && . ~/.bashrc

# # Copy requirements file
# COPY requirements_docker_api.txt /tmp/requirements.txt

# # Update pip
# RUN pip --timeout=30000 install --no-cache-dir --upgrade pip

# # Install dependencies
# #RUN pip --timeout=30000 install --no-cache-dir -r /tmp/requirements.txt

# # Copy API
# #RUN mkdir /src/
# COPY . /app

# # Set workdir
# WORKDIR /app

# # Expose app port
# EXPOSE 9000

# # Start application
# CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "9000"]


# 


# # Use the official Python image from the Docker Hub
# FROM python:3.11.7

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements_docker_api.txt /tmp/requirements.txt

# # Upgrade pip to the latest version and install dependencies
# RUN python -m pip install --no-cache-dir --upgrade pip && \
#     python -m pip install --no-cache-dir -r /tmp/requirements.txt

# # Copy the API source code into the container
# COPY . /app

# # Expose the application port
# EXPOSE 9000

# # Start the application
# CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "9000"]



# Use an official Python runtime as a parent image
FROM python:3.11.7

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements_docker_api.txt /tmp/requirements.txt

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

# Install the dependencies from the requirements file
#RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt
#RUN pip install --no-cache-dir -r /tmp/requirements.txt


# Copy the source code into the container
COPY . /app

# Set the working directory to the source code directory
WORKDIR /app

# Expose the port the application runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
