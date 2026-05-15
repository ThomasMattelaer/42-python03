import sys


def ft_inventory_system() -> dict[str, int]:
    argc = len(sys.argv)
    inventory_dict: dict[str, int] = {}
    i = 1
    if argc == 1:
        print("Error - No parameters provided")
        return inventory_dict
    while (i < argc):
        try:
            splitted = sys.argv[i].split(":")
            if (splitted[0] in inventory_dict):
                raise ValueError(f"Redundant item: '{splitted[0]}'" +
                                 "- discarding")
            if (len(splitted) != 2):
                raise ValueError(f"Error - Invalid parameter {sys.argv[i]}")
            try:
                inventory_dict[splitted[0]] = int(splitted[1])
            except ValueError as e:
                print(f"Quantity Error: {e}")
        except ValueError as e:
            print(f"{e}")
        i += 1
    return inventory_dict


if __name__ == "__main__":
    inventory_dict = ft_inventory_system()
    item_list = list(inventory_dict.keys())
    if len(item_list) > 0:
        sum = sum(inventory_dict.values())
        max_values = 0
        min_values = float('inf')
        max_key = ""
        min_key = ""
        print("=== Inventory System Analysis ===")
        print(f"Got inventory: {inventory_dict}")
        print(f"Item list: {item_list}")
        print(f"Total quantity of the {len(item_list)} items: {sum}")
        for key in inventory_dict:
            percentage = round((inventory_dict[key] / sum) * 100, 1)
            print(f"Item {key} represents {percentage}%")
            if (inventory_dict[key] >= max_values):
                max_key = key
                max_values = inventory_dict[key]
            if (inventory_dict[key] <= min_values):
                min_key = key
                min_values = inventory_dict[key]
        print(f"Item most abundant: {max_key}" +
            f" with quantity {inventory_dict[max_key]}")
        print(f"Item least abundant: {min_key}" +
            f" with quantity {inventory_dict[min_key]}")
        inventory_dict.update({"magic_item": 15})
        print(f"Updated inventory: {inventory_dict}")
