# Entry point: Python runs this file when you type "python -m mini_ems".

# Import the settings loader and its error type from the config module.
from mini_ems.config import ConfigError, load_settings


# Start the application.
def main() -> None:
    # Load and check all settings before doing any work.
    try:
        # Read the environment once; the result is passed on, never read again.
        settings = load_settings()
    # A bad setting: stop here with a short message instead of a long traceback.
    except ConfigError as error:
        # SystemExit with a text prints it to stderr and ends with exit code 1.
        raise SystemExit(f"Config error: {error}") from None
    # Temporary start message; Bit 4 replaces print() with logging.
    print("mini_ems started")
    # Show the settings in use; a frozen dataclass prints all its fields.
    print(settings)


# Run main() only when this file is executed, not when it is imported.
if __name__ == "__main__":
    # Call the start function.
    main()