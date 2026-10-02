import sys
import os
import site


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    venv_path = sys.prefix
    curr_python = sys.executable
    for path in site.getsitepackages():
        if path.startswith(venv_path):
            packages_path = path

    if in_venv:
        status = "Welcome to the construct"
        venv_name = os.path.basename(venv_path)
        message = (
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting the global system."
            )
    else:
        status = "You're still plugged in"
        venv_name = "None detected"
        message = (
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            "\nTo enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
            )

    print(f"\nMATRIX STATUS: {status}\n")
    print(f"Current Python: {curr_python}")
    print(f"Virtual environment: {venv_name}")

    if in_venv:
        print(f"Environment Path: {venv_path}")
        print(message)
        print(f"\nPackage installation path: \n{packages_path}")
    else:
        print(message)


if __name__ == "__main__":
    main()
