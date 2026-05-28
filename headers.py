
import requests
headers = {
    "x-api-key": "expense-tracker-secret-2024"
}

secure_response = requests.get( "https://jsonplaceholder.typicode.com/todos/1", headers=headers)

print(secure_response.status_code)