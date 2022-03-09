# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.


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


album = make_album("metallica", "ride the lightning")
print(album)

album = make_album("kenye west", "donda", 27)
print(album)

album = make_album("beethoven", "ninth symphony")
print(album)
