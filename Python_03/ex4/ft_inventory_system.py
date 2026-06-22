import sys

def ft_inventory_system() -> None:
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided")
    else:
        dict_items = dict()
        for arg in sys.argv[1:]:
            # print("\n")
            # print (arg)
            lst_object = arg.split(":")
            if len(lst_object) != 2:
                print(f"Error - invalid parameter '{arg}'")
            else:
                for key in dict_items.keys():
                    # print(f"{lst_object[0]} vs {key}")
                    if lst_object[0] == key:
                        print(f"Redundant item '{lst_object[0]}' - discarding")
                        break
                else:
                    # print("ELSE")
                    try:
                        key = lst_object[0].lower()
                        value = int(lst_object[1])
                        if value <= 0:
                            raise ValueError(f"quantity must be a positive number '{value}'")
                        dict_items[key] = value
                    except ValueError as err:
                        print(f"Quantity error for '{lst_object[0]}': {err}")

        # dict_items[object[0]] = {object[1]}
        print(f"Got inventory: {dict_items}")
        lst_items = list((dict_items.keys()))
        print(f"Item list: {lst_items}")
        total_items = len(dict_items)
        total_items_qty = sum(dict_items.values())
        print(f"Total quantity of the {total_items} items: {total_items_qty}")
        most_abundant_qty = 0
        least_abundant_item = lst_items[0]
        least_abundant_qty = dict_items[least_abundant_item]
        for item in dict_items.keys():
            item_qty = dict_items[item]
            n = round(item_qty * 100 / total_items_qty, 1)
            print(f"Item {item} represents {n}%")
            if most_abundant_qty < item_qty:
                most_abundant_item = item
                most_abundant_qty = dict_items[item]
            if least_abundant_qty > item_qty:
                least_abundant_item = item
                least_abundant_qty = dict_items[item]
        print(f"Item most abundant: {most_abundant_item} with quantity {most_abundant_qty}")
        print(f"Item least abundant: {least_abundant_item} with quantity {least_abundant_qty}")





def main() -> None:
    print("=== Inventory System Analysis ===")
    ft_inventory_system()


if __name__ == "__main__":
    main()
