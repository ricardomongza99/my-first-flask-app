def valid_username(username):
    return username[0].isupper()

def valid_password(password):
    return any(char.isalpha() for char in password) and any(char.isdigit() for char in password)