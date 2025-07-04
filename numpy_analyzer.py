import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("Select the type of array to create:")
        print("1. 1D Array\n2. 2D Array\n3. 3D Array")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements)
        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements).reshape(rows, cols)
        elif choice == 3:
            dim1 = int(input("Enter dimension 1: "))
            dim2 = int(input("Enter dimension 2: "))
            dim3 = int(input("Enter dimension 3: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements).reshape(dim1, dim2, dim3)
        print("Array created successfully:")
        print(self.array)

    def array_slicing(self):
        print("Choose an operation:\n1. Indexing\n2. Slicing\n3. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            r, c = map(int, input("Enter row and column index: ").split())
            print("Indexed value:", self.array[r][c])
        elif choice == 2:
            r_start, r_end = map(int, input("Enter row range (start:end): ").split(":"))
            c_start, c_end = map(int, input("Enter column range (start:end): ").split(":"))
            print("Sliced Array:")
            print(self.array[r_start:r_end, c_start:c_end])

    def mathematical_operations(self):
        print("Choose a mathematical operation:")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        choice = int(input("Enter your choice: "))
        elements = list(map(int, input("Enter same-size array elements separated by space: ").split()))
        second_array = np.array(elements).reshape(self.array.shape)
        if choice == 1:
            print("Result of Addition:")
            print(self.array + second_array)
        elif choice == 2:
            print("Result of Subtraction:")
            print(self.array - second_array)
        elif choice == 3:
            print("Result of Multiplication:")
            print(self.array * second_array)
        elif choice == 4:
            print("Result of Division:")
            print(self.array / second_array)

    def combine_arrays(self):
        elements = list(map(int, input("Enter elements of another array to combine: ").split()))
        second_array = np.array(elements).reshape(self.array.shape)
        combined = np.vstack((self.array, second_array))
        print("Combined Array (Vertical Stack):")
        print(combined)

    def sort_array(self):
        print("Sorting applied row-wise.")
        sorted_array = np.sort(self.array, axis=1)
        print("Sorted Array:")
        print(sorted_array)

    def statistics(self):
        print("Choose an operation: 1.Sum 2.Mean 3.Median 4.Standard Deviation 5.Variance")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Sum of Array:", np.sum(self.array))
        elif choice == 2:
            print("Mean of Array:", np.mean(self.array))
        elif choice == 3:
            print("Median of Array:", np.median(self.array))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))
        elif choice == 5:
            print("Variance:", np.var(self.array))


def main():
    analyzer = DataAnalytics()
    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.mathematical_operations()
        elif choice == 3:
            analyzer.combine_arrays()
        elif choice == 4:
            analyzer.sort_array()
        elif choice == 5:
            analyzer.statistics()
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
