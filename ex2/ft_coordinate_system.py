import math


def get_player_pos() -> tuple[float, ...]:
    while (1):
        try:
            i = 0
            input_coord = input("Enter new coordinates as floats in format"
                                + "'x,y,z':")
            splitted = input_coord.split(',')
            result: list[float] = []
            error = False
            for element in splitted:
                i += 1
                try:
                    result.append(float(element))
                except ValueError as e:
                    print(f"Error on parameter '{element}': {e}")
                    error = True
            if (error):
                continue
            coord = tuple(result)
            if (i != 3):
                raise ValueError
            print(f"{coord}")
            break
        except ValueError:
            print("Invalid Syntax")
    return coord


if __name__ == "__main__":
    print("===Game Coordinate System ===")
    print("Get a first set of coordinates")
    coord1 = get_player_pos()
    print(f"Got a first tuple: {coord1}")
    x1, y1, z1 = coord1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center = round(math.sqrt((x1-0)**2 + (y1-0)**2 + (z1-0)**2), 4)
    print(f"Distance to center: {distance_center}")

    print("Get a second set of coordinates")
    coord2 = get_player_pos()
    print(f"Got a second tuple: {coord2}")
    x2, y2, z2 = coord2
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)
    print(f"Distance between the 2sets of coordinates: {distance}")
