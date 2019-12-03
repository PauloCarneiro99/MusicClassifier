import spotipy
import spotipy.util as util
import random
import pandas as pd
import os
from itertools import chain
from datetime import datetime
import json

repository = os.getcwd()
original_df = pd.read_csv("{}/../Dataset/dataset.csv".format(repository))
original_df = original_df[0:10]

# Dados da Autentificacao
with open(".env", "r") as read_file:
	credentials = json.load(read_file)

CLIENT_ID = credentials["CLIENT_ID"]
CLIENT_SECRET = credentials["CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "http://localhost:8080"
SCOPE = "user-library-read"

#Acessando através do token
token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

myuri = credentials["myuri"]

user = spotify.user(credentials["user"])


#Pegando o ID das musicas
af = []
cont = 0
print(cont, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
for artist, track in zip(original_df["author"], original_df["title"]):
    track_id = spotify.search(q="artist:" + artist + " track:" + track, type="track")
    cont = cont + 1
   
    if(len(track_id["tracks"]["items"]) < 1):
        af.append("")
    else :
        id = track_id["tracks"]["items"][0]["id"]
        af.append(spotify.audio_features(id))

    if cont % 100 == 0:
        print(cont, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    

flat_af = []
for elem in af:
    if elem:
        flat_af.append(elem[0])
    else :
        flat_af.append("")

#Transformando de Data Frame
features = pd.Series(flat_af)
df_features = features.apply(pd.Series)
# df_features.to_csv(r"{}/new_data.csv".format(repository))

#Concatenando com o DataSet
final_df = pd.concat([original_df, df_features], axis = 1)
final_df = final_df.drop(columns = [0])

final_df.to_csv(r"{}/../Dataset/full_data.csv".format(repository))
#print(df1.head(50))