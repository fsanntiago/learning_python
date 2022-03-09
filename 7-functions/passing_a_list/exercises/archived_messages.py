# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.


from typing import List


def show_messages(messages: List[str]) -> None:
    """Print all messages in the list

    Args:
        messages: list of short messages
    """
    print("\nShowing all messages:")
    for message in messages:
        print(message)


def send_messages(messages: List[str], sent_messages: List[str]) -> None:
    """Print each message, and then move it to sent_messages.

    Args:
        messages: List of messages
        sent_messages: List to where the message should be sent
    """
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(f"Current message: {current_message}")
        sent_messages.append(current_message)


messages = ["happy new year", "good morning", "have a nice day"]
show_messages(messages)

sent_messages: List[str] = []
send_messages(messages[:], sent_messages)


print("\nFinal lists:")
print(messages)
print(sent_messages)
