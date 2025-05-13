# python-module/fetch_configs.py

import boto3  # For AWS example – similar libraries exist for Azure/GCP
import json

def fetch_aws_configurations():
    client = boto3.client('ec2', region_name='us-east-1')  # Customize region as needed
    # Fetch details for EC2 instances; expand as required.
    instances = client.describe_instances()
    # Process output (convert to dict, clean data)
    config_data = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            config_data.append({
                "InstanceId": instance.get("InstanceId"),
                "State": instance.get("State", {}).get("Name"),
                "KeyName": instance.get("KeyName"),
                "PublicIpAddress": instance.get("PublicIpAddress"),
                # … include additional relevant configurations
            })
    return config_data

if __name__ == "__main__":
    configs = fetch_aws_configurations()
    print(json.dumps(configs, indent=2))
