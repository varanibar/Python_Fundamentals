import sys
from importlib import import_module, metadata


dependencies = {"pandas":"Data manipulation ready",
        "numpy":"Numerical computation ready",
        "requests":"Network access ready",
        "matplotlib":"Visualization ready"
        }


# modules = ["pandas",
#         "numpy",
#         "requests",
#         "matplotlib"
#         ]


def is_installed(module: str) -> None:
    try:
        import_module(module)
        return True
    except ImportError:
        return False

def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    missing_packages = False
    for (module, description) in dependencies.items():
        if is_installed(module):
            version = metadata.version(module)
            print(f"[OK] {module} ({version}) - {description}")
        else:
            print(f"[MISSING] {module} is NOT installed")
            missing_packages = True

    if missing_packages:
        print(
            "\n\nMissing dependencies:\n"
            "Use pip or poetry to install the missing dependencies.\n"
            "\nUsing pip:\n"
            " -To install a single package, use:\n"
            "    python -m pip install <package>\n"
            " -To install multiple packages with a text file, use:\n"
            "    python -m pip install -r <requirements file>\n"
            "\nUsing poetry:\n"
            " -To install all dependencies defined in pyproject.toml, use:\n"
            "    poetry install\n"
            )

    else:
        print("\n\nAnalyzing Matrix data...")



if __name__ == "__main__":
    main()
