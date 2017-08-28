AWS SAM (serverless application model) with:

An API Gateway endpoint that:

* receives an image in base 64 encoding and calls a Lambda fucntion to
upload the image to an S3 bucket
* returns the resulting public url for that image
