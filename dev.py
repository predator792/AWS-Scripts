#!/usr/bin/python
import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='mysecondla7bucket')
