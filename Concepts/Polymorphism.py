'''
The word "polymorphism" means "many forms", and in programming
it refers to methods/functions/operators with the same name that
can be executed on many objects or classes.
'''
# Function Polymorphism
# The function len() is polymorphic because it can be used on
# different objects

len("hello")
len(["a", "b"])

# Class Polymorphism
# there can be multiple classes with the same method name,
# and because of polymorphism, we can execute the same method
# for all three classes

class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        print("woff!")

class Cat:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        print("meow!")

class Duck:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        print("quack!")

dog = Dog("Doggo")
cat = Cat("Catto")
duck = Duck("Duckie")

for _ in (dog, cat, duck):
    _.talk()
print()


# Inheritance Class Polymorphism
# The child classes inherit the properties and mehtods from
# the parent class but because of polymorphism we can execute
# the same method for all classes.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def move(self) -> None:
        print("Run!")

class Horse(Animal):
    pass

class Snake(Animal):
    def move(self) -> None:
        print("Crawl!")

class Bird(Animal):
    def move(self) -> None:
        print("Fly!")

horse = Horse("horsie")
snake = Snake("snakie")
bird = Bird("birdie")

for _ in (horse, snake, bird):
    print(_.name,": ",end="")
    _.move()
