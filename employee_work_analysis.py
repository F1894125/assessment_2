import re

########## CUSTOM EXCEPTIONS ##########
class InvalidInputError(Exception):
    """
    Custom exception for invalid input.
    """
    def __init__(self, message):
        super().__init__(message)

########## GLOBAL CONSTANTS ##########
HOURS_THRESHOLD: int = 50

########## CLASSES TO STORE DEPARTMENT AND EMPLOYEE DETAILS ##########
class Department:
    """
    Class to store department details.

    Attributes:
        name (str): Name of the department.
    
    Methods:
        __init__: Initializer that creates a new department by accepting name.
        __str__: Returns a human readable string for the Department object.
    """

    def __init__(self, name: str):
        """
        Initializer to create a Department object.
        
        Args:
            self (Department): The current Department object itself.
            name (str): Name of the department.
        """
        self.name: str = name
    
    def __str__(self):
        """
        Returns a human readable string for the current Department object.
        """
        return f"{self.name}"


class Employee:
    """
    Class to store employee details.

    Attributes:
        name (str): Name of the employee.
        department (Department): Department object associated with the employee.
        hours (int): Total number of hours worked.

    Methods:
        __init__: Initializer that creates a new employee by accepting name, department, and hours worked.
        __str__: Returns a human readable string for the Employee object.
        overtime_employees: Displays the name of the employees who worked more than a specified number of hours.
    """

    def __init__(self, name: str, dept: Department, hours: int):
        """
        Initializer to create an Employee object.
        
        Args:
            name (str): Name of the employee.
            dept (Department): Department object associated with the employee.
            hours (int): Total number of hours worked.
        """
        self.name: str = name
        self.dept: Department = dept
        self.hours: int = hours
    
    def __str__(self):
        """
        Returns a human readable string for the current Employee object.
        """
        return f"{self.name}"

########## MAPPINGS TO DEPARTMENTS AND EMPLOYEES ##########
departments: dict = {}
employees: dict = {}

########## FUNCTIONS TO IMPLEMENT OPERATIONS ##########
def validate_input(pattern: str, value: str, error_message: str):
    """
    Validates the input value against the provided regex pattern.
    If the value does not match the pattern, an InvalidInputError is raised.
    
    Args:
        pattern (str): The regex pattern to validate against.
        value (str): The input value to be validated.
        error_message (str): The error message to be used in the exception if validation fails.
    
    Returns:
        str: The validated input value if it matches the pattern.
    
    Raises:
        InvalidInputError: If the input value does not match the regex pattern.
    """
    if not re.fullmatch(pattern, value):
        raise InvalidInputError(error_message)
    return value

def add_department(**new_departments):
    """
    Function to create a new department object.
    """
    for d_id, name in new_departments.items():
        new_department: Department = Department(name=name)
        departments[d_id] = new_department


def add_employee():
    """
    Function to create a new employee object.
    """
    while True:
        e_id: str = input("Enter ID of the new employee: ")
        try:
            e_id = validate_input(r"\d{4}", e_id, "Field should be only have 4 NUMERIC characters.")
            print(f"\n'{e_id}' accepted as employee ID.")
            break
        except InvalidInputError as e:
            print(f"\nError: {e}")

    while True:
        name: str = input("Enter name of the new employee: ").strip().title()
        try:
            name = validate_input(r"[a-zA-Z]+", name, "Field should be only ALPHABETIC.")
            print(f"\n'{name}' accepted as employee name.")
            break
        except InvalidInputError as e:
            print(f"\nError: {e}")
    
    while True:
        d_id: str = input(f"Enter department ID for {name}: ")
        try:
            d_id = validate_input(r"\d{3}", d_id, "Field should be only have 3 NUMERIC characters.")
        except InvalidInputError as e:
            print(f"\nError: {e}")
        else:
            print(f"\n'{d_id}' accepted as department ID.")
            break
    
    while True:
        hours: str = input(f"Enter hours worked by {name}: ")
        if re.fullmatch(r"\d{2}", hours):
            print(f"\n'{hours}' accepted as hours worked.")
            break
        else:
            print(f"\n'{hours}' is invalid, field should only have 2 NUMERIC characters.")

    new_employee: Employee = Employee(name=name, dept=departments[d_id], hours=int(hours))
    employees[e_id] = new_employee

def more_than_hour_threshold():
    """
    Displays employees who worked more than the hour threshold.
    """
    print('\n', '-'*40, f'Employees who worked more than {HOURS_THRESHOLD} hours', '-'*40)
    for e_id, employee in employees.items():
        if employee.hours > HOURS_THRESHOLD:
            print(f"{e_id} - {employee.name} worked {employee.hours}.")


def display_all_departments():
    """
    Displays all departments.
    """
    print('\n', '-'*40, f'List of all Deparments', '-'*40)
    for d_id, department in departments.items():
        print(f"{d_id} - {department.name}.")


def menu():
    
    while True:
        print("\n--- Welcome to Employee Work Analysis System ---")
        print("1. Add a new department.")
        print("2. Add a new employee.")
        print("3. Display all departments.")
        print("4. Display employees who worked more hours than the threshold.")
        print("5. Terminate")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            new_departments: dict = {}
            d_id: str = ""
            name: str = ""

            while True:
                while True:
                    d_id = input("\nEnter ID of the new department: ")
                    if re.fullmatch(r"\d{3}", d_id):
                        print(f"'{d_id}' accepted as department ID.")
                        break
                    else:
                        print(f"'{d_id}' is invalid, field should be only have 3 NUMERIC characters.")

                while True:
                    name = input("\nEnter name of the new department: ").strip().title()
                    if re.fullmatch(r"[a-zA-Z]+", name):
                        print(f"'{name}' accepted as department name.")
                        break
                    else:
                        print(f"'{name}' is invalid, field should be only ALPHABETIC.")
                
                new_departments[d_id] = name
                
                opt: str = input("\nEnter 'n'/'N' to stop adding another department: ").strip().lower()
                if opt == 'n':
                    break
            
            add_department(**new_departments)

        elif choice == '2':
            add_employee()
        elif choice == '3':
            display_all_departments()
        elif choice == '4':
            more_than_hour_threshold()
        elif choice == '5':
            print("Terminating program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()