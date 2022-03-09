# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.


from typing import Optional


def make_shirt(size: Optional[str] = "large", message: str = "I love Python"):
    """Summarize the shirt that's going to be made.

    Args:
        size (str, optional): _description_. Defaults to "large".
        message (str, optional): _description_. Defaults to "I love Python".
    """
    print(f"\n - Shirt size: {size}")
    print(f" - Message on the shirt: {message}")


# Large shirt and default message
make_shirt()

# Medium shirt and default message
make_shirt("medium")

# Shirt of any size with a different message
make_shirt("small", "I love Java")
