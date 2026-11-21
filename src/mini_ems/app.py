"""The work the application does; for now it only reports its settings."""

# logging is the standard library module for log messages.
import logging

# Settings is only used here as a type hint for the function argument.
from mini_ems.config import Settings

# One logger per module; __name__ is "mini_ems.app", so log lines show where they came from.
logger = logging.getLogger(__name__)


# Run the application with settings that are already loaded and checked.
def run(settings: Settings) -> None:
    # INFO: normal events that an operator wants to see.
    logger.info("mini_ems started")
    # Values are passed as arguments; logging builds the text only if the line is written.
    logger.info("Site: latitude=%s, longitude=%s", settings.latitude, settings.longitude)
    # DEBUG: details for the developer; hidden unless the level is DEBUG.
    logger.debug("Settings in use: %s", settings)