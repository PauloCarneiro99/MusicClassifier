# Enrichment

The purpose of this branch is to try an enriched approach using Spotify API extra information on songs.

Spotify's database offers a series os different characteristics for tracks such as acoustics, danceability, duration_ms, energy, instrumentals.

## Data Collection

The data was collected through Spotify's API using as reference the previous dataset (```file.csv```). The script ```spotifyteste.py``` requested every track and stored the response in a data frame. The later result was stored as ```Full_data.csv```.

As an alternative to speed up requests, the script ```spotify_pseudo_parallel.py``` was used in multiple terminals, taking as arguments the interval of the original dataset that it would collect.

## Data Processing