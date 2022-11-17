import sqlite3
def joinOperations():
    connection = sqlite3.connect("chinook.db")
    join = connection.execute("""select albums.Title, artists.Name from artists
    inner join albums on artists.ArtistId = albums.ArtistId""")
    for row in join:
        print("Album Title = " + row[0])
        print("Artist Name = " + row[1])
    connection.commit()
    connection.close()
joinOperations()