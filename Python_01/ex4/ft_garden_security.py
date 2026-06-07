class Plant:
    def __init__(self, name, height, age, growth=0):
        self._name = name.capitalize()
        self.__height = round(height, 1)
        self.__age = age
        # else:
        #     print(f"{self._name}: Error, height can't be negative")
        # if age > 0:
        #     self.__age = round(age, 0)
        # else:
        #     print(f"{self._name}: Error, age can't be negative")
        #     self.__age = 0
        if growth == 0:
            self._growth = round(height / age, 1)
        else:
            self._growth = growth

    def grow(self):
        self.__height = round(self.__height + self._growth, 1)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.__age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self):
        if self.get_age() > 0:

                print(f"Plant created: {self._name}: {self.__height}cm, {self.__age} days old")
        else:
            print("Error")

def ft_garden_security():
    plant = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    plant.show()
    print("")

    plant.set_age(-30)
    print("")


if __name__ == "__main__":
    ft_garden_security()
