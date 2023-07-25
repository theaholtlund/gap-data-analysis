# Data Analytics Framework for GAP Package Management

## Description

This project is completed as part of the CS5099: Dissertation in Computer Science module with the University of St Andrews, with Dr. Olexandr Konovalov supervising the project. The framework is created with the aim of providing a useful tool to individuals interested in the developments, distribution and community of GAP - a programming language concerned with computational discrete algebra.

## Prerequisites

- The program requires Python version 3.8 or higher.
- Running the program also requires Jupyter Notebook.
- Using the framework requires a GitHub token. To retrieve data, generate a personal token from within your [GitHub Tokens settings](https://github.com/settings/tokens).
- Make sure the GitHub token is saved in a hidden file with the name `~/.github_shell_token` in your home directory.

## Installation

1. Clone the code repository to your local machine.
2. Install required libraries by running the following command in the terminal:
   > `pip install -r requirements.txt`

## Usage

With the project opened in your preferred IDE or Jupyter Notebook environment, it can be used for computational analysis related to GAP packages. The program can also be executed through Docker, as described further down in this file. The framework is composed of several Python files and Jupyter Notebooks, where the Python files are not intended to be accessed or modified in order to run the program. To retrieve the data, analyse its contents and visualise key relations, only the notebooks in the _notebooks_ folder are needed. This folder has four files for data retrieval, one for data analysis and one for data visualisation, all named to reflect the order in which they are intended to be executed:

1. Date Retrieval:

   - 01_get_repo_data.ipynb: This file contains functions to retrieve the necessary data in regards to repository analysis and visualisation. It is concerned with statistical analysis of the individual repositories hosted by GAP on GitHub.
   - 02_get_monitoring_data.ipynb: This file contains functions to retrieve the necessary data in regards to monitoring the current state of GAP from a distribution and redistribution perspective. It is concerned with metrics related to the GAP package distribution repository on GitHub.
   - 03_get_testing_data.ipynb: This file contains functions to retrieve the necessary data in regards to tested versions, required version and GitHub Actions for the GAP package repositories. It pulls data on logic, consistency and discrepancies related to GAP versions for the given package.
   - 04_get_community_data.ipynb: This file contains functions to retrieve the necessary data in regards to the GAP community, retrieving data related to authors, issue submitters and collaboration, investigating trends and interactions.

2. Data Analysis:

   - 05_data_analysis.ipynb: This file accesses the retrieved data from the _collected_data_ folder, and uses it to output interesting and noteworthy findings. It is primarily concerned with the bigger picture and situations that could be of concern to individuals managing or redistributing GAP.

3. Data Visualisation:
   - 06_data_visualisation.ipynb: This file accesses the retrieved data from the _collected_data_ folder, and uses it to visualise key findings in terms of trends and collaboration patterns. It is primarily concerned with data that is better interpreted when visualised, such as volume, contribution frequency and interaction networks.

## Running the Framework with Docker

- To run the framework usiong Docker, you first need to install Docker on your system if you have not already done so. Docker can be downloaded and installed from the [Docker Website](https://www.docker.com/get-started/).
- Additionally, the GitHub token must be stored in the project, as it will not be accessible from the home directory when using Docker. An `.env` file has already been added to the project, and to the .gitignore file to ensure it is not accidentally added to any Git repositories, as this is sensitive data that should be kept private and protected like a password. In the file, add your GitHub token by adding the following code in the file and saving it, replacing _YOUR_GITHUB_TOKEN_ with the actual GitHub token:
  > `GITHUB_TOKEN=YOUR_GITHUB_TOKEN`
- The project directory already contains a Docker file, which can be used to create a Docker image. Once the repository is clones to your local machine, you can build the Docker image using the following command in the terminal:
  > `docker build -t gap_data_analysis .`
- Having created the Docker image, you can access the program as a Docker container by running the following command in the terminal:
  > `docker run -p 8888:8888 --env-file .env gap_data_analysis`
- Running this will initiate a Docker container mapped to the JupyterLab environment, accessible from port 8888 on the local host machine. The link to open the the JupyterLab in your web browser can be found in the terminal.
- All running containers, along with the conatiner's name and id, can be found by running the following command in the terminal:
  > `docker ps`
- Terminating the container environment in JupyterLab can be done by using the `Ctrl+C` keys, or by running the following command in the terminal, replacing the _container_id_ with the actual id of the container:
  > `docker stop container_id`

## Additional Documentation

- [GAP Organisation Website](https://www.gap-system.org/): Webpage of the GAP organisation, containing installation instructions, data libraries, package overview, documentation and contact information.
- [All GAP Pacakges](https://gap-packages.github.io/): Complete list of all GAP packages, including where they are hosted and how they are maintained.
- [The PyGitHub Project](https://pypi.org/project/PyGithub/): Description of the PyGitHub project, containing a short tutorial describing its usage and how to access GitHub objects.
- [GitHub REST API Documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28): Contains information on how to use the REST API, including GitHub based integrations, data retrieval and workflow automation.
- [GitHub Objects and Syntax](https://pygithub.readthedocs.io/en/latest/github_objects.html): Overview on how to work with GitHub objects, describing types, classes, methods, parameters and return types.
