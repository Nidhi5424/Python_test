
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email or not (email.endswith('.com') or email.endswith('.org')):
        raise InvalidEmailError("Invalid email! Must contain '@' and end with .com or .org.")
    else:
        print("Valid email address:", email)

user_email = input("Enter your email: ")

try:
    validate_email(user_email)
except InvalidEmailError as e:
    print(e)
