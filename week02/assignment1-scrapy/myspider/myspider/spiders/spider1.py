import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem


class Maoyao(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        url: str = 'https://maoyan.com/films?showType=3'
        print('starting to crawl...')
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, Response):
        print('scrapy is parsing')
        print(Response.url)
        items = []
        movies = Selector(response=Response).xpath('//div[@class="movie-hover-info"]')
        try:
            for movie in movies[:10]:
                name = movie.xpath('./div[1]/span[@class="name "]/text()').get()
                movie_type = movie.xpath('./div[2]/text()')[1].get().strip()
                show_time = movie.xpath('./div[3]/text()')[1].get().strip()
                # print('name is',name)
                # print('movie_type is: ',movie_type)
                # print('show_time is ', show_time)
                item = SpidersItem()
                item['name'] = name
                item['movie_type'] = movie_type
                item['show_time'] = show_time
                items.append(item)
        except:
            print('an error occurred')
        finally:
            print('items are ', items)
        return items
