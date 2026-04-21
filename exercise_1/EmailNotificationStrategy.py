

from NotificationStrategy import NotificationStrategy
from User import User


class EmailNotificationStrategy(NotificationStrategy):
    def send(self, user:User, message):
        print(f"sending email notification for {user.email} and the message is {message}")