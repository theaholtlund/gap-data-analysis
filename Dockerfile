# Use Jupyter base image for Docker, a miniwhamal Jupyter Notebook environment
# The pre-built image already contains the setup for both Python and Jupyter Notebook
FROM jupyter/minimal-notebook

# Set the working dir to 'app' for copying project files into the container
# All commands in the Dockerfile must then be executed from the 'app' directory
WORKDIR /app

# Copy all files from local project dir to container's working dir
# This is what makes the project files available inside the Docker container
COPY . /app

# Install the required dependencies for the framework
RUN pip install -r requirements.txt