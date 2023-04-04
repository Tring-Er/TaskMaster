import os
import sys
from ctypes import windll, byref, create_string_buffer


USER_HOME_PATH = os.path.expanduser("~")
DOCUMENTS_PATH = os.path.join(USER_HOME_PATH, "Documents")
TASKMASTER_FOLDER_PATH = os.path.join(DOCUMENTS_PATH, "TaskMaster")
TASKS_FOLDER_PATH = os.path.join(TASKMASTER_FOLDER_PATH, "Tasks")
CURRENT_FOLDER = ...
FONT_PATH = ...

REQUIRED_FOLDERS = (TASKMASTER_FOLDER_PATH, TASKS_FOLDER_PATH)


class Loader:
    
    @staticmethod
    def startup() -> None:
        Loader.set_current_folder()
        Loader.load_font(FONT_PATH)
        Loader.create_task_master_folders_if_not_present()
    
    @staticmethod
    def create_task_master_folders_if_not_present() -> None:
        for folder in REQUIRED_FOLDERS:
            Loader.create_folder_if_not_present(folder)
    
    @staticmethod
    def create_folder_if_not_present(folder_path: str) -> None:
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            ...
    
    @staticmethod
    def load_font(font_path: str) -> None:
        print(CURRENT_FOLDER, FONT_PATH)
        FR_PRIVATE  = 0x10
        FR_NOT_ENUM = 0x20
        byte_font_path = bytes(font_path, "utf-8")
        path_buffer = create_string_buffer(byte_font_path)
        flags = FR_PRIVATE | FR_NOT_ENUM
        windll.gdi32.AddFontResourceExA(byref(path_buffer), flags, 0)
    
    @staticmethod
    def is_project_compiled() -> bool:
        if getattr(sys, 'frozen', False):
            return True
        return False
    
    @staticmethod
    def set_current_folder() -> None:
        global CURRENT_FOLDER, FONT_PATH
        if Loader.is_project_compiled():
            CURRENT_FOLDER = os.path.dirname(sys.executable)
        else:
            CURRENT_FOLDER = os.path.abspath(os.path.dirname(__file__))
        FONT_PATH = os.path.join(CURRENT_FOLDER, "resources", "fonts", "NexaRustSlab-BlackShadow01.otf")
    
    @staticmethod
    def get_title_bar_icon() -> str:
        return os.path.join(CURRENT_FOLDER, "resources", "icons", "title_bar.ico")
