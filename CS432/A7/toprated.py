#coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movielens = pd.merge(movie_ratings, users)

#most_rated = movielens.groupby('title').size().sort_values(ascending=False)[:25]
#print most_rated

femaleUsers = movielens.groupby('sex')
print femaleUsers

#movie_stats = movielens.groupby('title').agg({'rating': [np.size, np.mean]})
#print movie_stats.head(25)
