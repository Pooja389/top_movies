import requests
from bs4 import BeautifulSoup
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data,"html.parser")
names = soup.select("h2")
movie_list = []
for name in names:
    movie_name = name.get_text(strip=True)
    movie_list.append(movie_name)

movie_list.reverse()
for movie in movie_list:
    print(movie)  
