import unittest           # Leonard Meza IS211
import conversions
from conversions_refactored import convert, ConversionNotPossible


class TestTempConversion(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("\nTesting the convert Celsius To Kelvin function")
        test_cases = [(0, 273.15), (100.0, 373.15), (-273.15, 0), (25.0, 298.15), (300, 573.15),]
        for celsius, expected in test_cases:
            result = conversions.convertCelsiusToKelvin(celsius)
            print(f"Testing function convert Celsius({celsius}) To Kelvin == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("\n---Testing conversions.py...\n-Testing the convert Celsius To Fahrenheit function")
        test_cases = [(0, 32), (100, 212), (-40, -40), (25, 77), (300, 572),]
        for celsius, expected in test_cases:
            result = conversions.convertCelsiusToFahrenheit(celsius)
            print(f"Testing function convert Celsius({celsius}) To Fahrenheit == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        print("\nTesting the convert Fahrenheit to Celsius function")
        test_cases = [(32, 0), (212, 100), (-40, -40), (77, 25), (572, 300),]
        for fahrenheit, expected in test_cases:
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            print(f"Testing function convert Fahrenheit({fahrenheit}) To Celsius == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        print("\nTesting the convert Fahrenheit to Kelvin Function")
        test_cases = [(32, 273.15), (212, 373.15), (-40, 233.15), (77, 298.15), (572, 573.15),]
        for fahrenheit, expected in test_cases:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            print(f"Testing function convert Fahrenheit({fahrenheit}) To Kelvin == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToCelsius(self):
        print("\nTesting the convert Kelvin to Celsius Function")
        test_cases = [(273.15, 0),(373.15, 100.0),(0, -273.15),(298.15, 25),(573.15, 300),]
        for kelvin, expected in test_cases:
            result = conversions.convertKelvinToCelsius(kelvin)
            print(f"Testing function convert Kelvin({kelvin}) To Celsius == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        print("\nTesting the convert Kelvin to Fahrenheit Function")
        test_cases = [(273.15, 32), (373.15, 212), (0, -459.67),(298.15, 77), (573.15, 572)]
        for kelvin, expected in test_cases:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            print(f"Testing function converting Kelvin ({kelvin}) To Fahrenheit == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)


class TestConversionsRefactored(unittest.TestCase):
    def testTempConversion(self):
        print("\nTesting Temperature Conversion Refactoring...")
        # celsius to
        test_cases = [
            ('Celsius', 'Kelvin', 0, 273.15),
            ('Celsius', 'Fahrenheit', 100, 212),
            ('Fahrenheit', 'Celsius', 32, 0),
            ('Fahrenheit', 'Kelvin', -40, 233.15),
            ('Kelvin', 'Celsius', 273.15, 0),
            ('Kelvin', 'Fahrenheit', 373.15, 212),

        ]

        for fromUnit, toUnit, value, expected in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"Convert {fromUnit} to {toUnit}, {value} == {expected}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def testDistanceConversion(self):
        print("\nTesting Distance Conversions Refactoring...")
        test_cases = [
            ('miles', 'meters', 1, 1609.344),
            ('meters', 'yards', 1, 1.09361),
            ('yards', 'miles', 1760, 1),
        ]
        for fromUnit, toUnit, value, expected in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"Convert {fromUnit} to {toUnit}, {value} {fromUnit} should equal {expected} {toUnit}, got {result}")
            self.assertAlmostEqual(result, expected, places=2)



    def testConversiontoSameUnit(self):
        print("\n---Testing conversions_refactored.py \nTesting Same Unit Conversions Refactoring...")
        test_cases = [('Celsius', 'Celsius', 0),
                      ('Fahrenheit', 'Fahrenheit', 32),
                      ('Kelvin', 'Kelvin', 273.5),
                      ('miles', 'miles', 1),
                      ('yards', 'yards', 1760),
                       ('meters', 'meters', 100)
                      ]
        for fromUnit, toUnit, value in test_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"Convert {fromUnit} to {toUnit}, {value} {fromUnit} should equal {value}, got {result}")
            self.assertAlmostEqual(result, value, places=2)



if __name__ == '__main__':
    unittest.main()

