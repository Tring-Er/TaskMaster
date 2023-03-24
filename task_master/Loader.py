import os
from ctypes import windll, byref, create_string_buffer


USER_HOME_PATH = os.path.expanduser("~")
DOCUMENTS_PATH = os.path.join(USER_HOME_PATH, "Documents")
TASKMASTER_FOLDER_PATH = os.path.join(DOCUMENTS_PATH, "TaskMaster")
TASKS_FOLDER_PATH = os.path.join(TASKMASTER_FOLDER_PATH, "Tasks")
FONT_PATH = rb"C:\Users\tring\Desktop\TaskMaster\task_master\resources\fonts\NexaRustSlab-BlackShadow01.otf"

REQUIRED_FOLDERS = (TASKMASTER_FOLDER_PATH, TASKS_FOLDER_PATH)

FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20


class Loader:
    
    @staticmethod
    def startup() -> None:
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
    def load_font(fontpath: str) -> None:
        path_buffer = create_string_buffer(fontpath)
        flags = FR_PRIVATE | FR_NOT_ENUM
        windll.gdi32.AddFontResourceExA(byref(path_buffer), flags, 0)