from rilz.client import Client
from rilz.services.locale import Locale

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

locale = Locale(client)

result = locale.list_codes()
