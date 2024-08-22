from src.utils import input_date_format_validated, clean_string, contains_letter
from src.config import *

# Store base URL in a constant
# Add extra URL based on date given by input user, format validated to match website url-requirements: YYYY-MM-DD
date = input_date_format_validated()
year = date.split("-")[0]
url = f"{BASE_URL}/{date}/#"

# Scrape the songs using BeautifulSoup
response = requests.get(url)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

# Process the soup to a list with items that contain the song title and artist name
raw_items = soup.findAll(class_="o-chart-results-list__item")
raw_items_text = [raw_item.text for raw_item in raw_items]
cleaned_items = [clean_string(item) for item in raw_items_text if contains_letter(item)]
final_items = [item for item in cleaned_items if item is not None]

# Separate the final_items list into two lists: one for song title names, one for artists
titles = [item.split(sep='---')[0] for item in final_items]
artists = [item.split(sep='---')[1] for item in final_items]

# Spotify's authentication via Spotipy
auth_manager = SpotifyOAuth(
    scope='playlist-modify-private',
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    show_dialog=True,
    username='suikerstroop',
    cache_path='token.txt',
)

# Create Spotify API Client that takes the OAuth object as a parameter
sp = spotipy.Spotify(auth_manager=auth_manager)
current_user = sp.current_user()['display_name']
current_user_id = sp.current_user()['id']
# print(f"We are logged in to the account of user '{current_user}', who's user id is '{current_user_id}'.")

# Create playlist and store it in variable
my_playlist = sp.user_playlist_create(user=current_user_id,
                                      name=date,
                                      public=False,
                                      description=f"Billboard Top 100 of {date}",
                                      )

# Search all the songs of our Top 100 on Spotify by track title, artist name and year. Store the song URI's in a list.
track_results = []
for i in range(0, len(final_items)):
    result = sp.search(q=f"track: {titles[i]} artist: artist: {artists[i]} year: {year}", type='track')
    song_uri = result['tracks']['items'][0]['uri']
    track_results.append(song_uri)

# Add the list of songs to the playlist
sp.playlist_add_items(
    playlist_id=my_playlist['id'],
    items=track_results
)
