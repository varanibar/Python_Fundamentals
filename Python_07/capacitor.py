from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("\n base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal("itself"))

    print("\n evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal("itself and others"))


def test_transfrom_factory(factory: TransformCreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("\n base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print(base_creature.attack())

    print("\n evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())
    print(evolved_creature.attack())


def main() -> None:
    print("=== Testing Creature with healing capability ===")
    healing_factory = HealingCreatureFactory()
    test_healing_factory(healing_factory)
    print()
    print()
    print("=== Testing Creature with transform capability ===")
    transform_factory = TransformCreatureFactory()
    test_transfrom_factory(transform_factory)

    print()


if __name__ == "__main__":
    main()
