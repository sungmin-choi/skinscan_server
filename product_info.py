import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict

url = 'https://incidecoder.com'



def getProductInfo(link):
    page = requests.get(url+link)

    soup = bs(page.text, "html.parser")

    result = OrderedDict()
    title = soup.select('#product-title')[0].text
    img_url = soup.select('#product-main-image > picture > img')[0].get('src')
    brand_name = soup.select('#product-brand-title > a')[0].text
    prouduct_description=soup.select('#product-details')[0].text.replace('\n', '')
    update_info=soup.select('#content > div.detailpage > div.std-side-padding.paddingtl > div.prodinfobox.prodnexttoimage.fleft > div > div.fs12')[0].text

    ingredients=soup.select('#showmore-section-ingredlist-short > div > span')

    result['title']=title
    result['img_url']=img_url
    result['brand_name']=brand_name
    result['prouduct_description']=prouduct_description
    result['update_info'] = update_info
    ingredients_text=''

    for ingredient in ingredients:
        ingredients_text+=ingredient.text

    result['ingredients'] = ingredients_text.replace(' ','').replace("\n", "").replace('[more]','')
    return result

