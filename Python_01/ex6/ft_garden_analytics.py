class Plant:
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float = 0
                ) -> None:
        self._name = name.capitalize()
        self._stats = self.Statistics()
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

    class Statistics:
        def __init__(self) -> None:
            self._number_grow = 0
            self._number_age = 0
            self._number_show = 0

    def show_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        print("Stats: ", end="")
        print(f"{self._stats._number_grow} grow, ", end="")
        print(f"{self._stats._number_age} age, ", end="")
        print(f"{self._stats._number_show} show")

    @staticmethod
    def is_year_old(age: int) -> None:
        print(f"Is {age} days more than a year? -> ", end="")
        if age > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def grow(self, days: int) -> None:
        self._stats._number_grow += 1
        self._height = round(self._height + (self._growth * days), 1)

    def age(self, days: int) -> None:
        self._stats._number_age += 1
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
        self._stats._number_show += 1
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float,
                color: str
                ) -> None:
        super().__init__(name, height, age, growth)
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
        self._bloom = 1


class Seed(Flower):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float,
                color: str,
                seeding: int = 42
                ) -> None:
        super().__init__(name, height, age, growth, color)
        self._number_seeds = 0
        self._seeding = seeding

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._number_seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._number_seeds += self._seeding


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                growth: float,
                trunk_diameter: float
                ) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter
        self._number_shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()
        print(f" {self._number_shade} shade")

    def produce_shade(self) -> None:
        self._number_shade += 1
        print(f"[asking the {(self._name).lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    Plant.is_year_old(30)
    Plant.is_year_old(400)

    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, 8.0, "red")
    rose.show()
    rose.show_stats()
    print(f"[asking the {(rose._name).lower()} to grow and bloom]")
    rose.grow(1)
    rose.bloom()
    rose.show()
    rose.show_stats()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 0.0, 5.0)
    oak.show()
    oak.show_stats()
    oak.produce_shade()
    oak.show_stats()

    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, 1.5, "yellow")
    sunflower.show()
    print(f"[make {sunflower._name.lower()} grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    sunflower.show_stats()

    print("\n=== Anonymous")
    unknown_plant = Plant.anonymous()
    unknown_plant.show()
    unknown_plant.show_stats()


if __name__ == "__main__":
    ft_garden_analytics()
