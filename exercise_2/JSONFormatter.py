

from MessageFormatterStrategy import MessageFormatterStrategy


import json

class JSONFormatter(MessageFormatterStrategy):

    def format(self, message: str) -> str:
        return json.dumps({"message": message})

    def get_type(self) -> str:
        return "JSON"