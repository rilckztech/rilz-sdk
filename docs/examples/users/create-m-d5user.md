from rilz.client import Client
from rilz.services.users import Users

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result = users.create_md5_user(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    password = 'password',
    name = '<NAME>' # optional
)
