# Use Jupyter base image for Docker, a minimal Jupyter Notebook environment
# The pre-built image already contains the setup for both Python and Jupyter Notebook
FROM jupyter/base-notebook

# Set the working dir to 'app' for copying project files into the container
# All commands in the Dockerfile must then be executed from the 'app' directory
WORKDIR /app

# Copy all files from local project dir to container's working dir
# This is what makes the project files available inside the Docker container
COPY --chown=${NB_UID} . /app

# Install the required dependencies for the framework
RUN pip install -r requirements.txt

# Change the owner of the files to 'jovyan' and set permissions
# This is the default user for running Jupyter images, to avoid running as root user
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

# Set the user and group for the Jupyter environment
USER ${NB_UID}:${NB_UID}

# Start the container with Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]