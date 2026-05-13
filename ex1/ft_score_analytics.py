import sys


def ft_score_analytics() -> None:

    argc = len(sys.argv)
    score = 0
    tab = []  # type: list
    i = 0
    while (i < argc):
        try:
            tab[i] = int(sys.argv[i])
            score += int(sys.argv[i])
        except ValueError:
            print(f"Invalid Parameter: '{sys.argv[i]}'")
        i += 1
    max_value = max(tab)
    min_value = min(tab)
    range = (max_value - min_value)
    print(f""" ===Player Score Analytics\n
Total Players: {argc}
Total score: {score}
High score: {max_value}
Lowest score: {min_value}
Score range: {range}
""")


if __name__ == "__main__":
    ft_score_analytics()
