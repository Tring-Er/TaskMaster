"""Imports all module in this folder and their respective classes (inside of the module)
in order to make this work, the class MUST have the same name as the module but with camel case
convenction.

So for example, if you have a module named reverse_task_text
then the class inside reverse_task_text.py MUST be called ReverseTaskText

Remember that the class MUST be a Mode class
"""

import importlib
import os

from presenter.modes.mode import Mode  # noqa: F401

files = os.listdir("./task_master/presenter/modes")
MODES = {}

for file in files:
    module_name = file.split(".py")[0]
    if module_name in ["__init__", "mode", "__pycache__"]:
        continue
    module = importlib.import_module("presenter.modes." + module_name)
    module_words = module_name.split("_")
    if len(module_words) > 1:
        capitalized_module_words = map(lambda word: word.capitalize(), module_words)
    else:
        capitalized_module_words = module_words[0].capitalize()
    class_name = "".join(capitalized_module_words)
    _class = getattr(module, class_name)
    MODES[_class.CLI_COMMAND] = _class
