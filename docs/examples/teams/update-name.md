from rilz.client import Client
from rilz.services.teams import Teams

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

teams = Teams(client)

result = teams.update_name(
    team_id = '<TEAM_ID>',
    name = '<NAME>'
)
