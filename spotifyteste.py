import spotipy
import spotipy.util as util
import random
import pandas as pd
from itertools import chain

df = pd.read_csv('file.csv')
df1 = df[:40]

# Dados da Autentificacao
CLIENT_ID = 'f08757aefb25428baa1f8359973a3c24'
CLIENT_SECRET = 'eb2766cf887b4ddd8aa45a8f7b674993'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'

#Acessando através do token
token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

myuri = 'spotify:user:12171527850'
#spotify.trace = True # turn on tracing
#spotify.trace_out = True # turn on trace out

user = spotify.user('12171527850')

#Pegando o ID das musicas
af = []
cont = 0
for artist, track in zip(df1['author'], df1['title']):
    track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track')
    if(len(track_id['tracks']['items']) < 1):
        cont = cont + 1
        af.append('')
        print(artist + ' ' + track + ' ' + str(cont))
    else :
        id = track_id['tracks']['items'][0]['id']
        af.append(spotify.audio_features(id))

flat_af = []
for elem in af:
    if elem:
        flat_af.append(elem[0])
    else :
        flat_af.append('')

print('Flat List : ', flat_af)

#Pegando as features das musicas
#af = spotify.audio_features(id)
#print(af)

#Transformando de Data Frame
features = pd.Series(flat_af)
df_features = features.apply(pd.Series)
df_features.to_csv(r'C:\Users\eduar\Documents\USP\Data Science\dataframe1.csv')

#Concatenando com o DataSet
df1 = pd.concat([df1, df_features], axis = 1)
#df1.drop(columns = ['Unnamed: 0', '0'])
df1.to_csv(r'C:\Users\eduar\Documents\USP\Data Science\dataframe2.csv')
#print(df1.head(50))