import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/tods/1")
    print(response.status_code)
    print(response.json())
    data = response.json()
    print(data['title'])
except Exception as e:
    print(f"error aaya: {e}")