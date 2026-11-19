"""Read the application settings from environment variables."""

# os gives access to the environment variables of this process.
import os

# dataclass builds a small class that only holds data.
from dataclasses import dataclass


# The level names that the logging module accepts (used in Bit 4).
_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


# Error type for a missing or bad setting, so main() can catch it by name.
class ConfigError(Exception):
    """A setting is missing or has a bad value."""


# frozen=True: the settings cannot be changed after they are loaded.
@dataclass(frozen=True)
class Settings:
    # Log level name, for example "INFO".
    log_level: str
    # Site latitude in degrees; north is positive.
    latitude: float
    # Site longitude in degrees; east is positive.
    longitude: float


# Read one variable, convert it to float, and check that it is in a range.
def _read_float(name: str, default: str, low: float, high: float) -> float:
    # Take the text from the environment, or the default text if it is not set.
    raw = os.environ.get(name, default)
    # Try to convert the text to a number.
    try:
        # float() also accepts spaces around the number, like " 43.26 ".
        value = float(raw)
    # float() raises ValueError for text like "43,26" or "abc".
    except ValueError:
        # Replace it with a clear message; "from None" hides the internal traceback.
        raise ConfigError(f"{name} must be a number, got {raw!r}") from None
    # Check the range; this also rejects "nan" and "inf".
    if not low <= value <= high:
        # Stop with a message that names the variable and the allowed range.
        raise ConfigError(f"{name} must be between {low} and {high}, got {value}")
    # Return the checked number.
    return value


# Build the Settings object once, at startup.
def load_settings() -> Settings:
    # Read the log level, remove spaces, and accept "debug" as well as "DEBUG".
    level = os.environ.get("MINI_EMS_LOG_LEVEL", "INFO").strip().upper()
    # Reject names the logging module does not know.
    if level not in _LOG_LEVELS:
        # List the allowed names in a fixed order in the message.
        raise ConfigError(
            f"MINI_EMS_LOG_LEVEL must be one of {sorted(_LOG_LEVELS)}, got {level!r}"
        )
    # Create and return the settings; each float is read and checked here.
    return Settings(
        # The checked log level.
        log_level=level,
        # Latitude must be between -90 and 90.
        latitude=_read_float("MINI_EMS_LATITUDE", "43.26", -90.0, 90.0),
        # Longitude must be between -180 and 180.
        longitude=_read_float("MINI_EMS_LONGITUDE", "-2.93", -180.0, 180.0),
    )