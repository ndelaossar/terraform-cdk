#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack,TerraformOutput

from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket

class MyAwsStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        # Using the AWS provider to manage AWS resources. In this case, we're connecting to LocalStack.
        AwsProvider(self, "aws",
                region="us-east-1",  # Or any region, LocalStack doesn't strictly enforce
                access_key="test",
                secret_key="test",
                skip_credentials_validation=True,
                skip_metadata_api_check=True,
                skip_requesting_account_id=True,
                endpoints=[
                    {
                        "s3": "http://localhost:4566",
                        "ec2": "http://localhost:4566",
                        "sts": "http://localhost:4566"
                    }
                ]
            )

        # Create an S3 bucket
        bucket = S3Bucket(self, "MyBucket",
            bucket="my-aws-cdktf-bucket-123456"  # Bucket names must be globally unique
        )

        # Create an EC2 instance
        instance = Instance(self, "MyInstance",
            ami="ami-12345678",
            instance_type="t2.micro"
        )

        # Output the bucket name and instance ID
        TerraformOutput(self, "bucket_name",
            value=bucket.id
        )
        TerraformOutput(self, "instance_id",
            value=instance.id
        )


app = App()
MyAwsStack(app, "aws-stack")

app.synth()
