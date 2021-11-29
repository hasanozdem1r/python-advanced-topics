# AWS S3 Bucket Data Ingestion


## Prerequisites
1. Amazon Web Services Account
2. AWS SDK (boto3)
3. Python

## Getting Started
Boto3 is the AWS SDK for Python.
Install AWS SDK 
```bash
    pip install boto3
```
Create the IAM User at AWS 
1. Under the Services menu in the AWS Console, navigate to IAM.
2. Under IAM click Users and then click 'Add user'
3. Type your username 'data_pipeline_r_w'
4. Click the type of access for this IAM user. Click 'programmatic access' since this user won't need to log into AWS consolei but rather access AWS resources programmatically via Python scripts.
5. Click Next : Permissions
6. On the “Set permissions” page, click the “Attach existing
policies to user directly” option. Add the AmazonS3Full?
Access policy.
7. Click Next: Tags. It’s a best practice in AWS to add tags to
various objects and services so you can find them later.
This is optional, however.
8. . Click Next: Review to verify your settings. If everything
looks good, click “Create user.”
9. You’ll want to save the access key ID and secret access key
for the new IAM user. To do so, click Download.csv and
then save the file to a safe location so you can use it in just
a moment.

Finally add a section to the pipeline.conf file called [aws_boto_credentials] to store credentials for the IAM user and the S3 bucket.

Pipeline.conf will look as below. <br><br>
[aws_boto_credentials] <br>
access_key = ijfiojr54rg8er8erg8erg8 <br>
secret_key = 5r4f84er4ghrg484eg84re84ger84 <br>
bucket_name = pipeline-bucket <br>
account_id = 4515465518 <br>


