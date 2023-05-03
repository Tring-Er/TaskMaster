import sys
import os


class ProgramData:
    
    @staticmethod
    def is_project_compiled() -> bool:
        if getattr(sys, 'frozen', False):
            return True
        return False
    
    @staticmethod
    def get_current_folder_path() -> str:
        if ProgramData.is_project_compiled():
            return os.path.dirname(sys.executable)
        return os.path.abspath(os.path.dirname(__file__))
