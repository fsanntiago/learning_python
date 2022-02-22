# 6-9. Favorite Places: Make a dictionary called favorite_places. Think
# of three names to use as keys in the dictionary, and store one to
# three favorite places for each person. To make this exercise a bit
# more interesting, ask some friends to name a few of their favorite
# places. Loop through the dictionary, and print each person’s name and
# their favorite places.

# Makes empty dict
favorite_places = {}

# Stores keys and values in the dictionary
favorite_places['fabricio'] = ['brazil', 'france', 'russian']
favorite_places['maria'] = ['united states', 'portugal', 'south africa']
favorite_places['frank'] = ['greece', 'brazil', 'argentina']

# Display favorite places
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t-{place.title()}")
