import requests

url = 'http://localhost:8000/api/categories/'

res = requests.get(url)

print(res.json())
