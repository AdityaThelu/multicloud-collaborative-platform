from flask import Flask, request
import boto3
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = file.read()

    # Upload to AWS S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name='us-east-1'
    )
    s3.put_object(Bucket='my-multicloud-bucket', Key=file.filename, Body=content)

    # Upload to Azure Blob
    blob_service = BlobServiceClient.from_connection_string(os.environ['AZURE_CONN_STRING'])
    container_client = blob_service.get_container_client('mycontainer')
    container_client.upload_blob(name=file.filename, data=content)

    return 'File uploaded to both AWS and Azure!'

if __name__ == "__main__":
    app.run(debug=True)
