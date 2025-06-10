def check_palindrome(s):
   
    assert s != "", "Input string should not be empty."

    if s == s[::-1]:
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")


user_input = input("Enter a string to check if it's a palindrome: ")


check_palindrome(user_input)
