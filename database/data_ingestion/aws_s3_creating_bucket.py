"""
This script is created with of support of AWS Docs to show you how to create a bucket in best way
@ Hasan Özdemir 01/10/2022
"""

# Check  docs/aws_s3_data_ingestion.md
# install boto3 -> pip install boto3
import boto3

# The name of an Amazon S3 bucket must be unique across all regions of the AWS platform

import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region
    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).
    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# List all the existing buckets for the AWS account.
# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')