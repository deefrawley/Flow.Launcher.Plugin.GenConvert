import locale
import textwrap
import re
import subprocess
import units as gc_units

from translation import _
from flox import Flox

try:
    locale.setlocale(locale.LC_NUMERIC, "")
except locale.Error:
    locale.setlocale(locale.LC_NUMERIC, "C")


# ---------------------------------------------------------------------------
# Unit lookup helpers
# ---------------------------------------------------------------------------

def _find_unit(abbr: str):
    """Return (category_key, unit_tuple) or (None, None)."""
    for cat_key, cat in gc_units.units.items():
        for u in cat["units"]:
            if abbr in (u[0], u[1], u[2]):
                return cat_key, u
    return None, None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_all_units(short: bool = False) -> list:
    """Return [[category, unit, ...], ...] — index 0 is always the category name."""
    result = []
    for cat_key, cat in gc_units.units.items():
        row = [cat_key] + [u[0] if short else f"{u[1]} ({u[0]})" for u in cat["units"]]
        result.append(row)
    return result


def get_hints_for_category(from_unit: str) -> list:
    """Return abbreviations of all other units in the same category."""
    cat_key, _ = _find_unit(from_unit)
    if not cat_key:
        return [_("no valid units")]
    return [u[0] for u in gc_units.units[cat_key]["units"] if u[0] != from_unit]


def gen_convert(amount: float, from_unit: str, to_unit: str) -> dict:
    """Convert amount from from_unit to to_unit.

    Returns a result dict on success or {"Error": reason} on failure.
    """
    if from_unit == to_unit:
        return {"Error": _("To and from unit is the same")}

    from_cat, src = _find_unit(from_unit)
    to_cat,   dst = _find_unit(to_unit)

    if not src or not dst:
        return {"Error": _("Problem converting {} and {}").format(from_unit, to_unit)}
    if from_cat != to_cat:
        return {"Error": _("Units are from different categories")}

    return {
        "category":   from_cat,
        "converted":  gc_units.convert(amount, src[0], dst[0], from_cat),
        "fromabbrev": src[0],
        "fromlong":   src[1],
        "fromplural": src[2],
        "toabbrev":   dst[0],
        "tolong":     dst[1],
        "toplural":   dst[2],
    }


def smart_precision(separator: str, amount: float, preferred: int = 3) -> int:
    """Return an appropriate number of decimal places for display."""
    s = str(amount)
    dec_places = s[::-1].find(separator)
    if dec_places == -1:
        return 0
    frac = s[-dec_places:]
    if int(frac) == 0:
        return 0
    fnz = re.search(r"[1-9]", frac).start()
    return preferred if fnz < preferred else fnz + 1


# ---------------------------------------------------------------------------
# Flox plugin
# ---------------------------------------------------------------------------

class GenConvert(Flox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger_level("info")

    def query(self, query):
        args = query.strip().split()

        if len(args) == 1:
            self._show_all_units()
        elif len(args) == 2:
            hints = get_hints_for_category(args[1])
            self.add_item(
                title=_("Available conversions"),
                subtitle=f"{args[0]} {args[1]} to {', '.join(hints)}",
            )
        elif len(args) == 3:
            self._do_convert(*args)
        else:
            self.add_item(
                title=_("General Converter"),
                subtitle=_("<Hotkey> <Amount> <Source unit> <Destination unit>"),
            )

    def _show_all_units(self):
        self.add_item(
            title=_("General Converter"),
            subtitle=_("<Hotkey> <Amount> <Source unit - case sensitive> <Destination unit - case sensitive>"),
        )
        if not self.settings.get("show_helper_text"):
            return
        for cat in get_all_units():
            title    = str(cat[0])
            subtitle = ", ".join(str(e) for e in cat[1:])
            icon     = f"assets/{title}.ico"
            for line in textwrap.wrap(subtitle, 110, break_long_words=False) or [subtitle]:
                self.add_item(title=title, subtitle=line, icon=icon)

    def _do_convert(self, raw_amount: str, from_unit: str, to_unit: str):
        try:
            result = gen_convert(float(raw_amount), from_unit, to_unit)
        except ValueError:
            self.add_item(title=_("Error - invalid number"), subtitle=raw_amount)
            return

        if "Error" in result:
            err = result["Error"]
            sub = (_("Choose two different units")
                   if err == _("To and from unit is the same")
                   else _("Check documentation for accepted units"))
            self.add_item(title=err, subtitle=sub)
            return

        dp            = locale.localeconv()["decimal_point"]
        precision     = smart_precision(dp, result["converted"], 3)
        amount_fmt    = locale.format_string("%.10g",            float(raw_amount),   grouping=True)
        converted_fmt = locale.format_string(f"%.{precision}f", result["converted"], grouping=True)
        copy_value    = locale.format_string(f"%.{precision}f", result["converted"])  # no thousands sep

        self.add_item(
            title=result["category"],
            subtitle=(
                f"{amount_fmt} {result['fromplural']} ({result['fromabbrev']}) = "
                f"{converted_fmt} {result['toplural']} ({result['toabbrev']})"
                f"  [Enter copies value]"
            ),
            icon=f"assets/{result['category']}.ico",
            method=self.copy_to_clipboard,
            parameters=[copy_value],
        )

    def copy_to_clipboard(self, value: str):
        """Copy converted value to Windows clipboard via clip.exe."""
        subprocess.run(["clip"], input=value.encode("utf-16-le"), check=True)
