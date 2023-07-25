# Data Analytics Framework for GAP Package Management

## Description

This project is completed as part of the CS5099: Dissertation in Computer Science module with the University of St Andrews, with Dr. Olexandr Konovalov supervising the project. The framework is created with the aim of providing a useful tool to individuals interested in the developments, distribution and community of GAP - a programming language concerned with computational discrete algebra.

## Installation

- The program requires Python. All required libraries can be installed through the requirements.txt file, by running the following command in the terminal:
  `pip install -r requirements.txt`
- Using the framework requires a GitHub token. To retrieve data, generate a personal token from within your [GitHub Tokens settings](https://github.com/settings/tokens).

## Usage

Make sure the GitHub token is saved in a hidden file with the name `~/.github_shell_token` in your home directory. Clone the project to your local directory, and open it in your preferred IDE or Jupyter Notebook environment. The program can also be accessed through Docker, as described further down in this file.

## Framework Contents

The analytical framework is composed of several files and Jupyter Notebooks. To retrieve the data, analyse its contents and visualise key relations, only the notebooks in the _notebooks_ folder. This folder has four files for data retrieval, one for data analysis and one for data visualisation, all named to reflect the order in which they are intended to be executed:

1. 01_get_repo_data.ipynb: This file contains functions to retrieve the necessary data in regards to repository analysis and visualisation. It is concerned with statistical analysis of the individual repositories hosted by GAP on GitHub.
2. 02_get_monitoring_data.ipynb: This file contains functions to retrieve the necessary data in regards to monitoring the current state of GAP from a distribution and redistribution perspective. It is concerned with metrics related to the GAP package distribution repository on GitHub.
3. 03_get_testing_data.ipynb: This file contains functions to retrieve the necessary data in regards to tested versions, required version and GitHub Actions for the GAP package repositories. It pulls data on logic, consistency and discrepancies related to GAP versions for the given package.
4. 04_get_community_data.ipynb: This file contains functions to retrieve the necessary data in regards to the GAP community, retrieving data related to authors, issue submitters and collaboration, investigating trends and interactions.
5. 05_data_analysis.ipynb: This file accesses the retrieved data from the _collected_data_ folder, and uses it to output interesting and noteworthy findings. It is primarily concerned with the bigger picture and situations that could be of concern to individuals managing or redistributing GAP.
6. 06_data_visualisation.ipynb: This file accesses the retrieved data from the _collected_data_ folder, and uses it to visualise key findings in terms of trends and collaboration patterns. It is primarily concerned with data that is better interpreted when visualised, such as volume, contribution frequency and interaction networks.

## Running the Framework with Docker

- To run the framework usiong Docker, you first need to install Docker on your system if you have not already done so. Docker can be downloaded and installed from the [Docker Website](https://www.docker.com/get-started/).
- The project directory already contains a Docker file, which can be used to create a Docker image. Once the repository is clones to your local machine, you can build the Docker image using the following command in the terminal:
  `docker build -t gap_data_analysis .`
- Having created the Docker image, you can access the program as a Docker container by running the following command in the terminal:
  `docker run -p 8888:8888 gap_data_analysis`
- Running this will initiate a Docker container mapped to the JupyterLab environment, accessible from port 8888 on the local host machine. The link to open the the JupyterLab in your web browser can be found in the terminal.
- Terminating the container environment in JupyterLab can be done by running the following command in the terminal:
  `docker stop container_id`
  replacing the _container_id_ with the actual container_id of the container. The program can also be terminated by using the `Ctrl+C` keys.
