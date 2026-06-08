class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int
                ) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height > 0.0 and self._height == 0.0:
            self._height = round(new_height, 1)
        elif new_height > 0.0:
            self._height = round(new_height, 1)
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            if self._height != 0:
                print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0 and self._age == 0:
            self._age = new_age
        elif new_age > 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            if self._age != 0:
                print("Age update rejected")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print("")
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-10.0)
    plant.set_age(-50)
    print("")
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
