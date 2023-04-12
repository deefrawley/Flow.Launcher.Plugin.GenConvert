import locale
import textwrap
import re
import units as gc_units

from translation import _
from flox import Flox


class GenConvert(Flox):
    locale.setlocale(locale.LC_NUMERIC, "")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger_level("info")

    def query(self, query):
        q = query.strip()
        args = q.split(" ")
        # Just keyword - show all units if the setting allows
        if len(args) == 1:
            all_units = get_all_units()
            self.add_item(
                title=_("General Converter"),
                subtitle=_(
                    "<Hotkey> <Amount> <Source unit - case sensitive> <Destination unit - case sensitive>"
                ),
            )
            if self.settings.get("show_helper_text"):
                for cat in all_units:
                    title = str(cat[0])
                    subtitle = ", ".join([str(elem) for elem in cat[1:]])
                    lines = textwrap.wrap(subtitle, 110, break_long_words=False)
                    if len(lines) > 1:
                        self.add_item(
                            title=(title),
                            subtitle=(lines[0]),
                            icon=f"assets/{title}.ico",
                        )
                        for line in range(1, len(lines)):
                            self.add_item(
                                title=(title),
                                subtitle=(lines[line]),
                                icon=f"assets/{title}.ico",
                            )
                    else:
                        self.add_item(
                            title=(title),
                            subtitle=(subtitle),
                            icon=f"assets/{title}.ico",
                        )
        # Keyword and first unit to convert from - show what it can be converted to
        elif len(args) == 2:
            hints = get_hints_for_category(args[1])
            self.add_item(
                title=_("Available conversions"),
                subtitle=(f"{args[0]} {args[1]} to {', '.join(hints)}"),
            )
        # Keyword and two units to convert from and to - try to convert
        elif len(args) == 3:
            try:
                # Units are case sensitive.
                do_convert = gen_convert(float(args[0]), args[1], args[2])
                if "Error" in do_convert:
                    if do_convert["Error"] == _("To and from unit is the same"):
                        self.add_item(
                            title=_("{}".format(do_convert["Error"])),
                            subtitle=_("Choose two different units"),
                        )
                    else:
                        self.add_item(
                            # f strings seem to break babel so use string formatting instead
                            title=_("Error - {}").format(do_convert["Error"]),
                            subtitle=_("Check documentation for accepted units"),
                        )
                else:
                    c = do_convert["converted"]
                    p = smart_precision(locale.localeconv()["decimal_point"], c, 3)
                    self.add_item(
                        title=(do_convert["category"]),
                        subtitle=(
                            f"{locale.format_string('%.10g', float(args[0]), grouping=True)} {args[1]} = {locale.format_string(f'%.{p}f', c, grouping=True)} {args[2]}"
                        ),
                        icon=f"assets/{do_convert['category']}.ico",
                    )
                    do_convert = []
            except Exception as e:
                self.add_item(title="Error - {}").format(repr(e), subtitle="")
        # Always show the usage while there isn't a valid query
        else:
            self.add_item(
                title=_("General Converter"),
                subtitle=_("<Hotkey> <Amount> <Source unit> <Destination unit>"),
            )


def get_all_units(short=False):
    """Returns all available units as a list of lists by category

    :param short: if True only unit abbreviations are returned, default is False
    :type amount: bool

    :rtype: list of lists
    :return: A list of lists for each category in units. Index 0 of each internal list
            is the category description
    """

    full_list = []
    for u in gc_units.units:
        cat_list = []
        cat_list.append(u)
        for u2 in gc_units.units[u]:
            cat_list.append(u2[0] if short else f"{u2[1]} ({u2[0]})")
        full_list.append(cat_list)
    return full_list


def get_hints_for_category(from_unit: str):
    """Takes an input unit and returns a list of units it can be converted to

    :param from_short: unit abbreviation
    :type amount: str

    :rtype: list
    :return: A list of other unit abbreviations in the same category
    """
    c = []
    category = ""

    # Find the category it's in
    for u in gc_units.units:
        for u2 in gc_units.units[u]:
            if u2[0] == from_unit or u2[1] == from_unit or u2[2] == from_unit:
                category = str(u)
                for uu in gc_units.units[category]:
                    if uu[0] != from_unit:
                        c.append(uu[0])
    if category:
        return c
    else:
        return ["no valid units"]


def gen_convert(amount: float, from_unit: str, to_unit: str):
    """Converts from one unit to another

    :param amount: amount of source unit to convert
    :type amount: float
    :param from_unit: abbreviation of unit  to convert from
    :type from_unit: str
    :param to_unit: abbreviation of unit to convert to
    :type to_unit: str

    :rtype: dict
    :return: if to_unit and from_unit are valid returns a dictionary
            {
                "category":{category of units},
                "converted":{converted amount},
                "fromabbrev":{from unit abbreviation},
                "fromlong":{from unit long name},
                "fromplural":{from unit plural name},
                "toabbrev":{to unit abbreviation},
                "tolong":{to unit long name},
                "toplural":{to unit plural name},
            }

            else returns a dictionary with error status
            {"Error": {error text}}
    """
    conversions = {}
    found_from = found_to = []
    if from_unit == to_unit:
        conversions["Error"] = _("To and from unit is the same")
        return conversions
    for u in gc_units.units:
        for u2 in gc_units.units[u]:
            if u2[0] == from_unit or u2[1] == from_unit or u2[2] == from_unit:
                found_from = u2
            if u2[0] == to_unit or u2[1] == to_unit or u2[2] == to_unit:
                found_to = u2
        # If we haven't both in the same category, reset
        if found_to and found_from:
            found_category = u
            break
        else:
            found_from = found_to = []
    if found_to and found_from:
        base_unit_conversion = eval(found_from[3].replace("x", str(amount)))
        final_conversion = eval(found_to[4].replace("x", str(base_unit_conversion)))
        conversions["category"] = found_category
        conversions["converted"] = final_conversion
        conversions["fromabbrev"] = found_from[0]
        conversions["fromlong"] = found_from[1]
        conversions["fromplural"] = found_from[2]
        conversions["toabbrev"] = found_to[0]
        conversions["tolong"] = found_to[1]
        conversions["toplural"] = found_to[2]

    else:
        conversions["Error"] = "Problem converting {} and {}".format(from_unit, to_unit)
    return conversions


def smart_precision(separator, amount, preferred=3):
    str_amt = str(amount)
    dec_places = str_amt[::-1].find(separator)
    # whole number
    if dec_places == -1:
        return 0
    frac_part = str_amt[-dec_places::]
    # fraction is just zeroes
    if int(frac_part) == 0:
        return 0
    fnz = re.search(r"[1-9]", frac_part).start()
    if fnz < preferred:
        return preferred
    return fnz + 1
