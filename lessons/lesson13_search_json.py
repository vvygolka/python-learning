# users = [
#     {"id": 1001, "name": "Влад"},
#     {"id": 1002, "name": "Полина"},
#     {"id": 1003, "name": "Иван"}
# ]

# for user in users:
#     if user["id"] == 1002:
#         print(user["name"])

# offers = [
#     {"bank": "Т-Банк", "rate": 17.9},
#     {"bank": "Сбер", "rate": 18.5},
#     {"bank": "Альфа-Банк", "rate": 16.8}
# ]

# for offer in offers:
#     if offer["bank"] == "Альфа-Банк":
#         print(offer["rate"])

# credits = [
#     {"bank": "Т-Банк", "status": "ACTIVE"},
#     {"bank": "Сбер", "status": "CLOSED"},
#     {"bank": "Альфа-Банк", "status": "ACTIVE"}
# ]

# for credit in credits:
#     if credit["status"] == "ACTIVE":
#         print(credit["bank"])

# products = [
#     {"name": "Свинина", "price": 300},
#     {"name": "Хлеб", "price": 100},
#     {"name": "Молоко", "price": 150},
#     {"name": "Яйца", "price": 180}
# ]
# total = 0
# name = ""
# for product in products:
#     if product["price"] >= total:
#         total = product["price"]
#         name = product["name"]
# print(name, total)

# response = {
#     "success": True,
#     "user": {
#         "name": "Влад"
#     },
#     "cards": [
#         {
#             "bank": "Т-Банк", 
#             "active": True
#         },
#         {
#             "bank": "Сбер", 
#             "active": False
#         },
#         {
#             "bank": "Альфа-Банк", 
#             "active": True
#         }
#     ]
# }

# if response["success"]:
#     print(response["user"]["name"])
#     for card in response["cards"]:
#         if card["active"]:
#             print(card["bank"])
# else:
#     print("Ошибка получения пользователя")
