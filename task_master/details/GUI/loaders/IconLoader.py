import os

from ProgramData import ProgramData


class IconLoader:
    
    @staticmethod
    def get_title_bar_icon_path() -> str:
        return os.path.join(ProgramData.get_current_folder_path(), "resources", "icons", "title_bar.ico")
