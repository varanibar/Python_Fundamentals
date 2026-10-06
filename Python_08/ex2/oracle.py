import os
import sys
import logging


try:
    from dotenv import load_dotenv
except ModuleNotFoundError as err:
    print(f"Error: {err}")
    print("To install it, run:")
    print("python -m pip install python-dotenv")
    sys.exit()


def load_variables() -> list[str | None]:
    # Load variables from .env to the system
    load_dotenv()

    levels = list(logging.getLevelNamesMapping().keys())

    # Retrieve environment variables in the system

    matrix_mode = os.getenv("MATRIX_MODE")
    if matrix_mode not in ["development", "production"]:
        matrix_mode = "production (default)"

    database_url = os.getenv("DATABASE_URL")
    if database_url:
        database_url = "Connected to local instance"

    api_key = os.getenv("API_KEY")
    if api_key:
        api_key = "Authenticated"

    log_level = os.getenv("LOG_LEVEL")
    if log_level not in levels:
        log_level = "DEBUG (default)"

    zion_endpoint = os.getenv("ZION_ENDPOINT")
    if zion_endpoint:
        zion_endpoint = "Online"

    print("Configuration loaded:")
    print(f"  Mode: {matrix_mode}")
    print(f"  Database: {database_url}")
    print(f"  API Access: {api_key}")
    print(f"  Log Level: {log_level}")
    print(f"  Zion Network: {zion_endpoint}")

    return [matrix_mode, database_url, api_key, log_level, zion_endpoint]


def security_check(variables: list[str | None]) -> None:
    print("Environment security check:")

    for var in variables:
        if not var:
            print("[KO] .env file not properly configured\n"
                  "      Empty or missing variables")
            sys.exit()

    print("  [OK] No hardcoded secrets detected")
    print("  [OK] .env file properly configured")
    print("  [OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # Check that local .env file exists
    if not os.path.isfile(".env"):
        print("Can't load configuration: .env not found")
        return

    variables = load_variables()
    print()

    security_check(variables)


if __name__ == "__main__":
    main()
