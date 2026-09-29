from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
    )


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved", end="")
    idx = 0
    for i in range(0, len(opponents) - 1):
        for j in range(1, len(opponents)):
            if i is not j:
                (factory_i, strategy_i) = opponents[i]
                (factory_j, strategy_j) = opponents[j]
                base_creature_i = factory_i.create_base()
                base_creature_j = factory_j.create_base()

                print("\n\n_____________")
                print(f"** Match {idx} **")
                idx += 1
                print("Opponents:")
                print(f"   {base_creature_i.name} from "
                      f"{factory_i.__class__.__name__}")
                print(f"   {base_creature_j.name} from "
                      f"{factory_j.__class__.__name__}")
                print("\n* Battle *")
                print(base_creature_i.describe())
                print(" vs.")
                print(base_creature_j.describe())
                print(" now fight!\n")

                try:
                    strategy_i.act(base_creature_i)
                    print()
                    strategy_j.act(base_creature_j)
                except Exception as err:
                    print(f"Battle error, aborting tournament: {err}")


def main() -> None:
    normal_strategy = NormalStrategy()
    agressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("\n_________________________________________________\n")
    print("=== Tournament 0 (basic) ===")
    print("[ (Fire+Normal), (Healing+Defensive) ]\n")
    opponents = [(flame_factory, normal_strategy),
                 (healing_factory, defensive_strategy)]
    battle(opponents)

    print("\n\n\n_________________________________________________\n")
    print("=== Tournament 1 (error) ===")
    print("[ (Fire+Aggressive), (Healing+Defensive) ]\n")
    opponents = [(flame_factory, agressive_strategy),
                 (healing_factory, defensive_strategy)]
    battle(opponents)

    print("\n\n\n_________________________________________________\n")
    print("=== Tournament 2 (multiple) ===")
    print("[ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]\n")
    opponents = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, agressive_strategy)]
    battle(opponents)
    print()


if __name__ == "__main__":
    main()
