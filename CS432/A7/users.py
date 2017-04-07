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
movielens = pd.merge(pd.merge(ratings,users),movies)

most_rated = movielens.groupby('title').size().sort_values(ascending=False)[:25]
movielens.sort_values([('user_id')], ascending=True)

userAge = movielens['age'] == 22
meList = movielens[userAge].sort_values([('age')])
userSex = meList['sex'] == 'F'
meList = meList[userSex].sort_values([('sex')])
userOcc = meList['occupation'] == 'student'
meList = meList[userOcc].sort_values([('occupation')])
#userId = meList['user_id'] == 304
userId = meList['user_id'] == 711
meList = meList[userId].sort_values([('user_id')])
userRatings = meList['rating'] > 4
#userRatings = meList['rating'] <= 2
meList = meList[userRatings].sort_values([('rating')], ascending=True)[:5]
print meList

# for line in movielens:
#     while(movielens[movielens.age = 22]):
#         print most_rated

#movie_stats = movielens.groupby('title').agg({'rating': [np.size, np.mean]})
#print movie_stats.head(25)
