from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.creatures import HealingCreature, TransformCreature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(f">>> {creature.name} goes for Normal strategy")
            print(creature.attack())

        else:
            raise Exception("Invalid Creature")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCreature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            transform_creature: TransformCreature = cast(
                TransformCreature, creature)
            print(f">>> {transform_creature.name} "
                  "goes for Agressive strategy")
            print(transform_creature.transform())
            print(transform_creature.attack())
            print(transform_creature.revert())

        else:
            raise Exception(
                f"Invalid Creature {creature.name} "
                "for the agressive strategy"
                f"\n{creature.name} "
                "does not have transforming capabilities."
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealingCreature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            healing_creature: HealingCreature = cast(HealingCreature, creature)
            print(f">>> {healing_creature.name} goes for Defensive strategy ")
            print(healing_creature.attack())
            print(healing_creature.heal("itself"))

        else:
            raise Exception(
                f"Invalid Creature {creature.name} "
                "for the defensive strategy"
                f"\n{creature.name} "
                "does not have healing capabilities."
                )
