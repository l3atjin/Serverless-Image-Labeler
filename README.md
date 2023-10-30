# Serverless-Image-Labeler
This is a demo project showcasing how AWS services can work together on the cloud.

Services I used:
- AWS Cloud9
- AWS S3
- AWS Lambda
- AWS CloudWatch
- AWS Rekognition

First, I created a lambda function that uses AWS Rekognition to label an image. Then, I setup an S3 bucket with public access that stores images. The lambda function is hooked to this bucket so that on every image upload it runs rekognition on this image to acquire a label, which is outputted. 

Here is a useful visualization created by Professor Noah Gift on this workflow:

![Alt text](https://user-images.githubusercontent.com/58792/112540085-26259d00-8d88-11eb-9756-36b608a78fcc.png)

# Note

This demo takes advantage of the full-scale services provided by AWS, which seems to be "the" way to develop applications right now. I wrote the lambda function on AWS C9 so everything I've done was through my browser. Deployment was as easy as clicking a button, literally. 

This demo also showcased how IAM permission should be set up. 
