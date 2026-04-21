from abc import ABC, abstractmethod

class MessageFormatterStrategy(ABC):

    @abstractmethod
    def format(self, message: str) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass