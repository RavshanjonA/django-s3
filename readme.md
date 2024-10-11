# Django S3 Bucket integration

#### This is a simple example of how to store static and media files to S3 bucket.

## Setup

1. ```pip install boto3 django-storages```
2. In settings file we have to set
```
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
            "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "region_name": os.getenv("S3_REGION"),  # e.g., "us-east-1"
            "bucket_name": os.getenv("BUCKET_NAME"),
        },
    },
    "staticfiles": {  # For static files
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
            "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "region_name": os.getenv("S3_REGION"), # e.g., "us-east-1"
            "bucket_name": os.getenv("BUCKET_NAME"),
            "location": "static",  # Specify a folder within your bucket
        },
    },
}

DEFAULT_FILE_STORAGE = "config.settings.storages.default"  # Replace "config.settings" with your actual settings path
STATICFILES_STORAGE = "config.settings.storages.staticfiles"
```
3. create .env file and add AWS params (we need create IAM user and S3 bucket first)
```
AWS_ACCESS_KEY_ID=your IAM user access key
AWS_SECRET_ACCESS_KEY=your IAM user secret key
S3_REGION=S3_REGION
BUCKET_NAME=BUCKET_NAME
```
4. run collectstatic command
```python

python manage.py collectstatic
```
