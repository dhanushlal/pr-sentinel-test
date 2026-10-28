def divide_numbers(a, b):
    # Potential ZeroDivisionError bug for testing
    return a / b

def get_user_role(role_id):
    query = f"SELECT * FROM users WHERE role = '{role_id}'"
    return query
