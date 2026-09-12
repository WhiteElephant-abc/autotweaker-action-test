"""Temperature conversions.

Temperatures are represented in Celsius unless stated otherwise.
"""

import re

ABSOLUTE_ZERO_CELSIUS = -273.15

_TEMPERATURE_PATTERN = re.compile(r"\A([+-]?\d+(?:\.\d+)?)\s*([CFK])\Z", re.IGNORECASE)


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert a Kelvin temperature to Celsius."""
    return kelvin + ABSOLUTE_ZERO_CELSIUS


def parse_temperature(text: str) -> float:
    """Parse a temperature string such as ``"21C"``, ``"70F"`` or ``"300K"``.

    The unit is case insensitive and surrounding whitespace is ignored. The
    result is always expressed in Celsius. A ``ValueError`` is raised when the
    string is not a temperature with a known unit.
    """
    match = _TEMPERATURE_PATTERN.match(text.strip()) if isinstance(text, str) else None
    if match is None:
        raise ValueError(f"not a temperature: {text!r}")

    value = float(match.group(1))
    unit = match.group(2).upper()
    if unit == "C":
        return value
    if unit == "F":
        return fahrenheit_to_celsius(value)
    return kelvin_to_celsius(value)
