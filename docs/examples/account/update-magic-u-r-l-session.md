from rilz.client import Client
from rilz.services.account import Account

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = Account(client)

result = account.update_magic_url_session(
    user_id = '<USER_ID>',
    secret = '<SECRET>'
)
