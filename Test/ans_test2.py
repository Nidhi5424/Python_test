
print("Welcome to the pattern Generator and Number analyzer!\n")

choice = 0

while choice != 3:

    print("Select an option: ")
    print("    1. Generate a Pattern")
    print("    2. Analyze a Range of Numbers")
    print("    3. Exit")

    choice = int(input("Enter your choice : "))

    match choice :
        case 1 : 
            n1 = int(input("Enter the number of rows for the pattern: "))
            print("Pattern: ")
            for i in range(1,n1+1):
                for j in range(1,i+1):
                    print("*",end = ' ')
                print()


        case 2 : 
            start = int(input("Enter the start of the range:"))
            end = int(input("Enter the end of the range:"))
            
            sum = 0
            
            for x in range(start,end +1):
                if (x %2 == 0):
                    print("Number",x, "is EVEN")
                else :
                    print("Number",x, "is ODD")

            sum = x + sum

            print("\nSum of all numbers from ",start,"to",end, "is: ",sum)
        

        case 3 : 
            print("\nExiting the program. \n" "   Goodbye!!!...")

        case _:
            print("Your choice is invelid...")

print("Exit")