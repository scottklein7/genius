import lyricsgenius
from lyricsgenius import Genius

client_access_token = "kLxktps7zneNyDod1aF4g-Uy_RDBblfNvL-CK-aACZzVJ6dXNNhqgQLfq-v6q3od"

# genius = lyricsgenius.Genius(client_access_token)

# artist = genius.search_artist("Ariana Grande", max_songs=1, sort="title")

# song = genius.search_song("34+35", artist.name)

# LYRICS = song.lyrics
# print(LYRICS)

## Code below was copied and pasted from LyricsGenius API --> would not run
## Error: "Song object is not subscriptable" ??

genius = lyricsgenius.Genius(client_access_token)

# artist = genius.search_artist('Andy Shauf', max_songs=0)
# song = genius.search_song('Toy You', artist.name)

# res = genius.album_cover_arts(104614)
# print(res['cover_arts'][0]['image_url'])
# search_term = "AUTOPILOT"
# album = genius.search_albums("AUTOPILOT", per_page=None, page=None)
# print(album)

############### ALBUM SEARCH ###############
# almbum = genius.search('Swimming', per_page=1, page=None, type_='album')
# print(almbum)
# print(almbum['sections'][0]['hits'][0]['result']['api_path'])
# print(almbum['sections'][0]['hits'][0]['result']['full_title'])
# print(almbum['sections'][0]['hits'][0]['result']['cover_art_url'])
# print(almbum['sections'][0]['hits'][0]['result']['release_date_components'])
# print(almbum['sections'][0]['hits'][0]['result']['artist']['image_url'])
# print(almbum['sections'][0]['hits'][0]['result']['artist']['name'])
# print(almbum['sections'][0]['hits'][0]['result']['artist']['id'])

############### Lyric SEARCH ###############
lyric = genius.search_lyrics("Your hidden glory and creation", per_page=1, page=None)
# print(lyric['sections'][0]['hits'][0]['highlights'][0]['value']) #gets searched for lyrics that match song lyrics
# print(lyric['sections'][0]['hits'][0]['result']['artist_names']) #band/artist name
print(lyric['sections'][0]['hits'][0]['result']['id']) #song id
# print(lyric['sections'][0]['hits'][0]['result']['song_art_image_url']) #band id
# print(lyric['sections'][0]['hits'][0]['result']['primary_artist']['api_path']) #band id
# print(lyric['sections'][0]['hits'][0]['result']['primary_artist']['header_image_url']) #band img

############### Song ###############
song = genius.search_song(title='How to save a life') 
# song = genius.search_song(title='How to save a life', artist='The Fray') # can also add 'Artist name as 2nd param
# song = genius.search_song(title='How to save a life', get_full_info=True) # gets the band as for the song
print(song)