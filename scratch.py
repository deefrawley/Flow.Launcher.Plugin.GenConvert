from plugin.settings import __package_title__, __version__

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
        "l": 0.001,
        "pt": 0.002113383,
        "qt": 0.001056691,
        "cup": 0.004226764,
        "tbsp": 0.067628224,
        "tsp": 0.2028846715942,
        "gal": 0.0002641727499999601,
    },
}


def genConvert(amount, from_unit, to_unit):
    conversions = {}
    if from_unit == to_unit:
        conversions["Error"] = "To and from unit is the same"
        return conversions
    # Convert from key unit to sub-unit (e.g. cm to in)gc 1 km mi
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
                    key_convert = ((1 / units[u][from_unit]) * amount) * 10
                    key_sub = units[u][to_unit] * key_convert
                    print(f"key_convert {amount} {from_unit} = {key_convert}")
                    print(f"key_sub = {key_sub}")

                    conversions[to_unit] = (1 / units[u][from_unit]) * (
                        units[u][to_unit] * amount
                    )
                    return conversions
        if not to_sub or not from_sub:
            conversions["Error"] = "Unit not found"
            return conversions


def listUnits():
    # Utility function to print out all conversions
    print(f"{__package_title__} v{__version__} Units")
    print("==============================")
    for all_units in units.keys():
        print(f"\n{all_units}, ", end="")
        for all_to_units in units[all_units].keys():
            print(f"{all_to_units}, ", end="")


""" result = input(" > ")
q = result.strip()
args = q.split(" ")
result2 = genConvert(float(args[1]), args[2], args[3])
if "Error" in result2:
    print(f"Error - {result2['Error']}")
else:
    print(f"{args[1]} {args[2]} = {result2[args[3]]:.6f} {args[3]}") """

listUnits()