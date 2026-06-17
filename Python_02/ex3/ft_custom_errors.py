class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_plant_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(f"Caught {err.__class__.__name__}: {err}")


def test_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(f"Caught {err.__class__.__name__}: {err}")


def test_garden_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as err:
        print(f"Caught GardenError: {err}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    test_plant_error()
    print("\nTesting WaterError...")
    test_water_error()
    print("\nTesting catching all garden errors...")
    test_garden_error()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
