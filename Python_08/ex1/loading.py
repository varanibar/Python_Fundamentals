import sys
from importlib import import_module, metadata

try:
    import pandas  # type: ignore
except ModuleNotFoundError:
    pass

try:
    import numpy  # type: ignore
except ModuleNotFoundError:
    pass

try:
    import requests  # type: ignore
except ModuleNotFoundError:
    pass

try:
    import matplotlib  # type: ignore
    import matplotlib.pyplot  # type: ignore
except ModuleNotFoundError:
    pass


dependencies = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
    }


def environment_check() -> None:
    if sys.prefix == sys.base_prefix:
        print("Curently working in a global environment")
    elif "pypoetry" in sys.prefix:
        print("Currently in a poetry environment")
    else:
        print("curently in a virtual environment")


def is_installed(module: str) -> bool:
    try:
        import_module(module)
        return True
    except ImportError:
        return False


def dependecy_check() -> bool:
    missing_packages = False
    for (module, description) in dependencies.items():
        if is_installed(module):
            version = metadata.version(module)
            print(f"[OK] {module} ({version}) - {description}")
        else:
            print(f"[MISSING] {module} is NOT installed")
            missing_packages = True

    return missing_packages


def matrix_analysis() -> None:
    print("\nChecking dataset access with 'requests'...")

    metadata_url = (
        "https://ourworldindata.org/grapher/"
        "annual-area-burnt-by-wildfires.metadata.json"
    )

    try:
        response = requests.get(metadata_url, timeout=10)
        response.raise_for_status()
        print(" Dataset request status: Request succesful")

    except requests.exceptions.RequestException as err:
        print(f" Request failed: {err}")
        return

    print("\nReading data directly from the online CSV with 'pandas'...")
    url = (
        "https://ourworldindata.org/grapher/"
        "annual-area-burnt-by-wildfires.csv"
        "?v=1&csvType=full&useColumnShortNames=false"
        )
    try:
        dataframe = pandas.read_csv(
            url,
            storage_options={
                "User-Agent": "Our World In Data data fetch/1.0"
            }
            )

    except Exception as err:
        print(f" Request failed: {err}")
        return

    print(" Collecting data from: Bolivia")
    bolivia_data = dataframe[dataframe["Entity"] == "Bolivia"]
    print(f" Data points collected: {len(bolivia_data)} ", end="")
    print(f"({bolivia_data["Year"].min()} to {bolivia_data["Year"].max()})")

    print("\nCalculating the average burned area with 'numpy'...")
    average = numpy.mean(bolivia_data["Annual area burnt by wildfires"])
    print(f" Average area burned (per year): {average:.0f} hectares")

    print("\nPlotting data with 'matplotlib'...")
    print(" Results saved to: bolivia_wildfires.jpg")
    matplotlib.pyplot.plot(
                        bolivia_data["Year"],
                        bolivia_data["Annual area burnt by wildfires"]
                        )
    matplotlib.pyplot.xlabel("Year")
    matplotlib.pyplot.ylabel("Area burned (hectares)")
    matplotlib.pyplot.title("Wildfire area burned in Bolivia")
    matplotlib.pyplot.savefig("bolivia_wildfires.jpg")

    print("\nAnalysis complete!")


def main() -> None:
    print("\nChecking current environment...")
    print("\nENVIRONMENT STATUS: ", end="")
    environment_check()

    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    missing_packages: bool = dependecy_check()

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
        matrix_analysis()


if __name__ == "__main__":
    main()
