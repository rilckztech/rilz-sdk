from rilz.client import Client
from rilz.services.health import Health
from rilz.enums import 

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

health = Health(client)

result = health.get_failed_jobs(
    name = .V1_DATABASE,
    threshold = None # optional
)
