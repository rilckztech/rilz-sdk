from rilz.client import Client
from rilz.services.functions import Functions
from rilz.enums import VCSDeploymentType

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

functions = Functions(client)

result = functions.create_vcs_deployment(
    function_id = '<FUNCTION_ID>',
    type = VCSDeploymentType.BRANCH,
    reference = '<REFERENCE>',
    activate = False # optional
)
