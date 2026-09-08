from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(
        player_one: CreatureFactory,
        player_two: CreatureFactory
        ) -> None:
    creature_one = player_one.create_base()
    creature_two = player_two.create_base()
    print(creature_one.describe())
    print(" vs.")
    print(creature_two.describe())
    print(" fight!")
    print(creature_one.attack())
    print(creature_two.attack())


def main():
    print("Testing fire factory")
    flame_factory = FlameFactory()
    test_factory(flame_factory)
    print()

    print("Testing aqua factory")
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)
    print()

    print("Testing battle")
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
