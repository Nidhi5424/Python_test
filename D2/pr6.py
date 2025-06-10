#Day2 Q6

input1 = input("Enter first boolean value (True/False): ")
input2 = input("Enter second boolean value (True/False): ")


bool1 = input1 == "True"
bool2 = input2 == "True"


print("\nLogical Operations:")
print(bool1, "and", bool2, "=", bool1 and bool2)
print(bool1, "or", bool2, "=", bool1 or bool2)
print("not", bool1, "=", not bool1)
print("not", bool2, "=", not bool2)
