
from google.cloud import storage


def upload_blob_from_stream(bucket_name, file_name, destination_blob_name):
    """Uploads bytes from a stream or other file-like object to a blob."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The stream or file (file-like object) from which to read
    # import io
    # file_obj = io.BytesIO()
    # file_obj.write(b"This is test data.")

    # The desired name of the uploaded GCS object (blob)
    # destination_blob_name = "storage-object-name"

    # Construct a client-side representation of the blob.

    #use api key for authentication
    storage_client = storage.Client.from_service_account_json('/Users/neeraj_py/Desktop/class/Sem3/ISC211/upload_to_bucket/civic-axon-123.json')

    #storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Rewind the stream to the beginning. This step can be omitted if the input
    # stream will always be at a correct position.


    # Upload data from the stream to your bucket.
    blob.upload_from_filename(file_name)

    print(
        f"Stream data uploaded to {destination_blob_name} in bucket {bucket_name}."
    )

# [END storage_stream_file_upload]

upload_blob_from_stream("video-upload-bucket", "/Users/neeraj_py/Desktop/class/Sem3/ISC211/upload_to_bucket/funny_cat.mp4", "funny_cat.mp4")