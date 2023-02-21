
from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task


class CLI(Readable, Sendable):
    
    def read(self) -> list[Task]:
        message = input("Write a text: ")
        return [self.converter(message)]
    
    def send(self, tasks: list[Task]) -> None:
        for task in tasks:
            print(task.text)
    
    def converter(self, text: str) -> Task:
        return Task(text)
    
    def print_task(self) -> None:
        tasks = self.read()
        for task in tasks:
            self.send(task)
