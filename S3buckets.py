#!/usr/bin/python
import boto3
import sys
import botocore
action= sys.argv[1]
bucket= sys.arg[2]
s3_client= boto3.client('s3')

if action == "create-bucket":
 print "creating bucket"
 s3_client.create_bucket(bucket=bucket_name)
