
class User:

    def __init__(self, name, email=None, phone=None, slack_id=None, messenger_id=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.slack_id = slack_id
        self.messenger_id = messenger_id
