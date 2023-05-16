from abc import ABC, abstractmethod


class Widget(ABC):

    @property
    @abstractmethod
    def tk_object(self) -> object:
        """Returns the tk object of the current class"""
    
    @abstractmethod
    def add_widget(self, widget: any) -> None:
        """Adds a widget inside this widget"""
    
    @abstractmethod
    def set_params(self, **kwargs) -> None:
        """Create the widget of the library"""
    
    @abstractmethod
    def show(self) -> None:
        """Shows the widgets on the screen (and show the widget inside this one as well)"""
