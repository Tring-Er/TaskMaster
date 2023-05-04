import os

from ProgramData import ProgramData


class FolderCreator:

    @staticmethod
    def create_task_master_folders_if_not_present() -> None:
        for folder in ProgramData.get_required_folders():
            FolderCreator.create_folder_if_not_present(folder)
    
    @staticmethod
    def get_tasks_file_path() -> str:
        return os.path.join(ProgramData.get_tasks_folder_path(), r"tasks.txt")
    
    @staticmethod
    def get_exported_tasks_file_path() -> str:
        return os.path.join(ProgramData.get_tasks_folder_path(), r"exported_tasks.txt")
    
    @staticmethod
    def create_folder_if_not_present(folder_path: str) -> None:
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass
