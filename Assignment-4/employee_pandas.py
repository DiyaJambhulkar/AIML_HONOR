import pandas as pd


class Employee:

    def __init__(self):
        self.file = "employee.csv"

    def add(self):
        try:
            id = input("Enter employee id: ")
            name = input("Enter name: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")

            new_employee = pd.DataFrame(
                [[id, name, department, salary]],
                columns=["id", "name", "department", "salary"]
            )

            try:
                data = pd.read_csv(self.file)
                data = pd.concat([data, new_employee], ignore_index=True)
            except FileNotFoundError:
                data = new_employee

            data.to_csv(self.file, index=False)

            print("Employee added successfully")

        except Exception as e:
            print("Error:", e)

    def display(self):
        try:
            data = pd.read_csv(self.file)
            print(data)

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)

    def update(self):
        try:
            data = pd.read_csv(self.file)

            id = input("Enter employee id: ")
            salary = input("Enter new salary: ")

            found = False

            for i in range(len(data)):
                if str(data.loc[i, "id"]) == id:
                    data.loc[i, "salary"] = salary
                    found = True
                    break

            if found:
                data.to_csv(self.file, index=False)
                print("Employee updated successfully")
            else:
                print("Employee not found")

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            data = pd.read_csv(self.file)

            id = input("Enter employee id: ")

            if id in data["id"].astype(str).values:
                data = data[data["id"].astype(str) != id]
                data.to_csv(self.file, index=False)
                print("Employee deleted successfully")
            else:
                print("Employee not found")

        except FileNotFoundError:
            print("Employee file not found")

        except Exception as e:
            print("Error:", e)


employee = Employee()

while True:

    print()
    print("Employee Management System")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        employee.add()

    elif choice == "2":
        employee.display()

    elif choice == "3":
        employee.update()

    elif choice == "4":
        employee.delete()

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")