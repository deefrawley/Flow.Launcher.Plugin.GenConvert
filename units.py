"""
Unit Syntax:
units = {
    "Category description": [
        ["abbreviation", 
         "unit name (singular)", 
         "unit name (plural)", 
         "conversion formula TO base unit", 
         "conversion formula FROM base unit"]
    ]
}    

The first entry for each category in the list of lists MUST be the base unit.
"""
units = {
    "Distance": [
        # Base
        ["m", "metre", "metres", "x * 1", "x * 1"],
        # All below convert to/from base
        ["mm", "millimetre", "millimetres", "x / 1000", "x * 1000"],
        ["cm", "centimetre", "centimetres", "x / 100", "x * 100"],
        ["km", "kilometre", "kilometres", "x / 0.001", "x * 0.001"],
        ["in", "inch", "inches", "x / 39.37008", "x * 39.37008"],
        ["ft", "foot", "feet", "x / 3.28084", "x * 3.28084"],
        ["yd", "yard", "yards", "x / 1.093613", "x * 1.093613"],
        ["mi", "mile", "miles", "x / 0.0006213712", "x * 0.0006213712"],
    ],
    "Volume": [
        # NOTE :- Volumes are tricky because America. Non metric units often have a US and Imperial
        # version. The default is US and the Imperial conversion can often be accessed by adding "imp"
        # to the unit code.
        # Base
        ["ml", "millilitre", "millilitres", "x * 1", "x * 1"],
        # All below convert to/from base
        ["gm", "gram", "grams", "x * 1", "x * 1"],
        ["l", "litre", "litres", "x / 0.001", "x * 0.001"],
        ["pt", "pint US", "pints US", "x / 0.002113383", "x * 0.002113383"],
        [
            "ptimp",
            "pint Imperial",
            "pints Imperial",
            "x / 0.001759754",
            "x * 0.001759754",
        ],
        ["qt", "quart US", "quarts US", "x / 0.001056691", "x * 0.001056691"],
        [
            "qtimp",
            "quart Imperial",
            "quarts Imperial",
            "x / 0.000879877",
            "x * 0.000879877",
        ],
        [
            "cup",
            "cup US",
            "cups US",
            "x / 0.0042267528198649",
            "x * 0.0042267528198649",
        ],
        [
            "cupimp",
            "cup Imperial",
            "cups Imperial",
            "x / 0.003519508",
            "x * 0.003519508",
        ],
        [
            "tbsp",
            "tablespoon US",
            "tabelspoons US",
            "x / 0.067628224",
            "x * 0.067628224",
        ],
        [
            "tbspimp",
            "tablespoon Imperial",
            "tabelspoons Imperial",
            "x / 0.05631213",
            "x * 0.05631213",
        ],
        [
            "tsp",
            "teaspoon US",
            "teaspoons US",
            "x / 0.2028846715942",
            "x * 0.2028846715942",
        ],
        [
            "tspimp",
            "teaspoon Imperial",
            "teaspoons Imperial",
            "x / 0.1689364",
            "x * 0.1689364",
        ],
        [
            "gal",
            "gallon US",
            "gallons US",
            "x / 0.0002641727499999601",
            "x * 0.0002641727499999601",
        ],
        [
            "galimp",
            "gallon Imperial",
            "gallons Imperial",
            "x / 0.0002199692",
            "x * 0.0002199692",
        ],
        [
            "floz",
            "fluid ounce US",
            "fluid ounces US",
            "x / 0.03381413",
            "x * 0.03381413",
        ],
        [
            "flozimp",
            "fluid ounce Imperial",
            "fluid ounces Imperial",
            "x / 0.03519508",
            "x * 0.03519508",
        ],
    ],
    "Area": [
        # Base
        ["sqm", "square metre", "square metres", "x * 1", "x * 1"],
        ["h", "hectare", "hectares", "x / 0.0001", "x * 0.0001"],
        ["ac", "acre", "acres", "x / 0.0002471052", "x * 0.0002471052"],
        ["sqcm", "square centimetre", "square centimetres", "x / 10000", "x * 10000"],
        ["sqkm", "square kilometre", "square kilometres", "x / 1000000", "x * 1000000"],
        ["sqin", "square inch", "square inches", "x / 1550.003", "x * 1550.003"],
        [
            "sqmi",
            "square mile",
            "square miles",
            "x / 0.0000003861022",
            "x * 0.0000003861022",
        ],
        ["sqft", "square foot", "square feet", "x / 10.76391", "x * 10.76391"],
        ["sqyd", "square yard", "square yards", "x / 1.19599", "x * 1.19599"],
    ],
    "Weight": [
        # Base
        ["gm", "gram", "grams", "x * 1", "x * 1"],
        # All below convert to/from base
        ["kg", "kilogram", "kilograms", "x / 0.001", "x * 0.001"],
        ["lb", "pound", "pounds", "x / 0.002205", "x * 0.001"],
        ["oz", "ounce", "ounces", "x / 0.035274", " 0.035274"],
        ["st", "stone", "stone", "x / 0.000157473", "x * 0.000157473"],
        ["ton", "ton", "ton", "x / 0.000001102310999995", "x / 0.000001102310999995"],
    ],
    "Temperature": [
        # Base
        ["c", "Celsius", "Celsius", "x * 1", "x * 1"],
        # All below convert to/from base
        ["f", "Farenheit", "Farenheit", "(x - 32) / 1.8", "(x * 1.8) + 32"],
        ["k", "Kelvin", "Kelvin", "x - 273.15", "x + 273.15"],
    ],
}
