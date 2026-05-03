from translation import _

# ---------------------------------------------------------------------------
# Unit definitions
# ---------------------------------------------------------------------------
# Format — linear units (4 fields):
#   (abbr, singular, plural, factor)
#   factor = how many base units is 1 of this unit
#   to_base   = value * factor
#   from_base = value / factor
#
# Format — affine units (5 fields, e.g. Temperature):
#   (abbr, singular, plural, factor, offset)
#   to_base   = (value + offset) * factor
#   from_base = (value / factor) - offset
#
# The first entry in each "units" list is the base unit (factor=1).
# ---------------------------------------------------------------------------

units = {
    _("Distance"): {
        "base": "m",
        "units": [
            ("m",   _("metre"),              _("metres"),              1),
            ("dm",  _("decimetre"),          _("decimetres"),          0.1),
            ("cm",  _("centimetre"),         _("centimetres"),         0.01),
            ("mm",  _("millimetre"),         _("millimetres"),         0.001),
            ("µm",  _("micrometre"),         _("micrometres"),         1e-6),
            ("nm",  _("nanometre"),          _("nanometres"),          1e-9),
            ("km",  _("kilometre"),          _("kilometres"),          1_000),
            ("in",  _("inch"),               _("inches"),              0.0254),       # exact
            ("ft",  _("foot"),               _("feet"),                0.3048),       # exact
            ("yd",  _("yard"),               _("yards"),               0.9144),       # exact
            ("mi",  _("mile"),               _("miles"),               1_609.344),    # exact
            ("nmi", _("nautical mile"),      _("nautical miles"),      1_852),        # exact
            ("ly",  _("light-year"),         _("light-years"),         9.4607304725808e15),
            ("au",  _("astronomical unit"),  _("astronomical units"),  1.495978707e11), # exact IAU
            ("pc",  _("parsec"),             _("parsecs"),             3.085677581e16),
            ("Å",   _("ångström"),           _("ångströms"),           1e-10),
        ]
    },

    _("Area"): {
        "base": "sqm",
        "units": [
            ("sqm",  _("square metre"),      _("square metres"),       1),
            ("sqcm", _("square centimetre"), _("square centimetres"),  1e-4),
            ("sqmm", _("square millimetre"), _("square millimetres"),  1e-6),
            ("sqkm", _("square kilometre"),  _("square kilometres"),   1e6),
            ("sqin", _("square inch"),       _("square inches"),       6.4516e-4),    # exact
            ("sqft", _("square foot"),       _("square feet"),         0.09290304),   # exact
            ("sqyd", _("square yard"),       _("square yards"),        0.83612736),   # exact
            ("sqmi", _("square mile"),       _("square miles"),        2_589_988.110336),
            ("ac",   _("acre"),              _("acres"),               4_046.8564224),
            ("h",    _("hectare"),           _("hectares"),            10_000),
        ]
    },

    _("Volume"): {
        # Imperial "imp" suffix convention for non-US variants
        "base": "ml",
        "units": [
            ("ml",      _("millilitre"),          _("millilitres"),          1),
            ("cl",      _("centilitre"),          _("centilitres"),          10),
            ("dl",      _("decilitre"),           _("decilitres"),           100),
            ("l",       _("litre"),               _("litres"),               1_000),
            ("decal",   _("decalitre"),           _("decalitres"),           10_000),
            ("m3",      _("cubic metre"),         _("cubic metres"),         1_000_000),
            ("cm3",     _("cubic centimetre"),    _("cubic centimetres"),    1),
            ("mm3",     _("cubic millimetre"),    _("cubic millimetres"),    0.001),
            ("dm3",     _("cubic decimetre"),     _("cubic decimetres"),     1_000),
            ("in3",     _("cubic inch"),          _("cubic inches"),         16.387064),    # exact
            ("ft3",     _("cubic foot"),          _("cubic feet"),           28_316.846592),
            ("pt",      _("pint US"),             _("pints US"),             473.176473),
            ("ptimp",   _("pint Imperial"),       _("pints Imperial"),       568.26125),
            ("qt",      _("quart US"),            _("quarts US"),            946.352946),
            ("qtimp",   _("quart Imperial"),      _("quarts Imperial"),      1_136.5225),
            ("cup",     _("cup US"),              _("cups US"),              236.588236),
            ("cupimp",  _("cup Imperial"),        _("cups Imperial"),        284.130625),
            ("tbsp",    _("tablespoon US"),       _("tablespoons US"),       14.786765),
            ("tbspimp", _("tablespoon Imperial"), _("tablespoons Imperial"), 17.758164),
            ("tsp",     _("teaspoon US"),         _("teaspoons US"),         4.928922),
            ("tspimp",  _("teaspoon Imperial"),   _("teaspoons Imperial"),   5.919388),
            ("gal",     _("gallon US"),           _("gallons US"),           3_785.411784),
            ("galimp",  _("gallon Imperial"),     _("gallons Imperial"),     4_546.09),
            ("floz",    _("fluid ounce US"),      _("fluid ounces US"),      29.573530),
            ("flozimp", _("fluid ounce Imperial"),_("fluid ounces Imperial"),28.413063),
            ("buuk",    _("bushel UK"),           _("bushels UK"),           36_368.72),
            ("buus",    _("bushel US"),           _("bushels US"),           35_239.07),
        ]
    },

    _("Weight"): {
        "base": "g",
        "units": [
            ("g",      _("gram"),          _("grams"),          1),
            ("mg",     _("milligram"),     _("milligrams"),     0.001),
            ("µg",     _("microgram"),     _("micrograms"),     1e-6),
            ("ng",     _("nanogram"),      _("nanograms"),      1e-9),
            ("kg",     _("kilogram"),      _("kilograms"),      1_000),
            ("t",      _("tonne"),         _("tonnes"),         1_000_000),
            ("lb",     _("pound"),         _("pounds"),         453.59237),        # exact
            ("oz",     _("ounce"),         _("ounces"),         28.349523125),     # exact
            ("st",     _("stone"),         _("stone"),          6_350.29318),
            ("ton",    _("US ton"),        _("US tons"),        907_184.74),
            ("tonimp", _("Imperial ton"),  _("Imperial tons"),  1_016_046.9088),
            ("Da",     _("dalton"),        _("daltons"),        1.66053906660e-24),# exact (2018 CODATA)
            ("u",      _("atomic mass unit"), _("atomic mass units"), 1.66053906660e-24),
        ]
    },

    _("Temperature"): {
        # Affine: to_base = (value + offset) * factor  (base = Celsius)
        "base": "c",
        "units": [
            ("c",  _("Celsius"),    _("Celsius"),    1,       0),
            ("f",  _("Fahrenheit"), _("Fahrenheit"), 1/1.8,  -32),
            ("k",  _("Kelvin"),     _("Kelvin"),     1,      -273.15),
            ("r",  _("Rankine"),    _("Rankine"),    1/1.8,  -491.67),
        ]
    },

    _("Speed"): {
        "base": "m/s",
        "units": [
            ("m/s",  _("metres per second"),    _("metres per second"),    1),
            ("km/h", _("kilometres per hour"),  _("kilometres per hour"),  1/3.6),
            ("mp/h", _("miles per hour"),       _("miles per hour"),       0.44704),  # exact
            ("ft/s", _("feet per second"),      _("feet per second"),      0.3048),   # exact
            ("kt",   _("knot"),                 _("knots"),                0.514444),
            ("mach", _("mach"),                 _("mach"),                 340.29),   # at sea level 15°C
            ("c",    _("speed of light"),       _("speed of light"),       299_792_458), # exact
        ]
    },

    _("Force"): {
        "base": "N",
        "units": [
            ("N",   _("newton"),         _("newtons"),         1),
            ("mN",  _("millinewton"),    _("millinewtons"),    0.001),
            ("kN",  _("kilonewton"),     _("kilonewtons"),     1_000),
            ("MN",  _("meganewton"),     _("meganewtons"),     1_000_000),
            ("dyn", _("dyne"),           _("dynes"),           1e-5),
            ("kgf", _("kilogram-force"), _("kilogram-force"),  9.80665),  # exact
            ("lbf", _("pound-force"),    _("pound-force"),     4.4482216152605),
            ("pdl", _("poundal"),        _("poundals"),        0.138254954376),
        ]
    },

    _("Pressure"): {
        "base": "Pa",
        "units": [
            ("Pa",   _("pascal"),              _("pascals"),              1),
            ("hPa",  _("hectopascal"),         _("hectopascals"),         100),
            ("kPa",  _("kilopascal"),          _("kilopascals"),          1_000),
            ("MPa",  _("megapascal"),          _("megapascals"),          1_000_000),
            ("GPa",  _("gigapascal"),          _("gigapascals"),          1e9),
            ("bar",  _("bar"),                 _("bar"),                  100_000),
            ("mbar", _("millibar"),            _("millibars"),            100),
            ("atm",  _("atmosphere"),          _("atmospheres"),          101_325),   # exact
            ("mmHg", _("millimetre of mercury"),_("millimetres of mercury"), 133.322387415),
            ("torr", _("torr"),                _("torr"),                 133.322368421),
            ("psi",  _("psi"),                 _("psi"),                  6_894.757293168),
            ("ksi",  _("ksi"),                 _("ksi"),                  6_894_757.293168),
            ("inHg", _("inch of mercury"),     _("inches of mercury"),    3_386.389),
        ]
    },

    _("Energy"): {
        "base": "J",
        "units": [
            ("J",    _("joule"),                _("joules"),                1),
            ("mJ",   _("millijoule"),           _("millijoules"),           0.001),
            ("kJ",   _("kilojoule"),            _("kilojoules"),            1_000),
            ("MJ",   _("megajoule"),            _("megajoules"),            1_000_000),
            ("GJ",   _("gigajoule"),            _("gigajoules"),            1e9),
            ("cal",  _("calorie (IT)"),         _("calories (IT)"),         4.1868),
            ("kcal", _("kilocalorie"),          _("kilocalories"),          4_186.8),
            ("kWh",  _("kilowatt-hour"),        _("kilowatt-hours"),        3_600_000),
            ("MWh",  _("megawatt-hour"),        _("megawatt-hours"),        3_600_000_000),
            ("BTU",  _("British thermal unit"), _("British thermal units"), 1_055.05585262),
            ("therm",_("therm"),                _("therms"),                105_480_400),
            ("eV",   _("electronvolt"),         _("electronvolts"),         1.602176634e-19),# exact
            ("keV",  _("kiloelectronvolt"),     _("kiloelectronvolts"),     1.602176634e-16),
            ("MeV",  _("megaelectronvolt"),     _("megaelectronvolts"),     1.602176634e-13),
            ("GeV",  _("gigaelectronvolt"),     _("gigaelectronvolts"),     1.602176634e-10),
            ("erg",  _("erg"),                  _("ergs"),                  1e-7),
        ]
    },

    _("Power"): {
        "base": "W",
        "units": [
            ("W",       _("watt"),                  _("watts"),                  1),
            ("mW",      _("milliwatt"),             _("milliwatts"),             0.001),
            ("kW",      _("kilowatt"),              _("kilowatts"),              1_000),
            ("MW",      _("megawatt"),              _("megawatts"),              1_000_000),
            ("GW",      _("gigawatt"),              _("gigawatts"),              1e9),
            ("hp",      _("horsepower (mech.)"),    _("horsepower (mech.)"),     745.69987),
            ("hpmet",   _("horsepower (metric)"),   _("horsepower (metric)"),    735.49875),
            ("BTU/hr",  _("BTU per hour"),          _("BTU per hour"),           0.29307107),
            ("kcal/hr", _("kilocalorie per hour"),  _("kilocalories per hour"),  1.163),
            ("VA",      _("volt-ampere"),           _("volt-amperes"),           1),
        ]
    },

    _("Torque"): {
        "base": "Nm",
        "units": [
            ("Nm",     _("newton-metre"),      _("newton-metres"),      1),
            ("kNm",    _("kilonewton-metre"),  _("kilonewton-metres"),  1_000),
            ("mNm",    _("millinewton-metre"), _("millinewton-metres"), 0.001),
            ("lbf_ft", _("pound-foot"),        _("pound-feet"),         1.3558179483314),
            ("lbf_in", _("pound-inch"),        _("pound-inches"),       0.1129848290276),
            ("kgfm",   _("kilogram-force metre"), _("kilogram-force metres"), 9.80665),
            ("ozf_in", _("ounce-force inch"),  _("ounce-force inches"), 0.0070615517),
            ("dyn_cm", _("dyne-centimetre"),   _("dyne-centimetres"),   1e-7),
        ]
    },

    _("Frequency"): {
        "base": "Hz",
        "units": [
            ("Hz",  _("hertz"),     _("hertz"),     1),
            ("kHz", _("kilohertz"), _("kilohertz"), 1_000),
            ("MHz", _("megahertz"), _("megahertz"), 1_000_000),
            ("GHz", _("gigahertz"), _("gigahertz"), 1e9),
            ("THz", _("terahertz"), _("terahertz"), 1e12),
            ("rpm", _("RPM"),       _("RPM"),       1/60),
            ("rps", _("rev/s"),     _("rev/s"),     1),
            ("rad/s", _("radian/second"), _("radians/second"), 1/(2 * 3.14159265358979323846)),
        ]
    },

    _("Angle"): {
        "base": "deg",
        "units": [
            ("deg",    _("degree"),      _("degrees"),      1),
            ("rad",    _("radian"),      _("radians"),      180 / 3.14159265358979323846),
            ("grad",   _("gradian"),     _("gradians"),     0.9),
            ("arcmin", _("arcminute"),   _("arcminutes"),   1/60),
            ("arcsec", _("arcsecond"),   _("arcseconds"),   1/3600),
            ("rev",    _("revolution"),  _("revolutions"),  360),
            ("mrad",   _("milliradian"), _("milliradians"), 180 / (3.14159265358979323846 * 1000)),
        ]
    },

    _("Amount of substance"): {
        "base": "mol",
        "units": [
            ("mol",  _("mole"),      _("moles"),      1),
            ("mmol", _("millimole"), _("millimoles"), 0.001),
            ("µmol", _("micromole"), _("micromoles"), 1e-6),
            ("nmol", _("nanomole"),  _("nanomoles"),  1e-9),
            ("pmol", _("picomole"),  _("picomoles"),  1e-12),
            ("kmol", _("kilomole"),  _("kilomoles"),  1_000),
        ]
    },

    _("Radioactivity"): {
        "base": "Bq",
        "units": [
            ("Bq",  _("becquerel"),  _("becquerels"),  1),
            ("kBq", _("kilobecquerel"), _("kilobecquerels"), 1_000),
            ("MBq", _("megabecquerel"), _("megabecquerels"), 1_000_000),
            ("GBq", _("gigabecquerel"), _("gigabecquerels"), 1e9),
            ("TBq", _("terabecquerel"), _("terabecquerels"), 1e12),
            ("Ci",  _("curie"),      _("curies"),      3.7e10),
            ("mCi", _("millicurie"), _("millicuries"), 3.7e7),
            ("µCi", _("microcurie"), _("microcuries"), 37_000),
            ("nCi", _("nanocurie"),  _("nanocuries"),  37),
            ("dpm", _("disintegrations per minute"), _("disintegrations per minute"), 1/60),
        ]
    },

    _("Radiation dose"): {
        # Absorbed dose — gray (Gy) as base
        "base": "Gy",
        "units": [
            ("Gy",   _("gray"),       _("grays"),       1),
            ("mGy",  _("milligray"),  _("milligrays"),  0.001),
            ("µGy",  _("microgray"),  _("micrograys"),  1e-6),
            ("cGy",  _("centigray"),  _("centigrays"),  0.01),
            ("rad",  _("rad"),        _("rads"),        0.01),
            ("mrad", _("millirad"),   _("millirads"),   1e-5),
        ]
    },

    _("Dose equivalent"): {
        # Sievert as base
        "base": "Sv",
        "units": [
            ("Sv",   _("sievert"),     _("sieverts"),     1),
            ("mSv",  _("millisievert"),_("millisieverts"), 0.001),
            ("µSv",  _("microsievert"),_("microsieverts"), 1e-6),
            ("rem",  _("rem"),         _("rem"),           0.01),
            ("mrem", _("millirem"),    _("millirem"),      1e-5),
        ]
    },

    _("Density"): {
        "base": "kg/m3",
        "units": [
            ("kg/m3",  _("kilogram per cubic metre"), _("kilograms per cubic metre"), 1),
            ("g/cm3",  _("gram per cubic centimetre"),_("grams per cubic centimetre"), 1_000),
            ("g/mL",   _("gram per millilitre"),      _("grams per millilitre"),      1_000),
            ("kg/L",   _("kilogram per litre"),       _("kilograms per litre"),       1_000),
            ("g/L",    _("gram per litre"),           _("grams per litre"),           1),
            ("mg/L",   _("milligram per litre"),      _("milligrams per litre"),      0.001),
            ("lb/ft3", _("pound per cubic foot"),     _("pounds per cubic foot"),     16.01846337),
            ("lb/in3", _("pound per cubic inch"),     _("pounds per cubic inch"),     27_679.9047102),
            ("lb/gal", _("pound per US gallon"),      _("pounds per US gallon"),      119.826427),
        ]
    },

    _("Dynamic viscosity"): {
        "base": "Pa_s",
        "units": [
            ("Pa_s",   _("pascal-second"),  _("pascal-seconds"),  1),
            ("mPa_s",  _("millipascal-second"), _("millipascal-seconds"), 0.001),
            ("cP",     _("centipoise"),     _("centipoise"),      0.001),
            ("P",      _("poise"),          _("poise"),           0.1),
            ("lb/ft_s",_("pound per foot-second"), _("pound per foot-second"), 1.4881639),
        ]
    },

    _("Kinematic viscosity"): {
        "base": "m2/s",
        "units": [
            ("m2/s",  _("square metre per second"),      _("square metres per second"),      1),
            ("mm2/s", _("square millimetre per second"),  _("square millimetres per second"), 1e-6),
            ("cSt",   _("centistokes"),  _("centistokes"), 1e-6),
            ("St",    _("stokes"),       _("stokes"),      1e-4),
            ("ft2/s", _("square foot per second"), _("square feet per second"), 0.09290304),
        ]
    },

    _("Data"): {
        "base": "B",
        "units": [
            # SI decimal — bytes
            ("B",   _("byte"),      _("bytes"),      1),
            ("KB",  _("kilobyte"),  _("kilobytes"),  10**3),
            ("MB",  _("megabyte"),  _("megabytes"),  10**6),
            ("GB",  _("gigabyte"),  _("gigabytes"),  10**9),
            ("TB",  _("terabyte"),  _("terabytes"),  10**12),
            ("PB",  _("petabyte"),  _("petabytes"),  10**15),
            # SI decimal — bits
            ("b",   _("bit"),       _("bits"),       1/8),
            ("Kb",  _("kilobit"),   _("kilobits"),   10**3  / 8),
            ("Mb",  _("megabit"),   _("megabits"),   10**6  / 8),
            ("Gb",  _("gigabit"),   _("gigabits"),   10**9  / 8),
            ("Tb",  _("terabit"),   _("terabits"),   10**12 / 8),
            ("Pb",  _("petabit"),   _("petabits"),   10**15 / 8),
            # IEC binary — bytes
            ("KiB", _("kibibyte"),  _("kibibytes"),  2**10),
            ("MiB", _("mebibyte"),  _("mebibytes"),  2**20),
            ("GiB", _("gibibyte"),  _("gibibytes"),  2**30),
            ("TiB", _("tebibyte"),  _("tebibytes"),  2**40),
            ("PiB", _("pebibyte"),  _("pebibytes"),  2**50),
            # IEC binary — bits
            ("Kib", _("kibibit"),   _("kibibits"),   2**10 / 8),
            ("Mib", _("mebibit"),   _("mebibits"),   2**20 / 8),
            ("Gib", _("gibibit"),   _("gibibits"),   2**30 / 8),
            ("Tib", _("tebibit"),   _("tebibits"),   2**40 / 8),
            ("Pib", _("pebibit"),   _("pebibits"),   2**50 / 8),
        ]
    },
}


# ---------------------------------------------------------------------------
# Conversion engine
# ---------------------------------------------------------------------------

def convert(value: float, from_abbr: str, to_abbr: str, category: str) -> float:
    """Convert value between two units in the same category."""
    unit_map = {u[0]: u for u in units[category]["units"]}
    src = unit_map[from_abbr]
    dst = unit_map[to_abbr]

    if len(src) == 5:  # affine (Temperature, Rankine, etc.)
        base_value = (value + src[4]) * src[3]
        return (base_value / dst[3]) - dst[4]
    else:              # linear
        return value * src[3] / dst[3]
