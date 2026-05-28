import requests

response = requests.get("http://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())
data = response.json()
if data['userId'] == 5:

 print(data["title"])

# Post request
new_todo = {
    "title": "Python seekhna hai",
    "completed": False,
    "userId" : 1
}

post_response = requests.post(
    "https://jsonplaceholder.typicode.com/todos",
    json=new_todo

)
print(post_response.status_code)
print(post_response.json())