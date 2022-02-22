# 6-11. Cities: Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary of information
# about each city and include the country that the city is in, its
# approximate population, and one fact about that city. The keys for
# each city’s dictionary should be something like country, population,
# and fact. Print the name of each city and all of the information you
# have stored about it.
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_435_191,
        'nearby mountains': 'mount fuji',
        },
    'são paulo': {
        'country': 'brazil',
        'population': 21_846_507,
        'nearby mountains': 'pico do jaraguá',
        },
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}")
    print(f"  It has a population of obout {population:,}")
    print(f"  The {mountains} mounats are nearby")
