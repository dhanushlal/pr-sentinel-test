def divide_numbers(a, b):
    # Potential ZeroDivisionError bug for testing
    return a / b

def get_user_role(role_id):
    query = f"SELECT * FROM users WHERE role = '{role_id}'"
    return query
    
def get_api_key():
    # Hardcoded secret test
    api_key = "AIzaSyD-fake-key-12345"
    return api_key
    
def greet_user(username):
    message = "Hello, " + username
    return message
