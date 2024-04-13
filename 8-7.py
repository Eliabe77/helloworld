def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('elton john', 'Rocket man')
print(album)

album = make_album('vivaldi', 'four seasons')
print(album)

album = make_album('barry white', 'let the music play')
print(album)