

# Terraform CDK with Python Examples
This repository provides practical examples of how to use the Cloud Development Kit for Terraform (CDKTF) with Python to manage infrastructure across different environments: AWS (via LocalStack), Docker, and Kubernetes.

## Prerequisites
Before you begin, ensure you have the following tools installed and configured on your system. Using a version manager like nvm for Node.js and tfenv for Terraform is highly recommended.

1. Terraform || tfenv: Manages infrastructure lifecycle.
2. Node.js || nvm: The CDKTF CLI runs on Node.js.
3. Yarn: A package manager for Node.js.

```bash
    brew install yarn
    brew install cdktf
    pip install pipenv
```

## Project Structure
The repository is organized into three distinct stacks, each demonstrating a different use case:

- 📂 aws-stack/: A project to deploy AWS resources (S3 Bucket, EC2 Instance) to a local LocalStack instance.

- 📂 docker-stack/: A project to build a Docker image and run a container on your local machine.

- 📂 kubernetes-stack/: A project to deploy a Kubernetes Namespace, Deployment, and Service to a cluster.

### Getting Started
Follow the instructions below to run each stack. The general workflow is the same for all of them: navigate to the directory, install dependencies, synthesize the code, and deploy.

#### AWS Stack (with LocalStack)
This stack creates an S3 bucket and an EC2 instance in LocalStack.

1. Start LocalStack: Before running the CDKTF commands, make sure your LocalStack Docker container is running.

2. Navigate to the Directory: 
```bash 
    cd aws-stack
```
3. Set up the Environment and Deploy:
```bash
    # Install Python dependencies
    pipenv install

    # Activate the virtual environment
    pipenv shell

    # Download provider bindings
    cdktf get

    # Synthesize your Python code into Terraform JSON
    cdktf synth

    # Deploy the resources to LocalStack
    cdktf deploy
```
4. Clean Up:
```bash
    cdktf destroy
```

#### Docker Stack
This stack pulls the latest nginx image and runs it in a container on your local Docker daemon, exposing port 8080.

1. Start Docker: Ensure your Docker Desktop or Docker daemon is running.

2. Navigate to the Directory:
```bash
    cd docker-stack
```
3. Set up the Environment and Deploy:
```bash
    # Install Python dependencies
    pipenv install

    # Activate the virtual environment
    pipenv shell

    # Download provider bindings
    cdktf get

    # Synthesize the code
    cdktf synth

    # Deploy the container
    cdktf deploy
```
4. Clean Up:
```bash
    cdktf destroy
```

#### Kubernetes Stack
This stack deploys an nginx application into a Kubernetes cluster using a Namespace, Deployment, and a NodePort Service.

1. Configure Kubernetes: Ensure your kubectl is configured to point to the desired cluster (e.g., Minikube, Docker Desktop Kubernetes, or a cloud-based cluster).

2. Navigate to the Directory:
```bash
    cd kubernetes-stack
```
3. Set up the Environment and Deploy:
```bash
    # Install Python dependencies
    pipenv install

    # Activate the virtual environment
    pipenv shell

    # Download provider bindings
    cdktf get

    # Synthesize the code
    cdktf synth

    # Deploy the resources to your cluster
    cdktf deploy
```
4. Clean Up:
```bash
    cdktf destroy
```