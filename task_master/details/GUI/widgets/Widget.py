from abc import ABC, abstractmethod


class Widget(ABC):
    
    @abstractmethod
    def add_widget(self, widget: any) -> None:
        """Adds a widget inside this widget"""
    
    @abstractmethod
    def create(self, **kwargs: dict[str: any]) -> None:
        """Create the widget of the library"""
    
    @abstractmethod
    def show(self) -> None:
        """Shows the widgets on the screen (and show the widget inside this one as well)"""
