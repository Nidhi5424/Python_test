
text = input("Enter a string: ")


if text == text[::-1]:
    print("It's a palindrome!")
else:
    print(text[::-1],"\nIt's not a palindrome.")

