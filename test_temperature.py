import unittest

from temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
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


class TestCelsiusToKelvin(unittest.TestCase):
    def test_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)

    def test_water_freezes(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_water_boils(self):
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)

    def test_below_absolute_zero_raises(self):
        with self.assertRaises(ValueError):
            celsius_to_kelvin(-273.16)


class TestKelvinToCelsius(unittest.TestCase):
    def test_absolute_zero(self):
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_water_freezes(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

    def test_water_boils(self):
        self.assertAlmostEqual(kelvin_to_celsius(373.15), 100)

    def test_below_absolute_zero_raises(self):
        with self.assertRaises(ValueError):
            kelvin_to_celsius(-0.01)


class TestRoundTrip(unittest.TestCase):
    def test_round_trip(self):
        for celsius in (-273.15, -40, 0, 21, 37, 100):
            with self.subTest(celsius=celsius):
                fahrenheit = celsius_to_fahrenheit(celsius)
                self.assertAlmostEqual(fahrenheit_to_celsius(fahrenheit), celsius)

    def test_kelvin_round_trip(self):
        for celsius in (-273.15, -40, 0, 21, 37, 100):
            with self.subTest(celsius=celsius):
                kelvin = celsius_to_kelvin(celsius)
                self.assertAlmostEqual(kelvin_to_celsius(kelvin), celsius)


if __name__ == "__main__":
    unittest.main()
