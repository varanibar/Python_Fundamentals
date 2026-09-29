from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class HealingCreature(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)


class TransformCreature(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.transformed = False


class Patamon(HealingCreature):
    def __init__(self) -> None:
        super().__init__("Patamon", "Air")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Boom Bubble!"

    def heal(self, target: str) -> str:
        return f"Heal! {self.name} heals {target} for a small amount!"


class Angemon(HealingCreature):
    def __init__(self) -> None:
        super().__init__("Angemon", "Angel")

    def attack(self) -> str:
        return f"Attack! {self.name} uses Hand of Fate!"

    def heal(self, target: str) -> str:
        return f"Heal! {self.name} heals {target} for a large amount"


class Gabumon(TransformCreature):
    def __init__(self) -> None:
        super().__init__("Gabumon", "Ice")

    def attack(self) -> str:
        if self.transformed is True:
            return f"Attack! {self.name} performs a boosted strike!"
        return f"Attack! {self.name} uses Blue Blaster!"

    def transform(self) -> str:
        self.transformed = True
        return f"Transform! {self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"Revert! {self.name} returns to initial form."


class Garurumon(TransformCreature):
    def __init__(self) -> None:
        super().__init__("Garurumon", "Ice")

    def attack(self) -> str:
        if self.transformed is True:
            return (f"Attack! {self.name} unleashes a devastating strike!")

        return f"Attack! {self.name} uses Howling Blaster!"

    def transform(self) -> str:
        self.transformed = True
        return f"Transform! {self.name} morphs into a mighty battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"Revert! {self.name} stabilizes its form."
