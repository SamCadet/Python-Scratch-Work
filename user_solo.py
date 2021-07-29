class User:
    # make a user profile
    def __init__(self, firstName, lastName, age, postCount):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.postCount = postCount
        self.logins = 0

    def describeUser(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        print(f'\nThis user\'s name is {self.fullName}')
        print(f'\t{self.fullName} is {self.age} years old.')
        print(f'\t{self.fullName} has made {self.postCount} posts.')

    def greetUser(self):
        print(f'\nWelcome back, {self.fullName}.')

    def incrementLoginAttempts(self):
        self.fullName = f'{self.firstName} {self.lastName}'
        self.logins += 1
        if self.logins == 1:
            print(f'{self.fullName} tried to log in {self.logins} time.')
        else:
            print(f'{self.fullName} tried to log in {self.logins} times.')

    def resetLoginAttempts(self):
        if self.logins >= 5:
            self.logins = 0
            print(f'Your login attempts have been reset, {self.fullName}.')
        else:
            print(f'Please try again, {self.fullName}.')
