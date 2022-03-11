""" 8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
=======================================================================
car = make_car('subaru', 'outback', color='blue', tow_package=True)
=======================================================================
Print the dictionary that’s returned to make sure all the information was
stored correctly. """


def make_car(manufacturer: str, model: str, **options) -> dict:
    """Make a dictionary representing a car

    Args:
        manufacturer (str): Car manufacturer
        model (str): Car model

    Returns:
        dict: Return a dictionary representing a car
    """
    car_dict = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }
    if options:
        for key, value in options.items():
            car_dict[key] = value

    return car_dict


my_outback = make_car("subaru", "outback", color="blue", tow_package=True)
print(my_outback)

my_old_accord = make_car(
    "honda", "accord", year=1991, color="white", headlights="popup"
)
print(my_old_accord)
