# import
import requests

# Toggl Option
_api_token = 'Your API Key'

headers = {
    'Content-Type': 'application/json',
}

data = '{"time_entry":{"description":"","tags":["Other"],"pid":88508848,"created_with":"curl"}}'

# Toggl API Request
r = requests.post('https://www.toggl.com/api/v8/time_entries/start', headers=headers, data=data, auth=(_api_token, 'api_token'), verify=False)
