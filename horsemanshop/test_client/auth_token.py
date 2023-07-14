import requests

auth_url = 'http://localhost:8000/auth-token/'
url = 'http://localhost:8000/api/articles/'
user = {'username': 'staff', 'password': '1123'}

auth_res = requests.post(auth_url, json=user)

print(auth_res.json())

if auth_res.status_code == 200:
    token = auth_res.json()['token']
    header = {
        'Authorization': f"Token {token}"
    }
    res = requests.get(url, headers=header)

    print(res.json())
