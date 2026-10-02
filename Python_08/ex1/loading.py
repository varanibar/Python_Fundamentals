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


def is_installed(module: str, function: str) -> None:
    try:
        import_module(module)
        version = metadata.version(module)
        print(f"[OK] {module} ({version}) - {function}")
    except ImportError:
        print(f"[KO] {module} is NOT installed")

def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    for (module, description) in dependencies.items():
        is_installed(module, description)


if __name__ == "__main__":
    main()
