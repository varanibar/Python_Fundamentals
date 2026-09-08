from abc import ABC, abstractmethod
from .creatures import Creature, Agumon, Greymon, Gomamon, Ikkakumon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Agumon()

    def create_evolved(self) -> Creature:
        return Greymon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Gomamon()

    def create_evolved(self) -> Creature:
        return Ikkakumon()
