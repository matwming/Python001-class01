from settings import url, request_settings
import requests
from bs4 import BeautifulSoup
from typing import Dict,List
import csv

def find_movies(html:str,num: int):
    soup = BeautifulSoup(html,'html.parser')
    if num == 0:
        return

    movies = soup.find_all('div', class_='movie-item-hover', limit=num)
    if len(movies) == 0:
        print('crawl is probably blocked. Please try again.')
        return

    moviesList: List[object] = []
    for movie in movies:
        new_soup = BeautifulSoup(str(movie),'html.parser')
        movie_info = {
            'name':new_soup.find_all('span',class_='name')[0].get_text(),
            'type':new_soup.find_all('span',class_='hover-tag')[0].parent.get_text().replace(' ','').split()[1],
            'show_time':new_soup.find_all('span',class_='hover-tag')[2].parent.get_text().replace(' ','').split()[1]
        }
        moviesList.append(movie_info)
    return moviesList


def process_movies(movieList) -> None:
    print('start to write a file...')
    print('movieList is ', movieList)
    with open('maoyan_movies.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name','Type','Show Time'])
        for movie in movieList:
            print('movie',movie)
            writer.writerow([f'{movie["name"]}' ,f'{movie["type"]}',f'{movie["show_time"]}'])
        print('writing is finished.')

def main():
    response = requests.get(url, headers=request_settings)
    response.encoding = 'utf-8'
    print(response.text)
    print(f'返回码是: {response.status_code}')
    result = find_movies(response.text,10)
    print(result)
    if result is None:
        print('no movie is successfully retrieved.')
        return
    process_movies(result)

main()