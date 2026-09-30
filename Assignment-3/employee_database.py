import pymysql


class Employee:

    def __init__(self):
        self.con = pymysql.connect(
            host="localhost",
            user="root",
            password="Diya#2007",
            database="employee"
        )

    def add(self):
        try:
            cur = self.con.cursor()

            id = input("Enter employee id: ")
            name = input("Enter name: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")

            cur.execute(
                "INSERT INTO employee VALUES (%s,%s,%s,%s)",
                (id, name, department, salary)
            )

            self.con.commit()

            print("Employee added successfully")

        except Exception as e:
            print("Error:", e)

    def display(self):
        try:
            cur = self.con.cursor()

            cur.execute("SELECT * FROM employee")

            rows = cur.fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print("Error:", e)

    def update(self):
        try:
            cur = self.con.cursor()

            id = input("Enter employee id: ")
            salary = input("Enter new salary: ")

            cur.execute(
                "UPDATE employee SET salary=%s WHERE id=%s",
                (salary, id)
            )

            self.con.commit()

            print("Employee updated successfully")

        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            cur = self.con.cursor()

            id = input("Enter employee id: ")

            cur.execute(
                "DELETE FROM employee WHERE id=%s",
                (id,)
            )

            self.con.commit()

            print("Employee deleted successfully")

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