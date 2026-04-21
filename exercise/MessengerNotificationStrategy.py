


from NotificationStrategy import NotificationStrategy


class MessengerNotificationStrategy(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending Messenger message to {user.messenger_id}: {message}")