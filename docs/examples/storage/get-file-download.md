from rilz.client import Client
from rilz.services.storage import Storage

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

storage = Storage(client)

result = storage.get_file_download(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    token = '<TOKEN>' # optional
)
