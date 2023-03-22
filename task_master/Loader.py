import os


USER_HOME_PATH = os.path.expanduser("~")
DOCUMENTS_PATH = os.path.join(USER_HOME_PATH, "Documents")
TASKMASTER_FOLDER = os.path.join(DOCUMENTS_PATH, "TaskMaster")
TASKS_FOLDER = os.path.join(TASKMASTER_FOLDER, "Tasks")

REQUIRED_FOLDERS = (TASKMASTER_FOLDER, TASKS_FOLDER)


class Loader:
    
    @staticmethod
    def startup() -> None:
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