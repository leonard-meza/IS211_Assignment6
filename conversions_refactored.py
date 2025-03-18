class ConversionNotPossible(Exception):                  # Leonard Meza IS211
    pass

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit == toUnit:
        return value

    temperatureUnits = {"celsius", "fahrenheit", "kelvin"}
    distanceUnits = {"miles", "yards", "meters"}


    # fromUnit to kelvin
    if fromUnit in temperatureUnits and toUnit in temperatureUnits:
        if fromUnit == "celsius":
            startValue = value + 273.15
        elif fromUnit == "fahrenheit":
            startValue = (value - 32) * 5 / 9.0 + 273.15
        elif fromUnit == "kelvin":
            startValue = value
        else:
            raise ConversionNotPossible(f"Unrecognized temperature unit: {fromUnit}")
        # kelvin to toUnit
        if toUnit == "celsius":
            return startValue - 273.15
        elif toUnit == "fahrenheit":
            return (startValue - 273.15) * 9.0 / 5.0 + 32
        elif toUnit == "kelvin":
            return startValue
        else:
            raise ConversionNotPossible(f"Unrecognized temperature unit: {toUnit}")
    # distance
    elif fromUnit in distanceUnits and toUnit in distanceUnits:
        if fromUnit == "miles":
            startValue = value * 1609.344
        elif fromUnit == "yards":
            startValue = value * 0.9144
        elif fromUnit == "meters":
            startValue = value
        else:
            raise ConversionNotPossible(f"Unrecognized distance Unit: {fromUnit}")

        if toUnit == "miles":
            return startValue / 1609.344
        elif toUnit == "yards":
            return startValue / 0.9144
        elif toUnit == "meters":
            return startValue
        else:
            raise ConversionNotPossible(f"Unrecognized distance unit: {toUnit}")
    else:
        raise ConversionNotPossible(f"Cannot convert from '{fromUnit}' to '{toUnit}'.")

