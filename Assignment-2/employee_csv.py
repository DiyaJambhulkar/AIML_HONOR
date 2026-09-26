import csv

# Employee class
class Employee:

    def __init__(self):
        self.file = "employee.csv"

    # Add employee
    def add_employee(self):
        try:
            id = input("Enter employee id: ")
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")

            with open(self.file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([id, name, department, salary])

            print("Employee added successfully")

        except Exception as e:
            print("Error:", e)

    # Display employees
    def display_employee(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)

    # Search employee
    def search_employee(self):
        try:
            id = input("Enter employee id: ")

            with open(self.file, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == id:
                        print("Employee found")
                        print(row)
                        return

            print("Employee not found")

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)

    # Update employee
    def update_employee(self):
        try:
            id = input("Enter employee id: ")
            rows = []

            with open(self.file, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    rows.append(row)

            found = False

            for row in rows:
                if row[0] == id:
                    row[1] = input("Enter new name: ")
                    row[2] = input("Enter new department: ")
                    row[3] = input("Enter new salary: ")
                    found = True
                    break

            if found:
                with open(self.file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

                print("Employee updated successfully")
            else:
                print("Employee not found")

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)

    # Delete employee
    def delete_employee(self):
        try:
            id = input("Enter employee id: ")
            rows = []
            found = False

            with open(self.file, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == id:
                        found = True
                    else:
                        rows.append(row)

            if found:
                with open(self.file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

                print("Employee deleted successfully")
            else:
                print("Employee not found")

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)


# Main function
def main():

    employee = Employee()

    while True:

        print()
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Display Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee.add_employee()

        elif choice == "2":
            employee.display_employee()

        elif choice == "3":
            employee.search_employee()

        elif choice == "4":
            employee.update_employee()

        elif choice == "5":
            employee.delete_employee()

        elif choice == "6":
            print("Program ended")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()