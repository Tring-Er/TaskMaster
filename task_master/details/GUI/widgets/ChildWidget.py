from abc import ABC, abstractmethod

from details.gui.widgets.Widget import Widget


class ChildWidget(Widget, ABC):
    
    @abstractmethod
    def set_parent(self, widget: Widget) -> None:
        """Set the parent of the current widget object"""
