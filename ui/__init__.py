from menu import Menu, MenuExitException
from printer import Printer
from listbox import Listbox
from refresher import Refresher
from checkbox import Checkbox
from path_picker import PathPicker
from number_input import IntegerAdjustInput
IntegerInDecrementInput = IntegerAdjustInput #Compatibility with old ugly name
from char_input import CharArrowKeysInput
from dialog import DialogBox

from funcs import ellipsize, format_for_screen


def to_be_foreground(func):
    """A safety check wrapper so that certain checks don't get called if menu is not the one active."""
    def wrapper(self, *args, **kwargs):
        if self.in_foreground:
            return func(self, *args, **kwargs)
        else:
            return False
    return wrapper
