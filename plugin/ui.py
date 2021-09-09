# -*- coding: utf-8 -*-
import textwrap
import copy
import locale
import plugin.utils

from typing import List
from plugin.templates import RESULT_TEMPLATE, ACTION_TEMPLATE
from flowlauncher import FlowLauncher
from plugin.extensions import _


class Main(FlowLauncher):
    messages_queue = []
    locale.setlocale(locale.LC_NUMERIC, "")

    def sendNormalMess(
        self, title: str, subtitle: str, iconpath: str = "assets/favicon.ico"
    ):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle
        message["IcoPath"] = iconpath

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, method: str, value: List):
        # information
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        # action
        action = copy.deepcopy(ACTION_TEMPLATE)
        action["JsonRPCAction"]["method"] = method
        action["JsonRPCAction"]["parameters"] = value
        message.update(action)

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        q = param.strip()
        args = q.split(" ")
        # Just keyword - show all units
        if len(args) == 1:
            all_units = plugin.utils.get_all_units()
            self.sendNormalMess(
                (_("General Converter")),
                _("<Hotkey> <Amount> <Source unit> <Destination unit>"),
            )
            for cat in all_units:
                title = str(cat[0])
                subtitle = ", ".join([str(elem) for elem in cat[1:]])
                lines = textwrap.wrap(subtitle, 110, break_long_words=False)
                if len(lines) > 1:
                    self.sendNormalMess((title), (lines[0]), f"assets/{title}.ico")
                    for line in range(1, len(lines)):
                        self.sendNormalMess(
                            (title), (lines[line]), f"assets/{title}.ico"
                        )
                else:
                    self.sendNormalMess((title), (subtitle), f"assets/{title}.ico")
        # Keyword and first unit to convert from - show what it can be converted to
        elif len(args) == 2:
            hints = plugin.utils.get_hints_for_category(args[1].lower())
            self.sendNormalMess(
                _("Available conversions"),
                (f"{args[0]} {args[1]} to {', '.join(hints)}"),
            )
        # Keyword and two units to convert from and to - try to convert
        elif len(args) == 3:
            try:
                # Units are currently case insensitive. May need to change this if in future new units
                # with official upper case shorthand are catered for
                args[1] = args[1].lower()
                args[2] = args[2].lower()
                do_convert = plugin.utils.gen_convert(float(args[0]), args[1], args[2])
                if "Error" in do_convert:
                    if do_convert["Error"] == "To and from unit is the same":
                        self.sendNormalMess(
                            _("{}".format(do_convert["Error"])),
                            _("Choose two different units"),
                        )
                    else:
                        self.sendNormalMess(
                            # f strings seem to break babel so use string formatting instead
                            _("Error - {}").format(do_convert["Error"]),
                            _("Check documentation for accepted units"),
                        )
                else:
                    self.sendNormalMess(
                        (do_convert["category"]),
                        (
                            f"{locale.format_string('%.6g', float(args[0]), grouping=True)} {args[1]} = {locale.format_string('%f', do_convert['converted'], grouping=True)} {args[2]}"
                        ),
                        f"assets/{do_convert['category']}.ico",
                    )
                    do_convert = []
            except Exception as e:
                self.sendNormalMess(_("Error - {}").format(repr(e)), "")
        # Always show the usage while there isn't a valid query
        else:
            self.sendNormalMess(
                _("General Converter"),
                _("<Hotkey> <Amount> <Source unit> <Destination unit>"),
            )
        return self.messages_queue
