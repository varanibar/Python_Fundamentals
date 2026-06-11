class Plant:
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float = 0
                ) -> None:
        self._name = name.capitalize()
        if height < 0.0:
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
            print("Setting height to 0.0cm")
        else:
            self._height = round(height, 1)
        if age < 0:
            self._age = 0
            print(f"{self._name}: Error, age can't be negative")
            print("Setting age to 0 days")
        else:
            self._age = age
        self._growth = growth

    def grow(self, days: int) -> None:
        self._height = round(self._height + (self._growth * days), 1)

    def age(self, days: int) -> None:
        self._age += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height > 0.0:
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
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                color: str
                ) -> None:
        super().__init__(name, height, age)
        self._color = color.lower()
        self._bloom = 0

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom == 1:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {(self._name).lower()} to bloom]")
        self._bloom = 1
        self.show()


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                trunk_diameter: float
                ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {(self._name).lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide")


class Vegetable(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float,
                harvest_season: str
                ) -> None:
        super().__init__(name, height, age, growth)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age_and_grow(self, days: int) -> None:
        print(f"[make {(self._name).lower()} grow and age for {days} days]")
        super().age(days)
        super().grow(days)
        self._nutritional_value = days
        self.show()


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, 2.1, "april")
    tomato.show()
    tomato.age_and_grow(20)


if __name__ == "__main__":
    ft_plant_types()
