from NotificationStrategy import NotificationStrategy


class SlackNotificationStrategy(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending Slack message to {user.slack_id}: {message}")
