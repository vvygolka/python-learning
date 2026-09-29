def user_name(response):
    if response["success"]:
        return response["user"]["name"]
    else:
        return None