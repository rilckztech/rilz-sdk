from rilz.client import Client
from rilz.services.account import Account

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = Account(client)

result = account.create_magic_url_token(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    url = 'https://example.com', # optional
    phrase = False # optional
)
