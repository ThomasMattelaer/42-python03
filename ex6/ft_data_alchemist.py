import random


if __name__ == "__main__":
    players_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
                    'john', 'kevin', 'Liam']
    all_capitalized_list = [element.capitalize() for element in players_list]
    only_capitalized_list = [element for element in players_list
                             if element == element.capitalize()]
    dict_capitalize = {element: random.randint(0, 1000)
                       for element in all_capitalized_list}
    average = round(sum(dict_capitalize.values()) / len(dict_capitalize), 2)
    dict_average = {key: dict_capitalize[key] for key in dict_capitalize
                    if dict_capitalize[key] > average}
    print(f"Initial list of players: {players_list}")
    print(f"new list with all names capitalized: {all_capitalized_list}")
    print(f"New list of capitalized names only: {only_capitalized_list}")
    print(f"Score dict: {dict_capitalize}")
    print(f"Score average: {average}")
    print(f"High scores: {dict_average}")
