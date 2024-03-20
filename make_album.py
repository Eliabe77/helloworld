def get_formatted_name(artist_name, album_title_name, artist_album_and_songs_number):
 """Return a full name, neatly formatted."""
 full_name = f"{artist_name} {album_title_name} {artist_album_and_songs_number}"
 return full_name.title() 
while True:
 print("\nPlease tell me artist, album and number of songs:")
 print("(enter 'q' at any time to quit)")
 a_name = input("artist name: ")
 if a_name == 'q':
  break
 al_name = input("album name: ")
 if al_name == 'q':
  break
 s_name = input("songs number: ")
 if s_name == 'q':
  break

 formatted_name = get_formatted_name(a_name, al_name, s_name)
 print(f"\n contains {formatted_name} songs!")