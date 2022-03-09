# 8-2. Favorite Book: Write a function called favorite_book() that
# accepts one parameter, title. The function should print a message,
# such as One of my favorite books is Alice in Wonderland. Call the
# function, making sure to include a book title as an argument in the
# function call.


def favorite_book(title):
    """Display favorite book

    Args:
        title (str): favorite book title.
    """
    print(f"One of my favorite books is {title.capitalize()}.")


favorite_book("Diary of a wimpy kid")
