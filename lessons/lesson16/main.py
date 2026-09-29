import calculator
import user_utils
import response_utils

calculator.add(2, 3)
calculator.multiply(2, 3)

user = {
    "name": "Влад",
    "age": 28
}

print(user_utils.get_user_name(user))

user = {
    "name": "Влад",
    "active": True
}

print(user_utils.is_active(user))

response = {
    "success": True,
    "user": {
        "name": "Влад"
    }
}

print(response_utils.user_name(response))