from rilz.client import Client
from rilz.services.sites import Sites
from rilz.input_file import InputFile

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

sites = Sites(client)

result = sites.create_deployment(
    site_id = '<SITE_ID>',
    code = InputFile.from_path('file.png'),
    activate = False,
    install_command = '<INSTALL_COMMAND>', # optional
    build_command = '<BUILD_COMMAND>', # optional
    output_directory = '<OUTPUT_DIRECTORY>' # optional
)
