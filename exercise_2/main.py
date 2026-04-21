from JSONFormatter import JSONFormatter
from MessageFormatterService import MessageFormatterService
from PlainTextFormatter import PlainTextFormatter
from XMLFormatter import XMLFormatter


def main():
    service = MessageFormatterService(JSONFormatter())
    service.process_message("Hello World")

    print("-----")

    service.set_formatter(XMLFormatter())
    service.process_message("Hello World")

    print("-----")

    service.set_formatter(PlainTextFormatter())
    service.process_message("Hello World")


if __name__ == "__main__":
    main()