
print("\nWelcome to the Pattern Generator and Number Analyzer! \n")

choice = 0

while choice != 3:
#while True:

    print("Select an option: ")
    print("    1. Generate a Pattern")
    print("    2. Analyze a Range of Numbers")
    print("    3. Exit")

    choice = int(input("\nEnter your choice:"))

    if choice == 1:
        row = int(input("\nEnter the number of row for the pattern:"))
        print("The Pattern will looks like...")
        for i in range(1,row+1):
            for _ in range(1,i+1):
                print("*", end=" ") 
            print()
                        
    elif choice == 2:
        start = int(input("Enter the start of the range:"))
        end = int(input("Enter the end of the range:"))
            
        sum = 0
            
        for x in range(start,end +1):
            
            sum = x + sum
            #sum += x

            if (x %2 == 0):
                print("Number",x, "is EVEN")
            else :
                print("Number",x, "is ODD")

        
        print("\nSum of all numbers from ",start,"to",end, "is: ",sum)

    else:
        print("\nExiting the program.")
        print("   Goodbye!!!...")
    
    #break

print("\nProgram ended.")