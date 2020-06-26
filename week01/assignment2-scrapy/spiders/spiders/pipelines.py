# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SpidersPipeline:
    def __init__(self):
        self.movies = []
    def process_item(self, item, spider):
        print('movie in pipline')
        print(item)
        self.movies.append(item)
        if len(self.movies) is 10:
            with open('maoyan_movies.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Name', 'Type', 'Show Time'])
                for movie in self.movies:
                    writer.writerow([f'{movie["name"]}', f'{movie["movie_type"]}', f'{movie["show_time"]}'])
                print('writing is finished.')
        return self.movies
