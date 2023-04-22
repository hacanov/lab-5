class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Employee(Person):
    def __init__(self, name: str, age: int, gender: str, position: str, salary: float):
        super().__init__(name, age, gender)
        self.position = position
        self.salary = salary

    def get_info(self):
        return super().get_info() + f", Position: {self.position}, Salary: {self.salary}"


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employees_info(self):
        employees_info = []
        for employee in self.employees:
            employees_info.append(employee.get_info())
        return employees_info


person = Person("Jon", 30, "Men")
print(person.get_info())
employee = Employee("Janet", 23, "Female", "Manager", 9000.0)
print(employee.get_info())
department = Department("IT Department")
department.add_employee(employee)
print(department.get_employees_info())
 