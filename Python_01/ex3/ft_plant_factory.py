class Plant:
    def __init__(self, name, height, age, growth=0):
        self._name = name.capitalize()
        self._height = round(height, 1)
        self._age = age
        if growth == 0:
            self._growth = round(height / age, 1)
        else:
            self._growth = growth

    def grow(self):
        self._height = round(self._height + self._growth, 1)

    def age(self):
        self._age = self._age + 1

    def show(self):
        print(f"Created: {self._name}: {self._height}cm, {self._age} days old")


def ft_plant_factory():
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    factory = [rose, oak, cactus, sunflower, fern]
    for plant in factory:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
