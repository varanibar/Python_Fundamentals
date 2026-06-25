import random


def create_dict(lst_names: list[str]) -> None:

    dict_scores = {name: random.randint(1, 1000)
                   for name in lst_names}
    total = sum(dict_scores.values())
    score_average: float = round(total / len(dict_scores), 2)
    dict_high_scores = {name: dict_scores[name]
                        for name in dict_scores
                        if dict_scores[name] > score_average}
    print("\nScore dict: ", dict_scores)
    print("Score average is ", score_average)
    print("High scores: ", dict_high_scores)


def ft_data_alchemist(lst_names: list[str]) -> None:
    names_all_caps = [name.capitalize()
                      for name in lst_names]
    names_only_caps = [name for name in lst_names
                       if name == name.capitalize()]
    print("New list with all names capitalized: ", names_all_caps)
    print("New list of capitalized names only: ", names_only_caps)
    create_dict(names_all_caps)


def main() -> None:
    print("=== Game Data Alchemist ===")
    lst_names = ["Frodo", "Sam", "aragorn", "Merry", "pippin", "gandalf"]
    print("\nInitial list of players:", lst_names)
    ft_data_alchemist(lst_names)


if __name__ == "__main__":
    main()
