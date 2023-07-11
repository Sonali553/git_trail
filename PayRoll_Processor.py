class Salaried_Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculatePay(self):
        return self.salary
class Hourly_Employee:
    def __init__(self, name, hourlyRate, hoursWorked):
        self.name = name
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked
    def calculatePay(self):
        weeklyPay = self.hourlyRate * self.hoursWorked
        return weeklyPay
obj1 = Hourly_Employee("Ram", 1000, 10)
obj2 = Salaried_Employee("suresh", 80000)
print(obj1.calculatePay())
print(obj2.calculatePay())