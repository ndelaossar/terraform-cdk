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
  #### Docker
  - cdktf init --template=python --providers=kreuzwerker/docker --local
  #### Kubernetes
  cdktf init --template=python \
             --project-name=terraform-cdk \
             --project-description="Learn how to develop CDKTF applications" \
             --providers="kubernetes@~>2.14" \
             --local
