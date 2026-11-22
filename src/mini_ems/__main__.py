# Entry point: Python runs this file when you type "python -m mini_ems".

# logging is configured here, and only here.
import logging

# sys.stdout is the standard output stream that Docker will collect.
import sys

# run() does the work; this file only connects config, logging and run().
from mini_ems.app import run

# Import the settings loader and its error type.
from mini_ems.config import ConfigError, load_settings

# Line format: time, level (padded to 8 characters), logger name, message.
LOG_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"


# Start the application.
def main() -> None:
    # Load the settings first, because the log level is one of them.
    try:
        # Read and check the environment once.
        settings = load_settings()
    # A bad setting: logging is not set up yet, so stop with a plain message.
    except ConfigError as error:
        # Prints the text to stderr and ends with exit code 1.
        raise SystemExit(f"Config error: {error}") from None
    # Set up logging once: level from the config, our format, output to stdout.
    logging.basicConfig(level=settings.log_level, format=LOG_FORMAT, stream=sys.stdout)
    # Hand over to the application code.
    run(settings)


# Run main() only when this file is executed, not when it is imported.
if __name__ == "__main__":
    # Call the start function.
    main()