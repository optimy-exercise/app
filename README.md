# Application Repo

## Dockerfile
This Dockerfile sets up the PHP application environment, installs necessary dependencies, and copies the application code into the container.

### Contents:
- **FROM php:7.4-apache**: Base image with PHP and Apache installed.
- **RUN apt-get update && apt-get install -y ...**: Updates package lists and installs necessary PHP extensions and utilities.
- **COPY router.php /var/www/html/**: Copies the PHP application file to the Apache web root directory.

### Usage:
To build and run the Docker image:
```sh
docker build -t php-app .
docker run -d -p 80:80 php-app
```

## router.php
This is the main PHP application file which connects to a MySQL database and displays data from it.

### Key functionalities:
- Connects to the MySQL database using environment variables for configuration.
- Executes a query to fetch data from the `test` table and displays it in an HTML table format.

### Usage:
Place this file in the web root directory of the Apache server in the Docker container.

## CI/CD Pipeline (ci-cd.yml)
This GitHub Actions workflow automates the CI/CD process for building, publishing, and deploying the Docker image, and running tests.

### Pipeline Stages:
1. **Build & Publish Docker Image**:
   - Checks out the code.
   - Builds the Docker image and tags it as `php-app`.
   - Logs in to DockerHub and pushes the image.

2. **Deploy to Server**:
   - Adds SSH key for accessing the server.
   - Pulls the Docker image on the server, stops any running instance of the app, removes it, and runs a new instance.

3. **Test Application**:
   - Installs necessary dependencies and sets up Python.
   - Downloads and sets up ChromeDriver for Selenium.
   - Runs the `testing.py` script to verify the application is working correctly.

### Usage:
The pipeline is triggered on push events to the `main` branch.

## Testing Script (testing.py)
This Python script uses Selenium to perform functional testing of the PHP application.

### Key functionalities:
- Sets up a headless Chrome browser.
- Navigates to the specified URL.
- Verifies the presence of a welcome message and table with expected data.

### Usage:
To run the tests:
```sh
python testing.py <url>
```

## Test Requirements (test_requirements.txt)
This file lists the Python dependencies required for running the tests.

### Contents:
- selenium
- webdriver-manager

### Usage:
To install the dependencies:
```sh
pip install -r test_requirements.txt
```

## Separate Testing Workflow (test.yml)
This GitHub Actions workflow is dedicated to running tests, allowing for manual execution as needed.

### Pipeline Stages:
1. **Setup Python and ChromeDriver**:
   - Installs necessary dependencies.
   - Sets up Python and ChromeDriver for running Selenium tests.

2. **Run Tests**:
   - Executes the `testing.py` script.

### Usage:
The workflow can be triggered manually or integrated into other pipelines.