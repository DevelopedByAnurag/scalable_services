# Deploying a Flask Application with Docker

## Introduction

This documentation provides a step-by-step guide on how to deploy a Flask application using Docker. By containerizing the application, Docker simplifies the deployment process and automates the setup across different environments. We will demonstrate this using a sample Flask application with three API endpoints.

### Application Overview

The sample Flask application consists of the following API endpoints:

1. `/greet`: Greets the specified user.
2. `/save_name`: Saves the name sent using a POST request to the MongoDB Atlas collection.
3. `/fetch_names`: Fetches the list of names from the MongoDB Atlas collection.

## Prerequisites

Before proceeding with the deployment process, ensure that you have the following prerequisites:

1. Docker installed on your machine. You can download it from the official Docker website: [https://www.docker.com/](https://www.docker.com/).
2. A MongoDB Atlas account to host the database. You can sign up for free at [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas).

## Deployment Steps

Follow the steps below to deploy the Flask application using Docker and understand how Docker simplifies and automates the deployment process:

### Step 1: Set Up the Flask Application

1. Clone the application repository from the provided source code.

2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the MongoDB Atlas connection details in the Flask application code.

### Step 2: Dockerize the Flask Application

1. Create a file named `Dockerfile` in the root directory of the Flask application.

2. Open the `Dockerfile` and add the following content:

   ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.8-slim-buster

    # Set the working directory in the container to /app
    WORKDIR /app

    # Add the current directory contents into the container at /app
    ADD . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install flask pymongo

    # Make port 4540 available to the world outside this container
    EXPOSE 4540

    # Run app.py when the container launches
    CMD ["python", "app.py"]
   ```

   The Dockerfile specifies the base image, sets the working directory, copies the requirements file, installs dependencies, copies the Flask application code, exposes the application port, and defines the startup command.

3. Save the `Dockerfile`.

### Step 3: Build the Docker Image

1. Open a terminal or command prompt.

2. Navigate to the root directory of the Flask application.

3. Build the Docker image using the following command:

   ```bash
   docker build -t anuragbatra706/scalable_api:latest .
   ```

   The `-t` flag tags the image with the name `flask-app`.

   Docker simplifies the build process by automating the creation of an image containing all the necessary dependencies and configurations.

### Step 4: Set Up MongoDB Atlas

1. Sign in to your MongoDB Atlas account.

2. Create a new cluster and note the connection details.

   Docker simplifies the setup process by encapsulating the application's dependencies within the container, removing the need to install and configure MongoDB separately on the host machine.

### Step 5: Create a Docker Compose File

1. Create a file named `docker-compose.yml` in the root directory of the Flask application.

2. Open the `docker-compose.yml` file and add the following

 content:

   ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-flask-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-flask-app
      template:
        metadata:
          labels:
            app: my-flask-app
        spec:
          containers:
          - name: my-flask-app
            image: my-flask-app:latest
            ports:
            - containerPort: 4540
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: my-flask-app-service
    spec:
      selector:
        app: my-flask-app
      ports:
        - protocol: TCP
          port: 80
          targetPort: 4540
      type: LoadBalancer
   ```

   The Docker Compose file defines the services required for the application. In this case, we have one service named `app` that builds the image using the `Dockerfile`, maps the container port to the host port, and sets the MongoDB Atlas connection URI as an environment variable.

   Docker Compose simplifies the orchestration and networking of multiple containers by allowing you to define and manage the services as a single entity.

3. Save the `docker-compose.yml` file.

### Step 6: Deploy the Application

1. Open a terminal or command prompt.

2. Navigate to the root directory of the Flask application.

3. Run the following command to start the application:

   ```bash
   docker-compose up
   ```

   Docker Compose automates the deployment process by creating and running the necessary containers based on the defined services. The Flask application will be accessible at [http://localhost:5000](http://localhost:5000).

   Docker simplifies the deployment process by providing a consistent environment for running the application across different machines. This eliminates the need to manually install dependencies or configure the environment on each host.
