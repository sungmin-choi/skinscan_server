import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict

search_url = 'https://incidecoder.com/search?query='


def getProductsList(keyword):
        result = OrderedDict()
        page = requests.get(search_url+keyword)


        soup = bs(page.text, "html.parser")

        elements = soup.select('#products > div.paddingbl > a.simpletextlistitem')

        elements2 = soup.select('#products > div.paddingbl.center.fs16 > a')

        products = []

        route_pages = []

        

        for index, element in enumerate(elements, 1):
                product = {
                        'id':index,
                        'title': element.text,
                        'url': element.get('href')
                }

                products.append(product)

        result['products'] = products

        for index, element in enumerate(elements2):
                route_page = {
                        'id':index,
                        'title': element.text,
                        'url': element.get('href')
                }

                route_pages.append(route_page)

        result['route_pages'] = route_pages
        
        return result


