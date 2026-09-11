import unittest

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


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


if __name__ == "__main__":
    unittest.main()
