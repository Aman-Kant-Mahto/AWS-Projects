import boto3

# Initialize a session using Amazon CloudWatch Logs
client = boto3.client('logs')

# Specify the log group name and log stream name
log_group_name = '/aws/lambda/my-log-group'  # Replace with your log group
log_stream_name = 'my-log-stream'  # Replace with your log stream

# Function to get logs from CloudWatch
def get_cloudwatch_logs(log_group_name, log_stream_name):
    try:
        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startFromHead=True  # Set to False if you want the latest logs first
        )

        # Print out the logs
        for event in response['events']:
            print(event['message'])

    except Exception as e:
        print(f"Error retrieving logs: {e}")

# Call the function
get_cloudwatch_logs(log_group_name, log_stream_name)
