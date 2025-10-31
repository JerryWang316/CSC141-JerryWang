def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nEnter album information (or 'q' to quit):")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print(f"Album created: {album}")