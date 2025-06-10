from rilz.client import Client
from rilz.services.databases import Databases

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result = databases.list_collections(
    database_id = '<DATABASE_ID>',
    queries = [], # optional
    search = '<SEARCH>' # optional
)
