from google.cloud import storage
from datetime import timedelta

def get_signed_url(input_uri):
    # Instantiate a client
    storage_client = storage.Client.from_service_account_json('/Users/neeraj_py/Desktop/class/Sem3/ISC211/upload_to_bucket/civic-axon-123.json')

    # Set the bucket name and file name
    bucket_name = input_uri.split('/')[1]
    file_name = input_uri.split('/')[2]

    # Get the bucket and blob
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
 
    # Set the expiration time for the URL (e.g. one hour)
    expiration = timedelta(hours=1)

    # Create a signed URL
    signed_url = blob.generate_signed_url(expiration=expiration, method='GET')

    # Print the signed URL
    return signed_url

#get_signed_url("/video-upload-bucket/funny_cat.mp4")

def get_thumbnail(input_uri):
    # Instantiate a client
    storage_client = storage.Client.from_service_account_json('/Users/neeraj_py/Desktop/class/Sem3/ISC211/upload_to_bucket/civic-axon-123.json')

    # Set the bucket name and file name
    bucket_name = "video-thumbnail-bucket"
    file_name = input_uri.split('/')[2]
    file_name = file_name.split('.')[0]+".jpg"

    # Get the bucket and blob
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
 
    # Set the expiration time for the URL (e.g. one hour)
    expiration = timedelta(hours=1)

    # Create a signed URL
    signed_url = blob.generate_signed_url(expiration=expiration, method='GET')

    # Print the signed URL
    return signed_url

    # Download the file
    #blob.download_to_filename(file_name)

#get_thumbnail("/video-upload-bucket/funny_cat.mp4")



