from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

all_movies = soup.find_all("h2")

movie_titles = []

for movie in all_movies:
    text = movie.getText(strip=True)
    if text and text[0].isdigit() and ")" in text:
        movie_titles.append(text)

movie_titles.reverse()

df = pd.DataFrame(movie_titles)

df.to_csv("movies.csv", index=False, header=False)
