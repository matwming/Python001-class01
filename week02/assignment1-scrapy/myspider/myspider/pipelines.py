# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql.cursors


def save_to_db(item):
    connect = pymysql.connect(
        hosthost='localhost',
        user='root',
        db='movie',
        password='root',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8mb4'
    )
    try:
        with connect.cursor() as cursor:
            # make sure local mysql has table row named, name, movie_type,show_time
            sql="insert into `movies` (`name`,`type`,`show_time`) values (%s, %s, %s)"
            cursor.execute(sql, (item['name'], item['movie_type'], item['show-time']))
            connect.commit()
    finally:
        connect.close()

def save_to_csv(self,item):
    with open('maoyan_movies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Type', 'Show Time'])
        for movie in self.movies:
            writer.writerow([f'{movie["name"]}', f'{movie["movie_type"]}', f'{movie["show_time"]}'])
        print('writing is finished.')


class MyspiderPipeline:
    def __init__(self):
        self.movies = []

    def process_item(self, item, spider):
        print('movie in pipline')
        print(item)
        self.movies.append(item)
        if len(self.movies) is 10:
            save_to_db(self, item)
        return self.movies



