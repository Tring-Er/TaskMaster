"""Imports all module in this folder and their respective classes (inside of the module)
in order to make this work, the class MUST have the same name as the module but with camel case
convenction.

So for example, if you have a module named reverse_task_text
then the class inside reverse_task_text.py MUST be called ReverseTaskText

Remember that the class MUST be a Mode class
"""

import importlib
import os

from presenter.cli.modes.mode import Mode

files = os.listdir("./task_master/presenter/cli/modes")
MODES = {}

for file in files:
    module_name = file.removesuffix(".py")
    if module_name in ["__init__", "mode", "__pycache__"]:
        continue
    module = importlib.import_module("presenter.cli.modes." + module_name)
    words_in_module_name = module_name.split("_")
    capitalized_module_words = map(lambda word: word.capitalize(), words_in_module_name)
    class_name = "".join(capitalized_module_words)
    _class = getattr(module, class_name)
    MODES[_class.CLI_COMMAND] = _class