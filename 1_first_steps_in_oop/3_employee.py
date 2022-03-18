MONTHS_IN_YEAR = 12


class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        annual_salary = self.salary * MONTHS_IN_YEAR
        return annual_salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary