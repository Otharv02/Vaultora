# Password is hard coded right now 
# LAter connect to db and metadata


def authenticate(username, password):
    valid_users = {
        "admin" : "1234"
    }

    return valid_users.get(username) == password