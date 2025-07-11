# Flask REST API – Multi-Cloud Data Transfer

This Flask app uploads a file to both AWS S3 and Azure Blob Storage securely via one API call.

## 🚀 How It Works
- Accepts a POST request with a file.
- Uploads file to:
  - AWS S3 using Boto3
  - Azure Blob using the Azure SDK

## 🔐 Environment Variables
Set the following before running the app:
