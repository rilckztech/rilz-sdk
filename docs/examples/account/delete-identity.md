from rilz.client import Client
from rilz.services.account import Account

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = Account(client)

result = account.delete_identity(
    identity_id = '<IDENTITY_ID>'
)
