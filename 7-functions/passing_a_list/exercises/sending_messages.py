# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


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
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
