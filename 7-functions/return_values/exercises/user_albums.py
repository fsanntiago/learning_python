# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


from typing import Dict


def make_album(artist: str, album_title: str, tracks: int = 0) -> dict:
    """Builld a dictionary containing information about an album

    Args:
        artist: The artist name
        album_title: The title of the album
        tracks: Number of tracks on the album. Defaults to 0.

    Returns:
        Dictionary containing information about the album
    """
    album_dict: Dict[str, str | int]
    album_dict = {
        "artist": artist.title(),
        "title": album_title.title(),
    }
    if tracks:
        album_dict["tracks"] = tracks

    return album_dict


# Prepare the prompts
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user kwon how to quit
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt).strip()
    if title == "quit":
        break

    artist = input(artist_prompt).strip()
    if artist == "quit":
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
