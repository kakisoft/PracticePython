import boto.ec2

aws_region = "us-west-2"
conn = boto.ec2.connect_to_region(region_name=aws_region)
