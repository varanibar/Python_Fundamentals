import sys


def main() -> None:
    argc = len(sys.argv)
    print("=== Player Score Analytics ===")
    list_scores: list[int] = []
    list_invalid: list[str] = []

    for i in range(1, argc):
        try:
            nbr = int(sys.argv[i])
            list_scores.append(nbr)
        except Exception:
            list_invalid.append(sys.argv[i])

    if len(list_invalid):
        for invalid in list_invalid:
            print(f"Invalid parameter: '{invalid}'")

    if len(list_scores):
        print("Scores processed: ", end="")
        print(list_scores)
        total_players = len(list_scores)
        print(f"Total players: {total_players}")

        total_score = 0
        for score in list_scores:
            total_score += score
        print(f"Total score: {total_score}")

        try:
            average_score = round(total_score / total_players, 1)
        except OverflowError as err:
            print(f"Average score: {err.__class__.__name__}: {err}")
        high_score = max(list_scores)
        low_score = min(list_scores)
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}\n")

    else:
        print("No scores provided. Usage: ", end="")
        print("python3 ft_score_analytics.py <score1> <score2> ...\n")


if __name__ == "__main__":
    main()
