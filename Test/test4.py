
last_factorial_result = 0

def display_menu():
    print("\n=======================================================")
    print("1. Input Data")
    print("2. Display summary using (Built-in Functions)")
    print("3. Calculate Factorial  (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset statistics (Return Multiple Values)")
    print("7. Exit Program")
    print("======================================================")


def input_data():
    """Accepts 1D list of numbers from the user."""
    
    print("\n --->>>>>> Data Input <<<<<<--- ")
    parts = input("Enter numbers separated by spaces: ").split()
    if not parts:
        print("\n   No input given.")
        return []
    
    for p in parts:
        for digit in p:
            if digit < '0' or digit > '9':
                print("Invalid input. \n      Please enter only intiger numbers.")
                return []
    
    data = [int(x) for x in parts]
    print("\n------:Data successfully recorded!:------")
    return data



def data_summary(*args, **kwargs):
    """
    Displays summary of the given data using built-in functions.
    Accepts any number of numerical arguments using *args.
    Optionally accepts keyword arguments using **kwargs.
    """
    print("\n --->>>>>> Data Summary <<<<<<--- ")
    if not args:
        print("No data provided.... :( )")
        return
    print(f"(i) Total Elements: {args}")
    print(f"(ii) Minimum Value: {min(args)}")
    print(f"(iii)Maximum Value: {max(args)}")
    print(f"(iv)Sum of all Values: {sum(args)}")
    print(f"(v)Average Value: {sum(args)/len(args)}")
    if kwargs:
        print("\nAdditional Keyword Arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


def factorial(n):
    """Recursive function to calculate factorial."""
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def handle_factorial():
    """Handles factorial calculation and updates global variable."""
    
    global last_factorial_result
    
    print("\n --->>>>>> Factorial Calculator <<<<<<---")
    
    while True:
        num = input("Enter a non-negative integer: ")
        if all('0' <= c <= '9' for c in num):
            num = int(num)
            break
        print("\n Invalid input. Please enter an integer...")
    
    result = factorial(num)
    last_factorial_result = result
    print(f"Factorial of {num} is: {result}")


def check_last_factorial():
    """Prints the last calculated factorial from the global variable."""
    
    print("\n--->>>>>> Last Factorial Result <<<<<<---")
    if last_factorial_result is not None:
        print(f"The last factorial calculated was: {last_factorial_result}")
    else:
        print("\n No factorial has been calculated yet.")

data = []
matrix_data = []


while True:
    display_menu()
    choice = input("\n  :)  Please enter your choice: ")

    if any(c < '0' or c > '9' for c in choice) or not (1 <= int(choice) <= 7):
         print("Invalid input.\n     Please enter a number between 1 and 7.")
    else:
         choice = int(choice)
   
    if choice == 1:
        data = input_data()

    elif choice == 2:
        if data:
            data_summary(*data, source="user input", note="1D list summary")
            print("\nDocstring of data_summary function:\n")
            print(data_summary.__doc__)
        else:
            print("No data available.\n  Please input data first.")

    elif choice == 3:
        handle_factorial()
        check_last_factorial()

    elif choice == 4:
        if data:
            filter_and_transform(data)
        else:
            print("No data available. \n Please input data first.")

    elif choice == 5:
        matrix_data = input_2d_data()
        display_row_column_sums(matrix_data)

    elif choice == 6:
        if data:
            asc, desc = sort_data(data)
            print("\n--->>>>>> Sorted Data <<<<<<---")
            print(f"    Ascending Order: {asc}")
            print(f"    Descending Order: {desc}")

            minimum, maximum, average = get_statistics(data)
            print("\n--->>>>>> Dataset Statistics <<<<<<---")
            print(f"    Minimum: {minimum}")
            print(f"    Maximum: {maximum}")
            print(f"    Average: {average:.2f}")
        else:
            print("No data available. Please input data first.")

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program.\n      Goodbye!!!... ;)")
        break

    else:
        print("Invalid choice. Please try again...")


