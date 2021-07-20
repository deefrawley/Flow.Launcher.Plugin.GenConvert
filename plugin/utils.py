from plugin.extensions import _

units = {
    "m": {
        "mm": 1000,
        "cm": 100,
        "km": 0.001,
        "in": 39.37008,
        "ft": 3.28084,
        "yd": 1.093613,
        "mi": 0.0006213712,
    },
    "ml": {
        "gm": 1,
        "l": 0.001,
        "pt": 0.002113383,
        "qt": 0.001056691,
        "cup": 0.004226764,
        "tbsp": 0.067628224,
        "tsp": 0.2028846715942,
        "gal": 0.0002641727499999601,
    },
    "sqm": {
        "h": 0.0001,
        "ac": 0.0002471052,
        "sqcm": 10000,
        "sqkm": 1000000,
        "sqin": 1550.003,
        "sqmi": 0.0000003861022,
        "sqft": 10.76391,
        "sqyd": 1.19599,
    },
    "gm": {
        "kg": 0.001,
        "lb": 0.002205,
        "oz": 0.035274,
        "st": 0.000157473,
        "ton": 0.000001102310999995,
    },
    # Special case temp C to F - actually handled in code
    "c": {
        "f": 1.8,
    },
}


def genConvert(amount, from_unit, to_unit):
    conversions = {}
    if from_unit == to_unit:
        conversions["Error"] = _("To and from unit is the same")
        return conversions
    # Handle celsius and farenheit as special cases as they aren't converted by exponents
    elif from_unit == "c" and to_unit == "f":
        conversions[to_unit] = (amount * 1.8) + 32
        return conversions
    elif from_unit == "f" and to_unit == "c":
        conversions[to_unit] = (amount - 32) / 1.8
        return conversions
    # Convert from key unit to sub-unit (e.g. cm to in)
    elif from_unit in units and to_unit in units[from_unit]:
        conversions[to_unit] = units[from_unit][to_unit] * amount
        return conversions
    # Convert from sub-unit to key unit (e.g. in to cm)
    elif to_unit in units and from_unit in units[to_unit]:
        conversions[to_unit] = (1 / units[to_unit][from_unit]) * amount
        return conversions
    # Convert from sub-unit to sub-unit (e.g. in to ft)
    else:
        for u in units:
            to_sub = False
            from_sub = False
            for u2 in units[u]:
                if u2 == to_unit:
                    to_sub = True
                elif u2 == from_unit:
                    from_sub = True
                if to_sub and from_sub:
                    # Convert via the key unit
                    conversions[to_unit] = (1 / units[u][from_unit]) * (
                        units[u][to_unit] * amount
                    )
                    return conversions
        conversions["Error"] = _("Problem converting {} and {}").format(
            from_unit, to_unit
        )
        return conversions


def listUnits():
    # Utility function to print out all conversions
    for all_units in units.keys():
        print(f"\n{all_units}, ", end="")
        for all_to_units in units[all_units].keys():
            print(f"{all_to_units}, ", end="")
