from rilz.client import Client
from rilz.services.users import Users

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result = users.create_scrypt_modified_user(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    password = 'password',
    password_salt = '<PASSWORD_SALT>',
    password_salt_separator = '<PASSWORD_SALT_SEPARATOR>',
    password_signer_key = '<PASSWORD_SIGNER_KEY>',
    name = '<NAME>' # optional
)
