# with open("banks.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)

# with open("banks.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# import json

# with open("user.json", "r", encoding="utf-8") as file:
#     user = json.load(file)
#     print(user["name"])

# import json

# with open("profile.json", "r", encoding="utf-8") as file:
#     profile = json.load(file)
#     print(profile["name"])
#     print(profile["city"])
#     print(profile["contacts"]["phone"])
#     print(profile["contacts"]["email"])

# import json

# with open("response.json", "r", encoding="utf-8") as file:
#     response = json.load(file)
#     if response["success"]:
#         print(response["user"]["name"])
#     else:
#         print("Ошибка получения пользователя")