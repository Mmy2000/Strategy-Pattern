

from MessageFormatterStrategy import MessageFormatterStrategy


class MessageFormatterService:

    def __init__(self , formatter:MessageFormatterStrategy):
        self._formatter = formatter

    def set_formatter(self , new_formatter:MessageFormatterStrategy):
        self._formatter = new_formatter

    def process_message(self , message:str):
        formatted = self._formatter.format(message)
        formatter_type = self._formatter.get_type()

        print(f"Type: {formatter_type}")
        print(f"Formatted Message: {formatted}")