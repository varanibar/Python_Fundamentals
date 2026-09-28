from ex0.factories import CreatureFactory
from .creatures import (HealingCreature,
                        TransformCreature,
                        Patamon,
                        Angemon,
                        Gabumon,
                        Garurumon)


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealingCreature:
        return Patamon()

    def create_evolved(self) -> HealingCreature:
        return Angemon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> TransformCreature:
        return Gabumon()

    def create_evolved(self) -> TransformCreature:
        return Garurumon()
