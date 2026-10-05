import requests


response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
data = response.json()

print(data["name"])
###
user = {
    "name": "Vlad",
    "email": "v.vygolka@yandex.ru"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users", 
    json = user)

data = response.json()

print(response.status_code)
print(data)

###

user = {
    "name": "Polina",
    "email": "p.vygolka@yandex.ru"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json = user
)

print(response.status_code)

data = response.json()
print(data)

###

data = {
    "email": "p.kulahgenkova@yandex.ru"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/users/1",
    json = data
)

print(response.status_code)

data = response.json()
print(data)

###

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)