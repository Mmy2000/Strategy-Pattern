

from NotificationStrategy import NotificationStrategy
from User import User


class SMSNotificationStrategy(NotificationStrategy):

    def send(self, user:User, message):
        print(f"sending sms notification for {user.slack_id} and the message is {message}")