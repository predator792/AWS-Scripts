#!/usr/bin/python
from boto3.session import Session
session= Session(aws_access_key_id='USEMYID', aws_secret_access_key='USEYOURACCESSKEYS')
s3 =session.resource('s3')
s3.create_bucket=('myfirstlabucket7')
