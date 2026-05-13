import sys


def ft_inventory_system() -> dict:
    argc = len(sys.argv)
    inventory_dict: dict = {}
    i = 1
    while (i < argc):
        splitted = sys.argv[i].split(":")
        inventory_dict[splitted[0]] = int(splitted[1])
        i += 1
    print(f"{inventory_dict}")
    return inventory_dict


if __name__ == "__main__":
    ft_inventory_system()
