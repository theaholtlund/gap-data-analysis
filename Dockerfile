# Use Jupyter base image for Docker, a minimal Jupyter Notebook environment
# The pre-built image already contains the setup for both Python and Jupyter Notebook
FROM jupyter/minimal-notebook

# Set the working dir to 'app' for copying project files into the container
# All commands in the Dockerfile must then be executed from the 'app' directory
WORKDIR /app

# Give users permission to read, write and execute files in the 'app' dir
# All users will have individual Docker images, and can manage settings appropriately
RUN chmod -R a+rwx /app

# Copy all files from local project dir to container's working dir
# This is what makes the project files available inside the Docker container
COPY . /app

# Install the required dependencies for the framework
RUN pip install -r requirements.txt

# Start the container with Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]