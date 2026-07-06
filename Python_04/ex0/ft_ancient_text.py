import sys
import typing


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            file: typing.IO[str] = open(file_name, "r")
            print("---\n")
            print(file.read(), end="")
            print("---")
            file.close()
            print(f"File '{file_name}' closed.")
        except Exception as err:
            print(f"Error opening file '{file_name}': {err}\n")


if __name__ == "__main__":
    main()
