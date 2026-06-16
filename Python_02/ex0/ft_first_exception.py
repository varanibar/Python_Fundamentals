def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    print(f"\nInput data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print("Caught input_temperature error: ", end="")
        print(f"{err}")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
