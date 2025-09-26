from translation import _

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
Descriptions wrapped in '_()' can, and should, be translated via the Python template
translation methods
"""
units = {
    _("Distance"): [
        # Base
        ["m", _("metre"), _("metres"), "x * 1", "x * 1"],
        # All below convert to / from base
        ["dm", _("decimetre"), _("decimetres"), "x / 10", "x * 10"],
        ["mm", _("millimetre"), _("millimetres"), "x / 1000", "x * 1000"],
        ["cm", _("centimetre"), _("centimetres"), "x / 100", "x * 100"],
        ["km", _("kilometre"), _("kilometres"), "x / 0.001", "x * 0.001"],
        ["in", _("inch"), _("inches"), "x / 39.37008", "x * 39.37008"],
        ["ft", _("foot"), _("feet"), "x / 3.28084", "x * 3.28084"],
        ["yd", _("yard"), _("yards"), "x / 1.093613", "x * 1.093613"],
        ["mi", _("mile"), _("miles"), "x / 0.0006213712", "x * 0.0006213712"],
    ],
    _("Volume"): [
        # NOTE :- Volumes are tricky because America. Non metric units often have a US and Imperial
        # version. The default is US and the Imperial conversion can often be accessed by adding "imp"
        # to the unit code.
        # Base
        ["ml", _("millilitre"), _("millilitres"), "x * 1", "x * 1"],
        # All below convert to/from base
        ["g", _("gram"), _("grams"), "x * 1", "x * 1"],
        ["l", _("litre"), _("litres"), "x / 0.001", "x * 0.001"],
        ["decal", _("decalitre"), _("decalitres"), "x / 0.0001", "x * 0.0001"],
        ["pt", _("pint US"), _("pints US"), "x / 0.002113383", "x * 0.002113383"],
        [
            "ptimp",
            _("pint Imperial"),
            _("pints Imperial"),
            "x / 0.001759754",
            "x * 0.001759754",
        ],
        ["qt", _("quart US"), _("quarts US"), "x / 0.001056691", "x * 0.001056691"],
        [
            "qtimp",
            _("quart Imperial"),
            _("quarts Imperial"),
            "x / 0.000879877",
            "x * 0.000879877",
        ],
        [
            "cup",
            _("cup US"),
            _("cups US"),
            "x / 0.0042267528198649",
            "x * 0.0042267528198649",
        ],
        [
            "cupimp",
            _("cup Imperial"),
            _("cups Imperial"),
            "x / 0.003519508",
            "x * 0.003519508",
        ],
        [
            "tbsp",
            _("tablespoon US"),
            _("tabelspoons US"),
            "x / 0.067628224",
            "x * 0.067628224",
        ],
        [
            "tbspimp",
            _("tablespoon Imperial"),
            _("tabelspoons Imperial"),
            "x / 0.05631213",
            "x * 0.05631213",
        ],
        [
            "tsp",
            _("teaspoon US"),
            _("teaspoons US"),
            "x / 0.2028846715942",
            "x * 0.2028846715942",
        ],
        [
            "tspimp",
            _("teaspoon Imperial"),
            _("teaspoons Imperial"),
            "x / 0.1689364",
            "x * 0.1689364",
        ],
        [
            "gal",
            _("gallon US"),
            _("gallons US"),
            "x / 0.0002641727499999601",
            "x * 0.0002641727499999601",
        ],
        [
            "galimp",
            _("gallon Imperial"),
            _("gallons Imperial"),
            "x / 0.0002199692",
            "x * 0.0002199692",
        ],
        [
            "floz",
            _("fluid ounce US"),
            _("fluid ounces US"),
            "x / 0.03381413",
            "x * 0.03381413",
        ],
        [
            "flozimp",
            _("fluid ounce Imperial"),
            _("fluid ounces Imperial"),
            "x / 0.03519508",
            "x * 0.03519508",
        ],
        [
            "dm3",
            _("cubic decimetre"),
            _("cubic decimetres"),
            "x / 0.001",
            "x * 0.001",
        ],
        [
            "mm3",
            _("cubic millimetre"),
            _("cubic millimetres"),
            "x / 0.1000",
            "x * 0.1000",
        ],
        [
            "cm3",
            _("cubic centimetre"),
            _("cubic centimetres"),
            "x / 1",
            "x * 1",
        ],
        [
            "m3",
            _("cubic metre"),
            _("cubic metres"),
            "x / 0.000001",
            "x * 0.000001",
        ],
        [
            "in3",
            _("cubic inch"),
            _("cubic inches"),
            "x / 0.061024",
            "x * 0.061024",
        ],
        [
            "ft3",
            _("cubic feet"),
            _("cubic feet"),
            "x / 0.0000353147",
            "x * 0.0000353147",
        ],
        [
            "buuk",
            _("bushel UK"),
            _("bushels UK"),
            "x / 0.0000274961",
            "x * 0.0000274961",
        ],
        [
            "buus",
            _("bushel US"),
            _("bushels US"),
            "x / 0.0000283776",
            "x * 0.0000283776",
        ],
    ],
    "Area": [
        # Base
        ["sqm", _("square metre"), _("square metres"), "x * 1", "x * 1"],
        ["h", _("hectare"), _("hectares"), "x / 0.0001", "x * 0.0001"],
        ["ac", _("acre"), _("acres"), "x / 0.0002471052", "x * 0.0002471052"],
        [
            "sqcm",
            _("square centimetre"),
            _("square centimetres"),
            "x / 10000",
            "x * 10000",
        ],
        [
            "sqkm",
            _("square kilometre"),
            _("square kilometres"),
            "x / 1000000",
            "x * 1000000",
        ],
        ["sqin", _("square inch"), _("square inches"), "x / 1550.003", "x * 1550.003"],
        [
            "sqmi",
            _("square mile"),
            _("square miles"),
            "x / 0.0000003861022",
            "x * 0.0000003861022",
        ],
        ["sqft", _("square foot"), _("square feet"), "x / 10.76391", "x * 10.76391"],
        ["sqyd", _("square yard"), _("square yards"), "x / 1.19599", "x * 1.19599"],
    ],
    "Weight": [
        # Base
        ["g", _("gram"), _("grams"), "x * 1", "x * 1"],
        # All below convert to/from base
        ["kg", _("kilogram"), _("kilograms"), "x / 0.001", "x * 0.001"],
        ["lb", _("pound"), _("pounds"), "x / 0.002205", "x * 0.002205"],
        ["oz", _("ounce"), _("ounces"), "x / 0.035274", "x * 0.035274"],
        ["st", _("stone"), _("stone"), "x / 0.000157473", "x * 0.000157473"],
        [
            "t",
            _("tonne"),
            _("tonnes"),
            "x / 0.000001",
            "x * 0.000001",
        ],
        [
            "ton",
            _("US ton"),
            _("US tons"),
            "x / 0.0000011023109950010196",
            "x * 0.0000011023109950010196",
        ],
        [
            "tonimp",
            _("Imperial ton"),
            _("Imperial tons"),
            "x / 0.00000098421",
            "x * 0.00000098421",
        ],
    ],
    "Temperature": [
        # Base
        ["c", _("Celsius"), _("Celsius"), "x * 1", "x * 1"],
        # All below convert to/from base
        ["f", _("Farenheit"), _("Farenheit"), "(x - 32) / 1.8", "(x * 1.8) + 32"],
        ["k", _("Kelvin"), _("Kelvin"), "x - 273.15", "x + 273.15"],
    ],
    "Speed": [
        # Base
        ["km/h", _("kilometres per hour"), _("kilometres per hour"), "x * 1", "x * 1"],
        [
            "m/s",
            _("metres per second"),
            _("metres per second"),
            "x / 0.2777777778",
            "x * 0.2777777778",
        ],
        [
            "mp/h",
            _("miles per hour"),
            _("miles per hour"),
            "x / 0.6213711922",
            "x * 0.6213711922",
        ],
        [
            "kt",
            _("knot"),
            _("knots"),
            "x / 0.5399568035",
            "x * 0.5399568035",
        ],
    ],
    "Energy": [
        # Base
        ["J", _("joule"), _("joules"), "x * 1", "x * 1"],
        [
            "cal",
            _("calorie"),
            _("calories"),
            "x / 0.2388459",
            "x * 0.2388459",
        ],
        [
            "kcal",
            _("kilocalorie"),
            _("kilocalories"),
            "x / 0.0002388459",
            "x * 0.0002388459",
        ],
        [
            "kJ",
            _("kilojoule"),
            _("kilojoules"),
            "x / 0.001",
            "x * 0.001",
        ],
        [
            "MJ",
            _("megajoule"),
            _("megajoules"),
            "x / 0.000001",
            "x * 0.000001",
        ],
        [
            "Gj",
            _("gigajoule"),
            _("gigajoules"),
            "x / 0.0000000010",
            "x * 0.0000000010",
        ],
        [
            "kWh",
            _("kilowatt hour"),
            _("kilowatt hours"),
            "x / 0.0000002778",
            "x * 0.0000002778",
        ],
        [
            "BTU",
            _("British thermal unit"),
            _("British thermal units"),
            "x / 0.0009478171",
            "x * 0.0009478171",
        ],
    ],
    "data": [
        # byte is the base
        ["B", _("byte"), _("bytes"), "x * 1", "x * 1"],
        ["KB", _("kilobyte"), _("kilobytes"), "x / 0.001", "x * 0.001"],  # 10^3,
        ["MB", _("megabyte"), _("megabytes"), "x / 0.000001", "x * 0.000001"],  # 10^6,
        [
            "GB",
            _("gigabyte"),
            _("gigabytes"),
            "x / 0.000000001",
            "x * 0.000000001",
        ],  # 10^9,
        [
            "TB",
            _("terabyte"),
            _("terabytes"),
            "x / 0.000000000001",
            "x * 0.000000000001",
        ],  # 10^12,
        [
            "PB",
            _("petabyte"),
            _("petabytes"),
            "x / 0.000000000000001",
            "x * 0.000000000000001",
        ],  # 10^15,
    ],
}
