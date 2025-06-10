from rilz.client import Client
from rilz.services.avatars import Avatars
from rilz.enums import Browser

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

avatars = Avatars(client)

result = avatars.get_browser(
    code = Browser.AVANT_BROWSER,
    width = 0, # optional
    height = 0, # optional
    quality = -1 # optional
)
