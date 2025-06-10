from rilz.client import Client
from rilz.services.tokens import Tokens

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tokens = Tokens(client)

result = tokens.create_file_token(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    expire = '' # optional
)
