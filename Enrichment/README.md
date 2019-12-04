# Enrichment

The purpose of this branch is to try an enriched approach using Spotify API extra information on songs.

Spotify's database offers a series os different characteristics for tracks such as acoustics, danceability, duration_ms, energy, instrumentals.

## Data Collection

The data was collected through Spotify's API using as reference the previous dataset (```file.csv```). The script ```spotifyteste.py``` requested every track and stored the response in a data frame. The later result was stored as ```Full_data.csv```.

As an alternative to speed up requests, the script ```spotify_pseudo_parallel.py``` was used in multiple terminals, taking as arguments the interval of the original dataset that it would collect.

## Data Processing

The first analysis was made trough PCA. We were interest in testing the relevance of components and perhaps to reduce the space search. Due to the low correlation between features, that was not possible.

After that, we tried using a neural network through Multi Layer Perceptron Algorithm. The main difficult was to chose the proper parameters for training, since we had a wild range of options. Given that, it was choosed to work around the kind of solver, the activation function, the loss alpha, the number of layers, number of perceptrons per layer and kind of learning rate.

In order to try a wide approach, a grid was construct. The best result yelded was with a hyperbolic tangent function of activation, a 0.1 alpha, a single layer with 100 neurons, a decreasing learning rate and a "adam" solver, which is a optimized version of stochastic descending gradient. 

This setup resulted in a 26% accuracy, which is slightly low, but significant better than random (which result in 3%). Compared with the previous defined algorithms, there are no signifcant improve.  

## Future Options

There are infinite many different layouts of hidden layers that could be tried and a random approach to direct this search could be used.

### Technologies
[![Python : spotipy](https://img.shields.io/badge/Python-Spotipy-green)](https://spotipy.readthedocs.io/en/latest/)