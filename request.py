import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'X':20})

print(r.json())