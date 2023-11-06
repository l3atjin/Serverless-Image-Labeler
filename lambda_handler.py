import boto3
from urllib.parse import unquote_plus
import os
import json

def upload_file(label, key, bucket):
    """Upload a file to an S3 bucket

    :param key: Name of image file
    :param bucket: Bucket to upload to
    :param label: Content of the new file, a json
    :return: True if file was uploaded, else False
    """
    file_name = key.split(".")[0] + ".json"
    
    print("filename is", file_name)
    print("bucket is", bucket)

    object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.put_object(Bucket=bucket, Key=file_name, Body=json.dumps(label))
    
    return True


def label_function(bucket, name):
    """This takes an S3 bucket and a image name!"""
    print(f"This is the bucketname {bucket} !")
    print(f"This is the imagename {name} !")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": name,
            }
        },
    )
    labels = response["Labels"]
    print(f"I found these labels {labels}")
    return labels


def lambda_handler(event, context):
    """This is a computer vision lambda handler"""

    print(f"This is my S3 event {event}")
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        print(f"This is my bucket {bucket}")
        key = unquote_plus(record["s3"]["object"]["key"])
        print(f"This is my key {key}")

    my_labels = label_function(bucket=bucket, name=key)
    
    print("This is a picture of", my_labels[0]["Name"])
    upload_file(my_labels, key, bucket)
    
    return my_labels
