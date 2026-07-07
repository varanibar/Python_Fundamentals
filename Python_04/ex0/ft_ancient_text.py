#!/usr/bin/env python3
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
            f: typing.IO[str] = open(file_name, "r")
            print("---\n")
            content = f.read()
            f.close()
            print(content)
            print(f"---\nFile '{file_name}' closed.\n")
        except Exception as err:
            print(f"Error opening file '{file_name}': {err}\n")


if __name__ == "__main__":
    main()
