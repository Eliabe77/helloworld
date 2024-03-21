def get_formatted_name(artist_name, album_title_name, songs_number):
 """Return a full name, neatly formatted."""
 full_name = f"{artist_name} {album_title_name} {songs_number}"
 return full_name.title() 
while True:
    print("\nPlease tell me artist, album and number of songs:")
    print("Enter 'q' at any time to quit")
    a_name = input("Artist name: ")
    if a_name == 'q':
     break
    album_name = input("Album name: ")
    if album_name == 'q':
     break
    s_number = input("songs number: ")
    if s_number == 'q':
     break

    formatted_name = get_formatted_name(a_name, album_name, s_number)
    print(f"\n contains {formatted_name}   songs!")