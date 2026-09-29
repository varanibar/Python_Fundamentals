from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Agumon(Creature):
    def __init__(self) -> None:
        super().__init__("Agumon", "Fire")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Pepper Breath!"


class Greymon(Creature):
    def __init__(self) -> None:
        super().__init__("Greymon", "Fire")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Mega Flame!"


class Gomamon(Creature):
    def __init__(self) -> None:
        super().__init__("Gomamon", "Water")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Marching Fishes!"


class Ikkakumon(Creature):
    def __init__(self) -> None:
        super().__init__("Ikkakumon", "Water/Ice")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Harpoon Torpedo!"
