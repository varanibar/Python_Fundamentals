import math


def get_player_pos() -> tuple[float, ...]:
    coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
    lst_coordinates = coordinates.split(",")
    if len(lst_coordinates) != 3:
        print("Invalid syntax")
        return get_player_pos()
    else:
        try:
            i = 0
            lst_xyz: list[float] = []
            while i < 3:
                nbr = float(lst_coordinates[i])
                lst_xyz.append(nbr)
                i += 1
        except Exception as err:
            print(f"Error on parameter '{lst_coordinates[i]}': {err}")
            return get_player_pos()
        else:
            return tuple(lst_xyz)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tup_1 = get_player_pos()
    print(f"Got a first tuple: {tup_1}")
    print(f"It includes: X={tup_1[0]}, Y={tup_1[1]}, Z={tup_1[2]}")
    dist = math.sqrt((tup_1[0]**2 + tup_1[1]**2 + tup_1[2]**2))
    print(f"Distance to center: {round(dist, 4)}\n")
    print("Get a second set of coordinates")
    tup_2 = get_player_pos()
    total = 0.0
    i = 0
    while i < 3:
        total += (tup_2[i] - tup_1[i])**2
        i += 1
    dist = math.sqrt((total))
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}\n")


if __name__ == "__main__":
    main()
