from rilz.client import Client
from rilz.services.functions import Functions
from rilz.enums import 

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

functions = Functions(client)

result = functions.create(
    function_id = '<FUNCTION_ID>',
    name = '<NAME>',
    runtime = .NODE_14_5,
    execute = ["any"], # optional
    events = [], # optional
    schedule = '', # optional
    timeout = 1, # optional
    enabled = False, # optional
    logging = False, # optional
    entrypoint = '<ENTRYPOINT>', # optional
    commands = '<COMMANDS>', # optional
    scopes = [], # optional
    installation_id = '<INSTALLATION_ID>', # optional
    provider_repository_id = '<PROVIDER_REPOSITORY_ID>', # optional
    provider_branch = '<PROVIDER_BRANCH>', # optional
    provider_silent_mode = False, # optional
    provider_root_directory = '<PROVIDER_ROOT_DIRECTORY>', # optional
    specification = '' # optional
)
