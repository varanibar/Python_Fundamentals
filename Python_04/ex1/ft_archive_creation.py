import sys


def ft_ancient_text() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_archive_creation.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            file = open(file_name, "r")
            print("---\n")
            print(file.read(), end="")
            file.close()
            print(f"\n---\nFile '{file_name}' closed.\n")
            ft_archive_creation()
        except Exception as err:
            print(f"Error opening file '{file_name}': {err}\n")


def ft_archive_creation() -> None:
    print("Transform data:")
    print("---\n")
    f = open(sys.argv[1], "r")
    content = f.read()
    f.close()
    lst_lines = content.splitlines()
    lst_lines = [line + "#" for line in lst_lines]
    new_content: str = "\n".join(lst_lines)
    print(new_content)
    new_file = input("\n---\nEnter new file name (or empty): ")
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
            print(f"Error: {err}")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
