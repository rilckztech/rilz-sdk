from rilz.client import Client
from rilz.services.sites import Sites
from rilz.enums import VCSDeploymentType

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

sites = Sites(client)

result = sites.create_vcs_deployment(
    site_id = '<SITE_ID>',
    type = VCSDeploymentType.BRANCH,
    reference = '<REFERENCE>',
    activate = False # optional
)
