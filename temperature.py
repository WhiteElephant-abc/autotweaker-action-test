"""Temperature conversions between Celsius, Fahrenheit and Kelvin."""

ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert a Celsius temperature to Kelvin."""
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError(f"temperature below absolute zero: {celsius} degrees Celsius")
    return celsius - ABSOLUTE_ZERO_CELSIUS


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert a Kelvin temperature to Celsius."""
    if kelvin < 0:
        raise ValueError(f"temperature below absolute zero: {kelvin} kelvin")
    return kelvin + ABSOLUTE_ZERO_CELSIUS
