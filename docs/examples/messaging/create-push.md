from rilz.client import Client
from rilz.services.messaging import Messaging

client = Client()
client.set_endpoint('https://<REGION>.rilck.com/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result = messaging.create_push(
    message_id = '<MESSAGE_ID>',
    title = '<TITLE>', # optional
    body = '<BODY>', # optional
    topics = [], # optional
    users = [], # optional
    targets = [], # optional
    data = {}, # optional
    action = '<ACTION>', # optional
    image = '[ID1:ID2]', # optional
    icon = '<ICON>', # optional
    sound = '<SOUND>', # optional
    color = '<COLOR>', # optional
    tag = '<TAG>', # optional
    badge = None, # optional
    draft = False, # optional
    scheduled_at = '', # optional
    content_available = False, # optional
    critical = False, # optional
    priority = MessagePriority.NORMAL # optional
)
