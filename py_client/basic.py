import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/' # http://127.0.0.1:8000/

get_response = requests.get(endpoint, json={"query":"Hello World"}) # HTTP Request
print(get_response.text) # Print raw text response
print(get_response.status_code)

# HTTP Request -> HTTP
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json()['message'])
# print(get_response.status_code)