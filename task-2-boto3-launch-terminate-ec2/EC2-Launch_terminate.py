import boto3

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Specify your AWS region

# Launch an EC2 instance
def launch_instance():
    try:
        response = ec2.run_instances(
            ImageId='ami-0c55b159cbfafe1f0',  # Example Amazon Linux 2 AMI
            InstanceType='t2.micro',  # Free tier eligible instance type
            KeyName='your-key-pair',  # Replace with your key pair
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'MyBoto3Instance'}  # Optional tag for your instance
                    ]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f'Instance launched, ID: {instance_id}')
        return instance_id
    except Exception as e:
        print(f'Error launching instance: {e}')

if __name__ == "__main__":
    instance_id = launch_instance()
