


from User import User
from NotificationService import NotificationService
from EmailNotificationStrategy import EmailNotificationStrategy
from SMSNotificationStrategy import SMSNotificationStrategy
from MessengerNotificationStrategy import MessengerNotificationStrategy
from SlackNotificationStrategy import SlackNotificationStrategy


def main():
    user = User(
        name="Mahmoud",
        email="mahmoud@example.com",
        phone="01012345678",
        slack_id="mahmoud.slack",
        messenger_id="mahmoud.messenger"
    )
    service = NotificationService(EmailNotificationStrategy())  # pyright: ignore[reportUndefinedVariable]
    service.send_notification(user, "Welcome via Email!")

    service.set_strategy(SMSNotificationStrategy())
    service.send_notification(user, "Welcome via SMS!")

    service.set_strategy(SlackNotificationStrategy())
    service.send_notification(user, "Welcome via Slack!")

    service.set_strategy(MessengerNotificationStrategy())
    service.send_notification(user, "Welcome via Messenger!")


if __name__ == "__main__":
    main()