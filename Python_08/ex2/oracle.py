import os
import sys


try:
    from dotenv import load_dotenv
except ModuleNotFoundError as err:
    print(f"Error: {err}")
    print("To install it run:")
    print("python -m pip install python-dotenv")
    sys.exit()

def load_variables() -> list[str | None]:

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")

    return [matrix_mode, database_url, api_key, log_level, zion_endpoint]

def security_check(variables: list[str, None]) -> None:
    print("Environment security check:")
    for var in variables:
        if not var:
            print("[KO] .env file not properly configured, missing values")
            return


def main() -> None:

    print("\nORACLE STATUS: Reading the Matrix...\n")

    if not load_dotenv():
        print("Can't load configuration: No .env file found")
        return

    variables = load_variables()
    print()

    security_check(variables)


if __name__=="__main__":
    main()
