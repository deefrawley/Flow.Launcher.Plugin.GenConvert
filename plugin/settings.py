# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dotenv_path = os.path.join(basedir, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# The default value can work, if no user config.
LOCAL = os.getenv("local", "en")


ICON_PATH = "assets/favicon.ico"

# the information of package
__package_name__ = "Flow.Launcher.Plugin.GenConvert"
__package_title__ = "General Converter"
__version__ = "1.0.0"
__short_description__ = "General weights and measures converter"
GITHUB_USERNAME = "deefrawley"


readme_path = os.path.join(basedir, "README.md")
try:
    __long_description__ = open(readme_path, "r").read()
except:
    __long_description__ = __short_description__


# other information
PLUGIN_ID = "73f2c04d-176a-4586-9ff5-69fae63321ef"
ICON_PATH = "assets/favicon.ico"
PLUGIN_ACTION_KEYWORD = "gc"
PLUGIN_AUTHOR = "deefrawley"
PLUGIN_PROGRAM_LANG = "python"
PLUGIN_URL = f"https://github.com/{GITHUB_USERNAME}/{__package_name__}"
PLUGIN_EXECUTE_FILENAME = "main.py"
