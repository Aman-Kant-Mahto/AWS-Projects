import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        s3_client.upload_file(file_name, bucket, object_name)
        print(f'Successfully uploaded {file_name} to {bucket}/{object_name}')
    except FileNotFoundError:
        print(f'The file {file_name} was not found')
    except NoCredentialsError:
        print('Credentials not available')

# Usage example
upload_to_s3('path/to/your/file.txt', 'your-s3-bucket-name', 'optional/object_name.txt')
