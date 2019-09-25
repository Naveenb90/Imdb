# Author: Naveen Baskaran
# Libraries
import pandas as pd

#loading data into dataframw
movie_df = pd.read_csv(r'movie_metadata.csv')  

# Replacing Empty and null values by Zero
values = {'gross': 0, 'budget':0}
movie_df = movie_df.fillna(value = values)

# 2.b.i Profitability profit using lambda
movie_df['Profit1'] = movie_df.apply (lambda row : row['gross']-row['budget'], axis =1)

# 2.b.ii Profitability profit (Simple calculation)
movie_df['Profit2'] = (movie_df['gross']- movie_df['budget'])/movie_df['budget']

# 2.b.iii Profitability Gross profit value using lambda
movie_df['Gross_Profit'] = movie_df.apply (lambda row : (((row['gross']-row['budget'])*100)/row['budget']) if row['gross'] !=0 and row['budget'] !=0 else  0, axis = 1)

# 2.b Top 10 genres and Gross Profit value 
top_ten_genre = movie_df[['genres','Gross_Profit']] #specify columns to filter 
print(top_ten_genre.groupby('genres').sum().sort_values('Gross_Profit',ascending = False).head(10))

# 2.c Top 10 directors  identification
top_ten_directors = movie_df[['director_name','Gross_Profit']]
print(top_ten_directors.groupby('director_name').sum().sort_values('Gross_Profit',ascending = False).head(10))

# 2.c Top 10 actors  identification
top_ten_actors = movie_df[['actor_1_name','Gross_Profit']]
print(top_ten_actors.groupby('actor_1_name').sum().sort_values('Gross_Profit',ascending = False).head(10))

# 2.c Best pair actor 1 and director 
best_pair = movie_df[['actor_1_name','director_name','imdb_score']]

# 3 Best Pair of actor and director 
print("Best pair of director and actor 1")
print(best_pair.sort_values('imdb_score',ascending = False).dropna().head(10))

print("Best pair of director and actor 1 using mean ")
print(best_pair.groupby(['actor_1_name','director_name']).mean().sort_values('imdb_score',ascending = False).head(10))
