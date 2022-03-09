# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# -----
# "Santiago, Chile"
# -----
# Call your function with at least three city-country pairs, and print the
# values that are returned.


def city_country(city: str, country: str) -> str:
    """Return the city and country names.

    Args:
        city: The name of the city
        country: The name of the country

    Returns:
        Return a string like 'Santiago, Chile'.
    """
    return f"{city.title()}, {country.title()}"


city = city_country("Santiago", "Chile")
print(city)

city = city_country("Rio", "Brazil")
print(city)

city = city_country("Lisboa", "Portugal")
print(city)
