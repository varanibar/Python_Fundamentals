import random


class Player:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.achievs = self.gen_player_achievements()

    def gen_player_achievements(self) -> set[str]:
        lst_achievs = Achievements().lst_achievs
        n = random.randrange(1, len(lst_achievs), 1)
        set_achievs = set(random.sample(lst_achievs, n))
        return set_achievs


class Achievements:
    lst_achievs = [
                    "Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"
                    ]


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = Player("alice")
    bob = Player("bob")
    charlie = Player("CHarlie")
    dylan = Player("DYLAN")
    tournament = [alice, bob, charlie, dylan]
    set_achievs = set(Achievements.lst_achievs)
    for player in tournament:
        print(f"Player {player.name}: {player.achievs}")
    print(f"\nAll distinct achievements: {set_achievs}\n")
    common_achievs = set_achievs
    for player in tournament:
        common_achievs = set.intersection(common_achievs, player.achievs)
    print(f"Common achievements: {common_achievs}\n")
    for player in tournament:
        others_achievs: set[str] = set()
        for other_player in tournament:
            if other_player != player:
                others_achievs = others_achievs | other_player.achievs
        unique_achievs = set.difference(player.achievs, others_achievs)
        print(f"Only {player.name} has: {unique_achievs}")
    print("")
    for player in tournament:
        diff = set.difference(set_achievs, player.achievs)
        print(f"{player.name} is missing: {diff}")


if __name__ == "__main__":
    main()
