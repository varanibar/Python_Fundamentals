class Plant:
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float = 0.0
                ) -> None:
        self._name = name.capitalize()
        self._height = round(height, 1)
        self._age = age
        if growth == 0.0:
            self._growth = round(height / age, 1)
        else:
            self._growth = growth

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 1)

    def age(self) -> None:
        self._age = self._age + 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


def ft_plant_growth() -> None:
    flower = Plant("rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    flower.show()
    week = range(1, 8, 1)
    for day in week:
        print(f"=== Day {day} ===")
        flower.grow()
        flower.age()
        flower.show()
    print(f"Growth this week: {round(flower._growth * day, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
