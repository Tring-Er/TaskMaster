import os

from ProgramData import ProgramData


class FolderCreator:

    @staticmethod
    def create_task_master_folders_if_not_present() -> None:
        for folder in FolderCreator.get_required_folders():
            FolderCreator.create_folder_if_not_present(folder)
    
    @staticmethod
    def get_required_folders() -> tuple[str]:
        return (FolderCreator.get_taskmaster_folder_path(), FolderCreator.get_tasks_folder_path())

    @staticmethod
    def get_user_home_path() -> str:
        return os.path.expanduser("~")
    
    @staticmethod
    def get_document_path() -> str:
        return os.path.join(FolderCreator.get_user_home_path(), "Documents")
    
    @staticmethod
    def get_taskmaster_folder_path() -> str:
        return os.path.join(FolderCreator.get_document_path(), "TaskMaster")
    
    @staticmethod
    def get_tasks_folder_path() -> str:
        return os.path.join(FolderCreator.get_taskmaster_folder_path(), "Tasks")
    
    @staticmethod
    def get_tasks_file_path() -> str:
        return os.path.join(FolderCreator.get_tasks_folder_path(), r"tasks.txt")
    
    @staticmethod
    def get_exported_tasks_file_path() -> str:
        return os.path.join(FolderCreator.get_tasks_folder_path(), r"exported_tasks.txt")
    
    @staticmethod
    def create_folder_if_not_present(folder_path: str) -> None:
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass
    
    @staticmethod
    def get_title_bar_icon_path() -> str:
        return os.path.join(ProgramData.get_current_folder_path(), "resources", "icons", "title_bar.ico")
