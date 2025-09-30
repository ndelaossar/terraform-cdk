#!/usr/bin/env python
import os

from constructs import Construct
from cdktf import App, TerraformStack,TerraformOutput

# We import the "Docker" library to work with Docker resources.
from cdktf_cdktf_provider_docker.provider import DockerProvider
from cdktf_cdktf_provider_docker.image import Image
from cdktf_cdktf_provider_docker.container import Container

# define the path to the Docker socket
current_user = os.getenv("USER")
docker_path = f"/Users/{current_user}/.docker/run/docker.sock"


class MyDockerStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Using the Docker provider to manage Docker resources.
        DockerProvider(self, "Docker",host=f"unix://{docker_path}")

        # Let's grab the latest Nginx image from Docker Hub. 📦
        nginx_image = Image(self, "NginxImage",name="nginx:latest")

        # Now we create a container using that image. 🚢
        nginx_container = Container(self, "NginxContainer",
            name="nginx-server",
            image=nginx_image.repo_digest,
            ports=[{"internal": 80, "external": 8080}]
        )

        # Define outputs to see the results of our work.
        TerraformOutput(self, "container_name",
            value=nginx_container.name,
            description="The name of our running Docker container."
        )


# This starts the magic!
app = App()
MyDockerStack(app, "docker-stack")

app.synth()
