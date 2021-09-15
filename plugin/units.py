from plugin.extensions import _

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
        # All below convert to/from base
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
        ["gm", _("gram"), _("grams"), "x * 1", "x * 1"],
        ["l", _("litre"), _("litres"), "x / 0.001", "x * 0.001"],
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
        ["gm", _("gram"), _("grams"), "x * 1", "x * 1"],
        # All below convert to/from base
        ["kg", _("kilogram"), _("kilograms"), "x / 0.001", "x * 0.001"],
        ["lb", _("pound"), _("pounds"), "x / 0.002205", "x * 0.002205"],
        ["oz", _("ounce"), _("ounces"), "x / 0.035274", " 0.035274"],
        ["st", _("stone"), _("stone"), "x / 0.000157473", "x * 0.000157473"],
        [
            "ton",
            _("ton"),
            _("ton"),
            "x / 0.000001102310999995",
            "x * 0.000001102310999995",
        ],
    ],
    "Temperature": [
        # Base
        ["c", _("Celsius"), _("Celsius"), "x * 1", "x * 1"],
        # All below convert to/from base
        ["f", _("Farenheit"), _("Farenheit"), "(x - 32) / 1.8", "(x * 1.8) + 32"],
        ["k", _("Kelvin"), _("Kelvin"), "x - 273.15", "x + 273.15"],
    ],
}
