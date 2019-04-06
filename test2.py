import requests
import json
my_domain = 'Sampreet.pythonanywhere.com'
username = 'Sampreet'
token = 'ca4f0a88a6e079a4a36d7dc50eef83b61379ce69'
id1 = '12195600'
id2 = '11969836'
input="print(3)"
#params = {'input': input,}
payload = {'input':input,}
response = requests.post('https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id2}/send_input/'.format(username=username, domain=my_domain,id2=id2),
                         headers={'Authorization': 'Token {token}'.format(token=token),'Content-Type': 'application/json'},data=json.dumps(payload))
if response.status_code == 200:
  print('All OK')
  print(response.text)
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        
