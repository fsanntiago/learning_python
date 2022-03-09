# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


def make_shirt(size: str, message: str):
    """Display a sentence with a size and message that
    should be printed on the shirt

    Args:
        size: size of the shirt(small, medium, large)
        message: message printed on the shirt
    """
    print(f"\n - Shirt size: {size}")
    print(f" - Message on the shirt: {message}")


make_shirt("large", "Hello!")
make_shirt(size="medium", message="Hello World!")
