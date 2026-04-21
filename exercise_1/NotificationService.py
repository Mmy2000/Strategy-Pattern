

from NotificationStrategy import NotificationStrategy


class NotificationService:
    def __init__(self , strategy:NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def send_notification(self,user,message):
        self._strategy.send(user,message)