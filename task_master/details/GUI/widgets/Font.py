from tkinter.font import Font as TkFont


class Font:
    
    def __init__(self, family: str, size: int) -> None:
        self._tk_object = TkFont(family=family, size=size)
    
    @property
    def tk_object(self) -> object:
        return self._tk_object
