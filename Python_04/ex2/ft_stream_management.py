#!/usr/bin/env python3
import sys
import typing


def ft_ancient_text() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_stream_management.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            f: typing.IO[str] = open(file_name, "r")
            print("---\n")
            content = f.read()
            f.close()
            print(content)
            print(f"---\nFile '{file_name}' closed.\n")
            ft_archive_creation()
        except Exception as err:
            print("[STDERR] Error opening file ", file=sys.stderr, end="")
            print(f"'{file_name}': {err}\n", file=sys.stderr)


def ft_archive_creation() -> None:
    print("Transform data:")
    print("---\n")
    f = open(sys.argv[1], "r")
    content = f.read()
    f.close()
    lst_lines = content.splitlines()
    lst_lines = [line + "#" for line in lst_lines]
    new_content = "\n".join(lst_lines)
    print(new_content)
    print("\n---\nEnter new file name (or empty): ", end="")
    new_file = sys.stdin.readline().rstrip("\n")
    if new_file == "":
        print("Not saving data")
    else:
        try:
            print(f"Saving data to '{new_file}'")
            f = open(new_file, "w")
            f.write(new_content)
            f.close()
            print(f"Data saved in file '{new_file}'.\n")
        except Exception as err:
            print("[STDERR] Error opening file ", file=sys.stderr, end="")
            print(f"'{new_file}': {err}\n", file=sys.stderr)
            print("Data not saved.\n")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
