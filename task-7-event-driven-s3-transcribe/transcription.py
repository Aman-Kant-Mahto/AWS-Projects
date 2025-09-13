import json
import boto3

def lambda_handler(event, context):
    transcribe = boto3.client('transcribe')
    s3 = boto3.client('s3')

    # Extracting the bucket name and file name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Transcription job details
    job_name = key.split('.')[0]  # Use the file name without extension
    job_uri = f"s3://{bucket}/{key}"

    # Start transcription job
    response = transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',  # Change as per your audio file format
        LanguageCode='en-US'  # Change as per your audio language
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Transcription job started successfully!')
    }
