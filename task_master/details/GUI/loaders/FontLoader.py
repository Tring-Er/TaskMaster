import os
from ctypes import windll, byref, create_string_buffer

from ProgramData import ProgramData


class FontLoader:

    @staticmethod
    def load_nexa_font() -> None:
        FontLoader.load_font(FontLoader.get_font_path())

    @staticmethod
    def load_font(font_path: str) -> None:
        FR_PRIVATE  = 0x10
        FR_NOT_ENUM = 0x20
        byte_font_path = bytes(font_path, "utf-8")
        path_buffer = create_string_buffer(byte_font_path)
        flags = FR_PRIVATE | FR_NOT_ENUM
        windll.gdi32.AddFontResourceExA(byref(path_buffer), flags, 0)

    @staticmethod
    def get_font_path() -> str:
        return os.path.join(ProgramData.get_current_folder_path(), "resources", "fonts", "NexaRustSlab-BlackShadow01.otf")
