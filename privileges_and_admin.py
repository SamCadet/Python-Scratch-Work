from user_solo import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can make announcements']

    def showPrivileges(self):
        print(
            f'\n An admin has the following privileges.\n\n{self.privileges}')


class Admin(User):
    def __init__(self, firstName, lastName, age, postCount):
        super().__init__(firstName, lastName, age, postCount)
        self.privileges = Privileges()
