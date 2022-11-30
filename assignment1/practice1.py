from google.cloud import storage
import wget
import io, os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='application_default_credentials.json'
os.environ["GCLOUD_PROJECT"]='balmy-hologram-370008'

project_id = 'balmy-hologram-370008'
bucket_name = 'df8-test'
destination_blob_name = 'wc_matches'
storage_client = storage.Client()

source_file = 'https://projects.fivethirtyeight.com/soccer-api/international/2022/wc_matches.csv'

def upload_blob(bucket_name, source, blob_name):   
    filename = wget.download(source)

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(filename)
    os.remove(filename)

upload_blob(bucket_name, source_file, destination_blob_name)

