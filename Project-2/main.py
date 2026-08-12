#User class definition
class User:
    #ctor
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}')

#User class object
user = User("Shiv")

#calling User class method
user.greeting()