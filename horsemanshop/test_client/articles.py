import requests

url = 'http://localhost:8000/api/articles/'

res = requests.get(url)

print(res.json())
