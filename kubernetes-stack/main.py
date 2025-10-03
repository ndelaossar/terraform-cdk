#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
# Import the Kubernetes provider, Deployment, and Service resources
from cdktf_cdktf_provider_kubernetes import deployment, service, provider, namespace

class MyK8sStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Configure the Kubernetes provider
        provider.KubernetesProvider(self, "kubernetes",
            config_path="~/.kube/config"  # Path to your kubeconfig file
            # You might need to configure kubeconfig or other authentication methods here
        )

        # Labels for the application
        app_labels = {"app": "web-app"}
        
        # Define a Kubernetes Namespace
        web_app_namespace = namespace.Namespace(self, "webAppNamespace",
            metadata=namespace.NamespaceMetadata(
                name="web-app"
            )
        )
        # Define a Kubernetes Deployment
        web_app_deployment = deployment.Deployment(self, "webAppDeployment",
            metadata=deployment.DeploymentMetadata(
                name="web-app-deployment",
                labels=app_labels,
                namespace=web_app_namespace.metadata.name
            ),
            spec=deployment.DeploymentSpec(
                replicas="2",
                selector=deployment.DeploymentSpecSelector(match_labels=app_labels),
                template=deployment.DeploymentSpecTemplate(
                    metadata=deployment.DeploymentSpecTemplateMetadata(labels=app_labels),
                    spec=deployment.DeploymentSpecTemplateSpec(
                        container=[
                            deployment.DeploymentSpecTemplateSpecContainer(
                                name="web-app-container",
                                image="nginx:latest",
                                port=[
                                    deployment.DeploymentSpecTemplateSpecContainerPort(container_port=80)
                                ]
                            )
                        ]
                    )
                )
            )
        )

        # Define a Kubernetes Service
        web_app_service = service.Service(self, "webAppService",
            metadata=service.ServiceMetadata(
                name="web-app-service",
                labels=app_labels,
                namespace=web_app_namespace.metadata.name
            ),
            spec=service.ServiceSpec(
                selector=app_labels,
                port=[
                    service.ServiceSpecPort(
                        port=80,
                        target_port="80",
                        node_port=30080
                    )
                ],
                type="NodePort"
            )
        )

app = App()
MyK8sStack(app, "kubernetes-stack")
app.synth()