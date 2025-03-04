import pandas as pd 
import matplotlib.pyplot as plt 
df1=pd.read_csv(r'C:\Users\Mainak\Downloads\tmdb_5000_credits.csv')
df2=pd.read_csv(r'C:\Users\Mainak\Downloads\tmdb_5000_movies.csv')
df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')
print(df2.head(5))
Cc= df2['vote_average'].mean()
print(Cc)
m= df2['vote_count'].quantile(0.9)
m
q_movies = df2.copy().loc[df2['vote_count'] >= m]
print(q_movies.shape)
def weighted_rating(x, m=m, C=Cc):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
#Sort movies based on score calculated above
q_movies = q_movies.sort_values('score', ascending=False)

#Print the top 15 movies
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10))
pop= df2.sort_values('popularity', ascending=False)

plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(6),pop['popularity'].head(6), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")