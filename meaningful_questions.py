""" Which are the top 10 movies based on IMDb rating?

    How has the average IMDb rating of movies changed over the years?

    Is there a relationship between movie length (in minutes) and IMDb rating?
 
    Do movies with higher vote counts generally have higher IMDb ratings? """
    

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_dataset.csv")

# Which are the top 10 movies based on IMDb rating?
top_movies = df.nlargest(10, 'IMDb Rating')[['Movie', 'IMDb Rating']]
plt.figure(figsize=(8,5))
sns.barplot(data=top_movies, x='IMDb Rating', y='Movie', palette="viridis")
plt.title("Top 10 Movies by IMDb Rating")
plt.xlabel("IMDb Rating")
plt.ylabel("Movie")
# plt.show()

# How has the average IMDb rating of movies changed over the years?
avg_rating_by_year = df.groupby('Year')['IMDb Rating'].mean().reset_index()
plt.figure(figsize=(10,5))
sns.lineplot(data=avg_rating_by_year, x='Year', y='IMDb Rating', marker='o')
plt.title("Average IMDb Rating Over the Years")
plt.xlabel("Year")
plt.ylabel("Average IMDb Rating")
# plt.show()

# Is there a relationship between movie length (in minutes) and IMDb rating?
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Length (min)', y='IMDb Rating', hue='IMDb Rating', palette='coolwarm', size='IMDb Rating', sizes=(20,200))
plt.title("Movie Length vs IMDb Rating")
plt.xlabel("Length (Minutes)")
plt.ylabel("IMDb Rating")
# plt.show()

# Do movies with higher vote counts generally have higher IMDb ratings? 
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Vote count', y='IMDb Rating', hue='IMDb Rating', palette='mako', size='Vote count', sizes=(20,200))
plt.title("Vote Count vs IMDb Rating")
plt.xlabel("Vote Count")
plt.ylabel("IMDb Rating")
plt.xscale('log')  
plt.show()


