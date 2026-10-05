import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)

data = response.json()

print(data["name"])
print(data["email"])

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

print(data[0]["name"])

for user in data:
    print(user["name"])
    if user["id"] == 5:
        print(user["name"])
        print(user["email"])

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data["name"])
    print(data["email"])
else:
    print("Ошибка запроса")
