import unittest

from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    parse_temperature,
)


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_water_freezes(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_water_boils(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)

    def test_minus_forty_needs_no_conversion(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)


class TestFahrenheitToCelsius(unittest.TestCase):
    def test_water_freezes(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_water_boils(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)


class TestRoundTrip(unittest.TestCase):
    def test_round_trip(self):
        for celsius in (-273.15, -40, 0, 21, 37, 100):
            with self.subTest(celsius=celsius):
                fahrenheit = celsius_to_fahrenheit(celsius)
                self.assertAlmostEqual(fahrenheit_to_celsius(fahrenheit), celsius)


class TestParseTemperature(unittest.TestCase):
    def test_celsius(self):
        self.assertAlmostEqual(parse_temperature("21C"), 21)

    def test_fahrenheit(self):
        self.assertAlmostEqual(parse_temperature("70F"), 21.11111111111111)

    def test_kelvin(self):
        self.assertAlmostEqual(parse_temperature("300K"), 26.85)

    def test_absolute_zero_kelvin(self):
        self.assertAlmostEqual(parse_temperature("0K"), -273.15)

    def test_negative_and_decimal_values(self):
        self.assertAlmostEqual(parse_temperature("-40F"), -40)
        self.assertAlmostEqual(parse_temperature("+21.5c"), 21.5)

    def test_whitespace_and_case_are_ignored(self):
        self.assertAlmostEqual(parse_temperature("  21 c "), 21)

    def test_unparsable_raises_value_error(self):
        for text in ("", "  ", "21", "21X", "C", "21CC", "abc", "2.1.5C", "21 C extra"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_temperature(text)

    def test_non_string_raises_value_error(self):
        for value in (None, 21, 21.0):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_temperature(value)


if __name__ == "__main__":
    unittest.main()
