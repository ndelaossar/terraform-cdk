# Terraform CDK 

### Prerequisites 
  - Terraform / tfvenv
  - node /nvm
  - brew install yarm
  - brew install cdktf
  - pip install pipenv

 ###  Initialize a new CDK for Terraform application
  #### AWS
  - cdktf init --template="python" --providers="aws@~>4.0"
  - pip install cdktf-cdktf-provider-aws
  - pipenv install cdktf-cdktf-provider-aws
  #### Docker
  cdktf init --template=python \
             --project-name=terraform-cdk-docker \
             --project-description="How to Deploy a Kubernetes Service" \
             --providers="Docker" \
             --local
  #### Kubernetes
  cdktf init --template=python \
             --project-name=terraform-cdk-kubenetes \
             --project-description="How to Deploy a Kubernetes Service" \
             --providers="Kubernetes" \
             --local
  #### cdktf get - download modules