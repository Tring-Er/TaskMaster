import os
import sys
from ctypes import windll, byref, create_string_buffer


class Program:

    def __init__(self) -> None:
        self.required_folders = (self.get_taskmaster_folder_path(), self.get_tasks_folder_path())
        self.startup()
    
    def get_user_home_path(self) -> str:
        return os.path.expanduser("~")
    
    def get_document_path(self) -> str:
        return os.path.join(self.get_user_home_path(), "Documents")
    
    def get_taskmaster_folder_path(self) -> str:
        return os.path.join(self.get_document_path(), "TaskMaster")
    
    def get_tasks_folder_path(self) -> str:
        return os.path.join(self.get_taskmaster_folder_path(), "Tasks")
    
    def get_tasks_file_path(self) -> str:
        return os.path.join(self.get_tasks_folder_path(), r"tasks.txt")
    
    def get_exported_tasks_file_path(self) -> str:
        return os.path.join(self.get_tasks_folder_path(), r"exported_tasks.txt")
    
    def startup(self) -> None:
        self.load_font(self.get_font_path())
        self.create_task_master_folders_if_not_present()
    
    def create_task_master_folders_if_not_present(self) -> None:
        for folder in self.required_folders:
            self.create_folder_if_not_present(folder)
    
    def create_folder_if_not_present(self, folder_path: str) -> None:
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass
    
    def load_font(self, font_path: str) -> None:
        FR_PRIVATE  = 0x10
        FR_NOT_ENUM = 0x20
        byte_font_path = bytes(font_path, "utf-8")
        path_buffer = create_string_buffer(byte_font_path)
        flags = FR_PRIVATE | FR_NOT_ENUM
        windll.gdi32.AddFontResourceExA(byref(path_buffer), flags, 0)
    
    def is_project_compiled(self) -> bool:
        if getattr(sys, 'frozen', False):
            return True
        return False
    
    def get_current_folder_path(self) -> str:
        if self.is_project_compiled():
            return os.path.dirname(sys.executable)
        return os.path.abspath(os.path.dirname(__file__))
    
    def get_font_path(self) -> str:
        return os.path.join(self.get_current_folder_path(), "resources", "fonts", "NexaRustSlab-BlackShadow01.otf")
    
    def get_title_bar_icon_path(self) -> str:
        return os.path.join(self.get_current_folder_path(), "resources", "icons", "title_bar.ico")
