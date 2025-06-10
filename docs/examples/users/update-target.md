from rilz.client import Client
from rilz.services.users import Users

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result = users.update_target(
    user_id = '<USER_ID>',
    target_id = '<TARGET_ID>',
    identifier = '<IDENTIFIER>', # optional
    provider_id = '<PROVIDER_ID>', # optional
    name = '<NAME>' # optional
)
