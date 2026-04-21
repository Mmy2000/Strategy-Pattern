
from abc import ABC, abstractmethod


class NotificationStrategy(ABC):

    @abstractmethod
    def send(self , user , message):
        pass