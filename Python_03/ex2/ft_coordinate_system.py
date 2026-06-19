import math


def convert_float(f: float) -> None:
    try:
        float(f)
    except Exception as err:
        print(f"Error on parameter '{f}': {err}")


def get_player_pos(coordinates: str) -> tuple:
    print("Enter new coordinates as floats in format 'x,y,z': ", end="")
    print(f"{coordinates}")
    lst_coordinates = coordinates.split(",")
    # print(lst_coordinates)
    # print(len(lst_coordinates))
    if len(lst_coordinates) != 3:
        print("Invalid syntax")
    else:
            try:
                for coordinate in lst_coordinates:
                    float(coordinate)
                tup = tuple(lst_coordinates)
                print(f"Got a first tuple: {tup}")
            except Exception as err:
                print(f"Error on parameter '{coordinate}': {err}")





def main() -> None:
    print("=== Game Coordinate System ===\n")
    get_player_pos("hello world")
    print("")
    get_player_pos("1.0 ,2.5 , 3.0")
    print("")
    get_player_pos("4,abc, b")
    print("")
    get_player_pos("4,5,6")
    print("")
if __name__ == "__main__":
    main()
