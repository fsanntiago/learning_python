# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.


def show_messages(messages: list[str]):
    """Print all messages in the list

    Args:
        messages: list of short messages
    """
    for message in messages:
        print(message)


messages = ["happy new year", "good morning", "have a nice day"]
show_messages(messages)
