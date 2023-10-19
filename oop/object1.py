class Employee:
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)
emp_3 = Employee('Corey', 'Schafer', 70000)

