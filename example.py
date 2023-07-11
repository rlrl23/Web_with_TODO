import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
                                                                        'Developer_1', 'password': 'developer1'})
print(response.status_code)
