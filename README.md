# Data Analytics Framework for GAP Package Management

## Description

This project is completed as part of the CS5099: Dissertation in Computer Science module with the University of St Andrews, under the supervision of Dr. Olexandr Konovalov. The framework aims to be a tool to individuals interested in the development, distribution and community behind GAP - a programming language for computational discrete algebra.

## Prerequisites

- The program requires Python version 3.8 or higher.
- Running the program also requires Jupyter Notebook.
- Using the framework requires a GitHub token. To retrieve data, generate a personal token from within your [GitHub Tokens settings](https://github.com/settings/tokens).
- Make sure the GitHub token is saved in a hidden file with the name `~/.github_shell_token` in your home directory, or accessible through an environmental variable if using Docker.

## Installation

1. Clone the repository to your machine.
2. Install required libraries by running the following command:
   > `pip install -r requirements.txt`

## Usage

Open the project in your preferred Jupyter Notebook environment. The program can also be executed through Docker, as described further down in this file. The framework is composed of several Python files and Jupyter Notebooks, where the Python files are not intended to be modified. Retrieving, analysing and visualising the data can be done solely through interacting with files in the _notebooks_ folder. This folder has four files for data retrieval, one for data analysis and one for data visualisation, all named to reflect the order in which they are intended to be executed:

1. Data Retrieval:

- `01_get_repo_data.ipynb`: Retrieves data in regards to repository analysis and visualisation. It is concerned with statistical analysis of the individual repositories hosted by GAP on GitHub.
- `02_get_monitoring_data.ipynb`: Retrieves data in regards to monitoring the current state of GAP from a distribution and redistribution perspective. It is concerned with metrics related to the GAP package distribution repository on GitHub.
- `03_get_testing_data.ipynb`: Retrieves data in regards to tested versions, required version and GitHub Actions for the GAP package repositories. It pulls data on logic, consistency and discrepancies related to GAP versions for the given package.
- `04_get_community_data.ipynb`: Retrieves data in regards to the GAP community, retrieving data related to authors, issue submitters and collaboration, investigating trends and interactions.

2. Data Analysis:

- `05_data_analysis.ipynb`: Accesses the retrieved data from the `collected_data` folder, and uses it to output findings. Primarily concerned with the bigger picture and analytical outputs in text format.
- It is important that you **save the file** after running the notebook, to make the outputs available in the Streamlit dashboard.

3. Data Visualisation:

- `06_data_visualisation.ipynb`: Accesses the retrieved data from the `collected_data` folder, and uses it to visualise findings. Primarily concerned with data that is easier explained and interpreted when visualised.
- It is important that you **save the file** after running the notebook, to make the outputs available in the Streamlit dashboard.

4. Interacting with Dashboard:

- To interact with the project Streamlit dashboard, run the following command in the terminal to start the server:
  > `streamlit run dashboard.py`
- Once the Streamlit server is running, you can access the dashboard by opening the URL provided in the terminal. If you want to make any changes or additions to the dashboard, Streamlit provides live reload, which automatically detects changes in the script and updates the dashboard in real-time.
- The dashboard allows for downloading outputs, as well as uploading other notebooks of identical style to display outputs. Downloaded outputs will be saved to a project folder created upon download, called `downloaded_data`.

## Running the Framework with Docker

- To run the framework usiong Docker, you first need to install Docker on your system if you have not already done so. Docker can be downloaded and installed from the [Docker Website](https://www.docker.com/get-started/).
- Additionally, the GitHub token must be stored in the project, as it will not be accessible from the home directory when using Docker. An `.env` file has already been added to the project. In the file, add the GitHub token by replacing `YOUR_GITHUB_TOKEN` with the actual GitHub token value:
- The project directory already contains a Docker file, which can be used to create a Docker image. Once the repository is cloned to your local machine, you can build the Docker image using the following command in the terminal:
  > `docker build -t gap_data_analysis .`
- Having created the Docker image, you can access the program as a Docker container by running the following command in the terminal:
  > `docker run -p 8888:8888 --env-file .env gap_data_analysis`
- Running this will initiate a Docker container mapped to the JupyterLab environment, accessible from port 8888 on the local host machine.
- Terminating the container environment in JupyterLab can be done by using the `Ctrl+C` keys, or by running the following command in the terminal, replacing the _container_id_ with the actual id of the container:
  > `docker stop container_id`

## Additional Documentation

- [GAP Organisation Website](https://www.gap-system.org/): Webpage of the GAP organisation, containing installation instructions, data libraries, package overview, documentation and contact information.
- [All GAP Pacakges](https://gap-packages.github.io/): Complete list of all GAP packages, including where they are hosted and how they are maintained.
- [The PyGitHub Project](https://pypi.org/project/PyGithub/): Description of the PyGitHub project, containing a short tutorial describing its usage and how to access GitHub objects.
- [GitHub REST API Documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28): Contains information on how to use the REST API, including GitHub based integrations, data retrieval and workflow automation.
- [GitHub Objects and Syntax](https://pygithub.readthedocs.io/en/latest/github_objects.html): Overview on how to work with GitHub objects, describing types, classes, methods, parameters and return types.
