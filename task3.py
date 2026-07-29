##part 1
class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def calculate_salary(self):
        return 0


##part2
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, monthly_salary):
        super().__init__(emp_id, name, age)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, hours_worked, hourly_rate):
        super().__init__(emp_id, name, age)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class Freelancer(Employee):
    def __init__(self, emp_id, name, age, project_rate, completed_projects):
        super().__init__(emp_id, name, age)
        self.project_rate = project_rate
        self.completed_projects = completed_projects

    def calculate_salary(self):
        return self.project_rate * self.completed_projects

##part3

employees = [
    FullTimeEmployee(201, "Sara", 28, 6500),
    PartTimeEmployee(202, "Omar", 21, 60, 25),
    Freelancer(203, "Mona", 33, 1400, 3)
]

print(" Employee Management System ")

for emp in employees:
    emp.display_info()
    print("Salary: $", emp.calculate_salary())
    print("-" * 50)

##part 4

total_payroll = 0
highest_salary = employees[0]

for emp in employees:
    total_payroll += emp.calculate_salary()

    if emp.calculate_salary() > highest_salary.calculate_salary():
        highest_salary = emp

print(" Employee Report ")
print("Total Employees:", len(employees))
print("Total Payroll: $", total_payroll)
print("Highest Salary Employee:", highest_salary.name)
print("Highest Salary: $", highest_salary.calculate_salary())