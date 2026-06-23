import sys


class Inventory:
    def __init__(self) -> None:
        self.dict_items = self.ft_inventory_system()

    def ft_inventory_system(self) -> dict[str, int]:
        dict_items: dict[str, int] = dict()
        for arg in sys.argv[1:]:
            argv = arg.split(":")
            if len(argv) != 2:
                print(f"Error - invalid parameter '{arg}'")
            else:
                for key in dict_items.keys():
                    if argv[0] == key:
                        print(f"Redundant item '{argv[0]}' - discarding")
                        break
                else:
                    try:
                        key = argv[0].lower()
                        value = int(argv[1])
                        if value < 0:
                            raise ValueError(
                                f"quantity must be a (+) number: '{value}'"
                                )
                    except ValueError as err:
                        print(f"Quantity error for '{argv[0]}': {err}")
                    else:
                        dict_items[key] = value
        return dict_items

    def ft_inventory_stats(self) -> None:
        print(f"Got inventory: {self.dict_items}")
        lst_items = list((self.dict_items.keys()))
        total_items = len(self.dict_items)
        total_items_qty = sum(self.dict_items.values())
        print(f"Item list: {lst_items}")
        print(f"Total quantity of the {total_items} items: {total_items_qty}")
        most_qty = 0
        least_item = lst_items[0]
        least_qty = self.dict_items[least_item]
        for item in self.dict_items.keys():
            item_qty = self.dict_items[item]
            n = round(item_qty * 100 / total_items_qty, 1)
            print(f"Item {item} represents {n}%")
            if most_qty < item_qty:
                most_item = item
                most_qty = self.dict_items[item]
            if least_qty > item_qty:
                least_item = item
                least_qty = self.dict_items[item]
        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

    def ft_inventory_update(self, new_item: dict[str, int]) -> None:
        self.dict_items.update(new_item)
        print(f"Updated inventory: {self.dict_items}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided")
    else:
        inventory = Inventory()
        inventory.ft_inventory_stats()
        new_item = {"magic_item": 1}
        inventory.ft_inventory_update(new_item)


if __name__ == "__main__":
    main()
