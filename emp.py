import mysql.connector

# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="emp"
)

cursor = connection.cursor()

def add_employee(name, age, department, salary):
    sql = "INSERT INTO employees (name, age, department, salary) VALUES (%s, %s, %s, %s)"
    val = (name, age, department, salary)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee {name} added successfully.")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    for emp in result:
        print(emp)

def update_employee(emp_id, name, age, department, salary):
    sql = "UPDATE employees SET name=%s, age=%s, department=%s, salary=%s WHERE id=%s"
    val = (name, age, department, salary, emp_id)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee {emp_id} updated successfully.")

def delete_employee(emp_id):
    sql = "DELETE FROM employees WHERE id=%s"
    val = (emp_id,)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee {emp_id} deleted successfully.")

def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            add_employee(name, age, department, salary)
        
        elif choice == '2':
            view_employees()
        
        elif choice == '3':
            emp_id = int(input("Enter Employee ID to update: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            update_employee(emp_id, name, age, department, salary)
        
        elif choice == '4':
            emp_id = int(input("Enter Employee ID to delete: "))
            delete_employee(emp_id)
        
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

menu()
connection.close()