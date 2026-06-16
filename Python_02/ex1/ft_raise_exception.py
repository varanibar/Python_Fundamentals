def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature(temp_str: str) -> None:
    print(f"\nInput data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except Exception as err:
        print("Caught input_temperature error: ", end="")
        print(f"{err}")


def ft_raise_exception() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_raise_exception()
