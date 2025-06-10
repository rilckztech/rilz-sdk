from rilz.client import Client
from rilz.services.storage import Storage

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

storage = Storage(client)

result = storage.get_bucket(
    bucket_id = '<BUCKET_ID>'
)
