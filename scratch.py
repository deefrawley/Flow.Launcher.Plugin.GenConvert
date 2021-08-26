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
        "floz": 0.03381413,
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


def get_hints(from_unit):
    """ Takes an input unit and returns a list of units it can be converted to """
    for u in units:
        if u == from_unit:
            return [x for x in units[from_unit].keys()]
        for u2 in units[u]:
            if u2 == from_unit:
                c = [x for x in units[u].keys() if x != from_unit]
                c.append(u)
                return c
    return ["no valid units"]


vv = get_hints("ox")
print(vv)