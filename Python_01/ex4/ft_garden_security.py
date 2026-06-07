class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float = 0) -> None:
        self._name = name.capitalize()
        if height > 0:
            self._height = round(height, 1)
        else:
            self._height = 0
            print(f"{self._name}: Error, height can't be negative")
        if age > 0:
            self._age = age
        else:
            self._age = 0
            print(f"{self._name}: Error, age can't be negative")
        if growth == 0:
            self._growth = round(height / age, 1)
        else:
            self._growth = growth

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 1)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self._height = round(new_height, 1)
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        if self._height > 0 and self._age > 0:
            print(f"{self._name}: {self._height}cm, {self._age} days old")


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-10)
    plant.set_age(-50)
    print("")
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
