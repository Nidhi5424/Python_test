class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, person_id, name, age):
        super().__init__(person_id, name, age)
        self.emp_id = None
        self.salary = None

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def __str__(self):
        return f"{self.name} ({self.emp_id})"

    def __eq__(self, other):
        return self.get_salary() == other.get_salary()

    def __lt__(self, other):
        return self.get_salary() < other.get_salary()

    def __gt__(self, other):
        return self.get_salary() > other.get_salary()


class Manager(Employee):
    def __init__(self, person_id, name, age, emp_id, salary, department):
        super().__init__(person_id, name, age)
        self.set_emp_id(emp_id)
        self.set_salary(salary)
        self.department = department


class Developer(Employee):
    def __init__(self, person_id, name, age, emp_id, salary, language):
        super().__init__(person_id, name, age)
        self.set_emp_id(emp_id)
        self.set_salary(salary)
        self.language = language


persons = {}
employees = {}


def create_person():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    person_id = "P" + str(len(persons) + 1)
    p = Person(person_id, name, age)
    persons[person_id] = p
    print(f"\nPerson created with ID: {person_id}, Name: {name}, Age: {age}.")


def create_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    person_id = "P" + str(len(persons) + 1)
    e = Employee(person_id, name, age)
    e.set_emp_id(emp_id)
    e.set_salary(salary)
    persons[person_id] = e
    employees[emp_id] = e
    print(f"\nEmployee created: ID: {emp_id}, Name: {name}, Age: {age}, Salary: ${salary}")


def create_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    person_id = "P" + str(len(persons) + 1)
    m = Manager(person_id, name, age, emp_id, salary, department)
    persons[person_id] = m
    employees[emp_id] = m
    print(f"\nManager created: ID: {emp_id}, Name: {name}, Age: {age}, Dept: {department}, Salary: ${salary}")


def create_developer():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    language = input("Enter Programming Language: ")
    person_id = "P" + str(len(persons) + 1)
    d = Developer(person_id, name, age, emp_id, salary, language)
    persons[person_id] = d
    employees[emp_id] = d
    print(f"\nDeveloper created: ID: {emp_id}, Name: {name}, Age: {age}, Language: {language}, Salary: ${salary}")


def show_details():
    print("\nShow Details:\n1. Person\n2. Employee\n3. Manager/Developer")
    choice = input("Enter your choice: ")

    if choice == '1':
        for p in persons.values():
            if isinstance(p, Person) and not isinstance(p, Employee):
                print(f"\nPerson ID: {p.person_id}, Name: {p.name}, Age: {p.age}")

    elif choice == '2':
        for e in employees.values():
            if type(e) == Employee:
                print(f"\nEmployee ID: {e.emp_id}, Name: {e.name}, Age: {e.age}, Salary: {e.salary}")

    elif choice == '3':
        for e in employees.values():
            if isinstance(e, Manager):
                print(f"\nManager ID: {e.emp_id}, Name: {e.name}, Age: {e.age}, Salary: {e.salary}, Dept: {e.department}")
            elif isinstance(e, Developer):
                print(f"\nDev ID: {e.emp_id}, Name: {e.name}, Age: {e.age}, Salary: {e.salary}, Lang: {e.language}")
    else:
        print("Invalid choice.")


def compare_salaries():
    id1 = input("\nEnter first employee ID: ")
    id2 = input("Enter second employee ID: ")
    e1 = employees.get(id1)
    e2 = employees.get(id2)
    if e1 and e2:
        if e1 > e2:
            print(f"\n{e1} has a higher salary than {e2}")
        elif e1 < e2:
            print(f"\n{e1} has a lower salary than {e2}")
        else:
            print(f"\n{e1} and {e2} have the same salary")
    else:
        print("\nOne or both employee IDs not found.")


while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create Developer")
    print("5. Show Details")
    print("6. Compare Salaries")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        create_person()
    elif choice == '2':
        create_employee()
    elif choice == '3':
        create_manager()
    elif choice == '4':
        create_developer()
    elif choice == '5':
        show_details()
    elif choice == '6':
        compare_salaries()
    elif choice == '7':
        print("\nExiting the system. All resources have been freed. \n\nGoodbye... :)")
        break
    else:
        print("\nInvalid choice. Try again.")
