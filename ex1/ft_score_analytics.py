import sys


def ft_score_analytics() -> None:
    argc = len(sys.argv)
    tab = []  # type: list
    i = 1
    print("===Player Score Analytics ===\n")
    while (i < argc):
        try:
            tab.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid Parameter: '{sys.argv[i]}'")
        i += 1
    length = len(tab)
    if (length > 0):
        score = sum(tab)
        max_value = max(tab)
        min_value = min(tab)
        range = (max_value - min_value)
        average_score = score / length
        print(f"""Score processed: {tab}
Total Players: {length}
Total score: {score}
Average score: {average_score}
High score: {max_value}
Lowest score: {min_value}
Score range: {range}
""")
    else:
        print(f"No scores provided. Usage: {sys.argv[0]} <score1> <score2> ..")


if __name__ == "__main__":
    ft_score_analytics()
