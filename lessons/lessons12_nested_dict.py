# book = {
#     "name": "Эрагон",
#     "author": "Кристофер Паолини",                                                                                                                                                                                                                                          
#     "year": "2003"
# }

# print(book["name"], book["author"])

# user = {
#     "address": {
#         "city": "Москва",
#         "street": "Ленина",
#         "house": 15
#     }
# }

# print(user["address"]["city"],user["address"]["street"])

# response = {
#     "products": [
#         {
#             "name": "Свинина",
#             "price": 300
#         },
#         {
#             "name": "Чёрный хлеб",
#             "price": 100
#         },
#         {
#             "name": "Молоко",
#             "price": 150
#         },
#         {
#             "name": "Яйца",
#             "price": 180
#         }
#     ]
# }

# # print(products["products"][0]["name"])

# for product in response["products"]:
#     print(product["name"])

# response = {
#     "success": True,
#     "user": {
#         "id": 1001,
#         "name": "Влад",
#         "premium": False
#     }
# }
# if "success" in response:
#     if response["success"] == True:
#         print(response["user"]["name"])
#     else:
#         print("Ошибка получения пользователя")

# response = {
#     "offers": [
#         {
#             "bank": "Т-Банк",
#             "rate": 17.9
#         },
#         {
#             "bank": "Сбер",
#             "rate": 18.5
#         },
#         {
#             "bank": "Альфа-Банк",
#             "rate": 16.8
#         }
#     ]
# }

# # print(response["offers"][0])

# for offer in response["offers"]:
#     print(offer["bank"], "-", offer["rate"],"%")