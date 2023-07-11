import requests

url = 'http://localhost:8000/api/article/1/'

res = requests.get(url)

print(res.json())
