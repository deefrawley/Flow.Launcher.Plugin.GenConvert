# -*- coding: utf-8 -*-

import copy
import plugin.utils

from typing import List
from plugin.templates import RESULT_TEMPLATE, ACTION_TEMPLATE
from flowlauncher import FlowLauncher
from plugin.extensions import _


class Main(FlowLauncher):
    messages_queue = []

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

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

        if len(args) == 3:
            try:
                # Units are currently case insensitive. May need to change this if in future new units
                # with official upper case shorthand are catered for
                args[1] = args[1].lower()
                args[2] = args[2].lower()
                do_convert = plugin.utils.genConvert(float(args[0]), args[1], args[2])
                if "Error" in do_convert:
                    self.sendNormalMess(
                        _("Error - {}").format(do_convert["Error"]),
                        _("Check documentation for accepted units"),
                    )
                else:
                    self.sendNormalMess(
                        (f"{args[0]} {args[1]} = {do_convert[args[2]]:.6f} {args[2]}"),
                        "",
                    )
            except Exception as e:
                self.sendNormalMess(_("Error - {}").format(repr(e)), "")
        # Always show the usage while there isn't a valid query
        else:
            self.sendNormalMess(
                _("General Converter"),
                _("<Hotkey> <Amount> <Source unit> <Destination unit>"),
            )
        return self.messages_queue
