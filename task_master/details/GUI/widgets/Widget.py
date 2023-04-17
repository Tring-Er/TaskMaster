from abc import ABC, abstractmethod


class Widget(ABC):
    
    @abstractmethod
    def add_widget(self, widget: any) -> None:
        """Adds a widget inside this widget"""
