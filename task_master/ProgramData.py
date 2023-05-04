import sys
import os


class ProgramData:

    @staticmethod
    def get_required_folders() -> tuple[str]:
        return (ProgramData.get_taskmaster_folder_path(), ProgramData.get_tasks_folder_path())

    @staticmethod
    def get_user_home_path() -> str:
        return os.path.expanduser("~")
    
    @staticmethod
    def get_document_path() -> str:
        return os.path.join(ProgramData.get_user_home_path(), "Documents")
    
    @staticmethod
    def get_taskmaster_folder_path() -> str:
        return os.path.join(ProgramData.get_document_path(), "TaskMaster")
    
    @staticmethod
    def get_tasks_folder_path() -> str:
        return os.path.join(ProgramData.get_taskmaster_folder_path(), "Tasks")
    
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
