class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    name_caps = plant_name.capitalize()
    if plant_name == name_caps:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(garden: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in garden:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught {err.__class__.__name__}: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants..")
    garden = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(garden)
    print("\nTesting invalid plants..")
    garden = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(garden)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
