# Parent Class
class Parent:
    def __init__(self):
        self.name = "parent"

    def say_hello(self):
        self.say_goodbye()
        print("Hello, my name is", self.name)

# Child Class
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.nickname = self.name

    def say_goodbye(self):
        print("Goodbye, my name is", self.nickname)

parent = Parent()
child = Child()

child.say_hello()
# parent.say_hello()