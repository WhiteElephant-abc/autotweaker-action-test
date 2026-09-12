"""Temperature conversions."""

ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_KELVIN = 0.0


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert a Celsius temperature to Kelvin.

    Raises ValueError for temperatures below absolute zero.
    """
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError(f"temperature below absolute zero: {celsius} Celsius")
    return celsius - ABSOLUTE_ZERO_CELSIUS


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert a Kelvin temperature to Celsius.

    Raises ValueError for temperatures below absolute zero.
    """
    if kelvin < ABSOLUTE_ZERO_KELVIN:
        raise ValueError(f"temperature below absolute zero: {kelvin} Kelvin")
    return kelvin + ABSOLUTE_ZERO_CELSIUS
