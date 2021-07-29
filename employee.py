

class Employee:
    def __init__(self, firstName, lastName, annualSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary

    def giveRaise(self, raiseAmount=5000):
        self.fullName = f'{self.firstName} {self.lastName}'
        if raiseAmount:
            self.raiseAmount = raiseAmount
        self.newSalary = self.annualSalary + self.raiseAmount
        print(f'\n{self.fullName} got a raise to the tune of ${self.raiseAmount}.')
        print(f'\n{self.fullName}\'s new salary is ${self.newSalary} per year.')


# rondell = Employee('Rondell', 'Williams', 89200)
# rondell.giveRaise()
