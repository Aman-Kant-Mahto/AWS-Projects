# 📤 Upload to S3 Without Logging into AWS

## Introduction
Sometimes you need to upload files to Amazon S3 without giving users full AWS credentials.  
This project demonstrates how to achieve this securely using **pre-signed URLs** and IAM policies.

## Objectives
- Explore alternative S3 upload methods.
- Learn to generate pre-signed URLs with boto3.
- Understand security best practices.

## Steps
1. Use `boto3` or AWS CLI to create a pre-signed URL.
2. Share the URL with a client or app for upload access.
3. Validate file upload without direct AWS login.

## Blog Link
🔗 [Uploading Objects to S3 Without Login](https://www.linkedin.com/posts/aman-kant-mahto_uploading-objects-to-amazon-s3-bucket-without-activity-7253298414266765313-saus)

## Conclusion
Pre-signed URLs enable **secure, temporary access** to S3 objects, ideal for apps or public file-sharing workflows.
