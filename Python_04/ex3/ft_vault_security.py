#!/usr/bin/env python3

def secure_archive(
        file: str,
        action: str,
        new_content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file) as f:
                content = f.read()
                return (True, content)
        elif action == "w":
            with open(file, action) as f:
                f.write(new_content)
                return (True, "Content successfully written to file")
    except Exception as err:
        return (False, f"{err}")
    return (False, f"Unknown action '{action}'. Expected 'w' or 'r'.")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    non_existent_file = secure_archive("/not/existing/file", "r")
    print(non_existent_file)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    inaccessible_file = secure_archive(
        "/home/varaniba/CODAM_CORE/Python/Python_04/etc/master.passwd",
        "r")
    print(inaccessible_file)

    print("\nUsing 'secure_archive' to read from a regular file:")
    regular_file = secure_archive(
        "/home/varaniba/CODAM_CORE/Python/Python_04/etc/ancient_fragment.txt",
        "r")
    print(regular_file)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    write_to_new_file = secure_archive("new_file.txt", "w", regular_file[1])
    print(write_to_new_file)


if __name__ == "__main__":
    main()
