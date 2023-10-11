"""
Design an employee class for reading and displaying the
employee information, the getInfo() and displayInfo() methods
will be used respectively. Where getInfo() will be a private
method.
"""

class employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id_ = emp_id
        self.name_ = name
        self.salary_ = salary

    def displayInfo(self):
        print(f"Information of {self.emp_id_}")
        print("Name : ", self.name_)
        print("Salary : {}".format(self.salary_))

employees = []
noOfEmp = input("Enter a num of employee you want to add : ")
start = 1
while(start <= int(noOfEmp)):
    emp_data = {}
    id = input("Enter EMP_ID: ")
    name = input("Enter a Name: ")
    salary = input("Enter a salary: ")
    salary = int(salary)
    emp1 = employee(id, name, salary)
    # emp1.displayInfo()
    emp_data['EMP_ID'] = id
    emp_data['NAME'] = name
    emp_data['SALARY'] = salary
    employees.append(emp_data)
    start += 1

print(employees)
