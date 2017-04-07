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

#Reading items file:
i_cols = ['movie_id', 'movie_title' ,'release_date','video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
 encoding='latin-1')

# users younger than 30 OR female
#users.set_index('user_id', inplace=True)
#users.sort_index()
#users.reset_index(inplace=True)
#items.set_index('movie id', inplace=True)
#print(users[(users.sex == 'F') & (users.age == 22) & (users.occupation == 'student')].head(3))
#print ratings.head(5)
#print(ratings[(ratings.user_id == 599) ].head(25))
#print(movies[(movies.movie_id==259)].head())
#print (users.loc[[304, 599, 711]])
movielens = pd.merge(pd.merge(ratings,users),movies)
#by_user = movielens.groupby('user_id')
#print(by_user.head())

#movielens.sort_values([('user_id')], ascending=True)

userAge = movielens['age'] == 22
meList = movielens[userAge].sort_values([('age')])
userSex = meList['sex'] == 'F'
meList = meList[userSex].sort_values([('sex')])
userOcc = meList['occupation'] == 'student'
meList = meList[userOcc].sort_values([('occupation')])

mean_ratings = meList.pivot_table(values='rating', index=['user_id', 'sex', 'age','occupation', 'title'], aggfunc='mean')
#moviesByUser = mean_ratings.sort_index(ascending=True)[:30]

#
# Make a new dataframe for one per user
#
print mean_ratings
