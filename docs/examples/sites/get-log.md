from rilz.client import Client
from rilz.services.sites import Sites

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

sites = Sites(client)

result = sites.get_log(
    site_id = '<SITE_ID>',
    log_id = '<LOG_ID>'
)
