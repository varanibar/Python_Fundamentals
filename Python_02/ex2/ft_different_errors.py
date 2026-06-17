def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 123
    else:
        print("Operation completed successfully")


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except Exception as err:
        print(f"Caught {err.__class__.__name__}: {err}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        test_error_types(operation_number)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
