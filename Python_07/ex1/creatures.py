from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Patamon(Creature):
    def __init__(self) -> None:
        super().__init__("Patamon", "Air")

    def attack(self) -> str:
        return super().attack("Boom Bubble")


class Angemon(Creature):
    def __init__(self) -> None:
        super().__init__("Angemon", "Angel")

    def attack(self) -> str:
        return super().attack("Hand of Fate")


class Gabumon(Creature):
    def __init__(self) -> None:
        super().__init__("Gabumon", "Ice")

    def attack(self) -> str:
        return super().attack("Blue Blaster")


class Garurumon(Creature):
    def __init__(self) -> None:
        super().__init__("Garurumon", "Ice")

    def attack(self) -> str:
        return super().attack("Howling Blaster")


