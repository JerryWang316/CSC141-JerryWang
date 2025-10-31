def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "The Dark Side of the Moon")
album3 = make_album("Taylor Swift", "1989", 13)

print(album1)
print(album2)
print(album3)