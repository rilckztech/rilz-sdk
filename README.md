# Rilz Python SDK

![Version](https://img.shields.io/badge/api%20version-1.7.0-blue.svg?style=flat-square)

**This SDK is compatible with Rilz server version 1.7.x. For older versions, please check [previous releases](https://github.com/rilckztech/rilz-sdk/releases).**

Rilz is an open-source backend as a service server that abstract and simplify complex and repetitive development tasks behind a very simple to use REST API. Rilz aims to help you develop your apps faster and in a more secure way. Use the Python SDK to integrate your app with the Rilz server to easily start interacting with all of Rilz backend APIs and tools. For full API documentation and tutorials go to [https://rilck.com/docs](https://rilck.com/docs)

![Rilz](https://github.com/rilckztech/rilz-sdk/raw/main/public/images/github.png)

## Installation

To install via [PyPI](https://pypi.org/):

```bash
pip install rilz
```


## Getting Started

### Init your SDK
Initialize your SDK with your Rilz server API endpoint and project ID which can be found on your project settings page and your new API secret Key from project's API keys section.

```python
from rilz.client import Client
from rilz.services.users import Users

client = Client()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)
```

### Make Your First Request
Once your SDK object is set, create any of the Rilz service objects and choose any request to send. Full documentation for any service method you would like to use can be found in your SDK documentation or in the [API References](https://rilck.com/docs) section.

```python
users = Users(client)

result = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")
```

### Full Example
```python
from rilz.client import Client
from rilz.services.users import Users
from rilz.id import ID

client = Client()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

users = Users(client)

result = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")
```

### Error Handling
The Rilz Python SDK raises `RilzException` object with `message`, `code` and `response` properties. You can handle any errors by catching `RilzException` and present the `message` to the user or handle it yourself based on the provided error information. Below is an example.

```python
users = Users(client)
try:
  result = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")
except RilzException as e:
  print(e.message)
```

### Learn more
You can use the following resources to learn more and get help
- 📜 [Rilz Docs](https://rilck.com/docs)
- 🚂 [Rilz Python Playground](https://github.com/rilckztech/playground-for-python)


## License

Please see the [BSD-3-Clause license](https://raw.githubusercontent.com/rilckztech/rilz-sdk/master/LICENSE) file for more information.
