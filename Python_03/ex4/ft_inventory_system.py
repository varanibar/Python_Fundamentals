import sys

def ft_inventory_system() -> None:
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided")
    else:
        i = 1
        dict_inventory = dict()

        for arg in sys.argv[1:]:
            lst_object = arg.split(":")
            if len(lst_object) != 2:
                print(f"Error - invalid parameter '{arg}'")
                break
            for key in dict_inventory.keys():
                if lst_object[0] == key:
                    print(f"Redundant item '{lst_object[0]}' - discarding")
                    break
            else:
                try:
                    key = lst_object[0].lower()
                    value = int(lst_object[1])
                    dict_inventory[key] = value
                except ValueError as err:
                    print(f"Quantity error for '{lst_object[0]}': {err}")
            i += 1

        # dict_inventory[object[0]] = {object[1]}
        print(f"Got inventory: {dict_inventory}")
        lst_items = list((dict_inventory.keys()))
        print(f"Item list: {lst_items}")
        total_items = sum(dict_inventory.values())
        print(f"Total quantity of the {len(lst_items)} items: {total_items}")
        for item in dict_inventory.keys():
            
            print(f"Item {item} represents {}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    ft_inventory_system()


if __name__ == "__main__":
    main()
