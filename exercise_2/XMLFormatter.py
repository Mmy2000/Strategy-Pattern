from MessageFormatterStrategy import MessageFormatterStrategy


class XMLFormatter(MessageFormatterStrategy):

    def format(self, message: str) -> str:
        return f"<message>{message}</message>"

    def get_type(self) -> str:
        return "XML"