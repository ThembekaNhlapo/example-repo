class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# 3. Create albums1 and add five Album objects
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Hotel California", 9, "Eagles")
]

print("albums1:")
for album in albums1:
    print(album)

# 4. Sort albums1 according to number_of_songs
albums1.sort(key=lambda album: album.number_of_songs)

print("\nalbums1 sorted by number of songs:")
for album in albums1:
    print(album)

# 5. Swap first and second elements
albums1[0], albums1[1] = albums1[1], albums1[0]

print("\nalbums1 after swapping positions 1 and 2:")
for album in albums1:
    print(album)

# 6. Create albums2
albums2 = []

# 7. Add five Album objects to albums2
albums2.extend([
    Album("1989", 13, "Taylor Swift"),
    Album("25", 11, "Adele"),
    Album("Hybrid Theory", 12, "Linkin Park"),
    Album("Nevermind", 13, "Nirvana"),
    Album("Born to Run", 8, "Bruce Springsteen")
])

print("\nalbums2:")
for album in albums2:
    print(album)

# 8. Copy all albums from albums1 into albums2
albums2.extend(albums1)

# 9. Add the specified albums
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops! ... I Did It Again", 16, "Britney Spears"))

# 10. Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.album_name)

print("\nalbums2 sorted alphabetically:")
for album in albums2:
    print(album)

# 11. Search for Dark Side of the Moon and print its index
for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\n'Dark Side of the Moon' found at index: {index}")
        break