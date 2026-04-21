from MessageFormatterStrategy import MessageFormatterStrategy


class PlainTextFormatter(MessageFormatterStrategy):

    def format(self, message: str) -> str:
        return message

    def get_type(self) -> str:
        return "PLAIN_TEXT"