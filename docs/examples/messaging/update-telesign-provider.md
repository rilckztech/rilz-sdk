from rilz.client import Client
from rilz.services.messaging import Messaging

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result = messaging.update_telesign_provider(
    provider_id = '<PROVIDER_ID>',
    name = '<NAME>', # optional
    enabled = False, # optional
    customer_id = '<CUSTOMER_ID>', # optional
    api_key = '<API_KEY>', # optional
    from = '<FROM>' # optional
)
