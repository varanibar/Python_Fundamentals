#Class without using mehtod ___init__()
#we would need to set properties manually for each object

class Person:
    pass

person1 = Person()
person1.name = "jos"
person1.age = 15

print(person1.name)
print(person1.age)



# print("**************************************")
#Using the method __init__() allows us to create objects
class People:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# person0 = People("jos", 15)
# print(person0.name)
# print(person0.age)

person1 = People("andre", 35, 180)
print(person1.height)


print("**************************************")
#we can also create a method to show the information instead of us doing it ourselves
class Tree:
    def __init__(self, name, height, diameter):
        self.name = name
        self.height = height
        self.diameter = diameter
    def show_data(self):
        print(f"{self.name.capitalize()} is {self.height}m tall and {self.diameter}m wide.")

tree1 = Tree("chapeo", 5, 1)
tree1.show_data()


print("**************************************")
#The input can be assigned to the object but also can be modified before being assigned to the object
#it can also be validaded beforehand
class Fish:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = self.convert(weight)
        self.age = self.validate(age)
    def show_data(self):
        print(f"{self.name.capitalize()} weighs {self.weight}g and is {self.age} days old.")
    def convert(self, weight):
        print(f"weight in kg = {weight}")
        self.weight = weight * 1000
        print(f"weight in g = {self.weight}")
        return self.weight
    def validate(self, age):
        print(f"Age input: {age}")
        if age > 0:
            self.age = age
            return self.age
        else:
            print("Age must be positive")

goldfish = Fish("goldfish", 5, 1)
goldfish.show_data()
salmon = Fish("salmon", 5, -1)
salmon.show_data()
