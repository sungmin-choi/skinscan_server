from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
import time


url = "https://incidecoder.com"

product_url= '/products/banila-co-hi-bye-vita-peel-essence'


ingredients_url='https://folliculitisscout.com/'





options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless=new")  
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)

driver.get(url+product_url)

driver.implicitly_wait(2)

elements=driver.find_elements(By.XPATH, '//*[@id="showmore-section-ingredlist-short"]/div/span')


ingredients = ''

for element in elements:
    ingredients +=element.text





driver.get(ingredients_url)


driver.implicitly_wait(2)

driver.find_element(By.ID, "ingredients").send_keys(ingredients)

time.sleep(0.5)

driver.find_element(By.XPATH,'//*[@id="ingredient-check-btn"]').click()

multi_triggers = driver.find_element(By.CSS_SELECTOR,'#cmsmasters_column_qnh56yuhtr > div > div > div > div.col-sm-9 > div:nth-child(1) > div > div.ing-result > div:nth-child(2) > div.fs-ing-details > div > div.right-fs-ing-attr-check > p.multi-triggers > b')

rows = driver.find_elements(By.CSS_SELECTOR,'#cmsmasters_column_qnh56yuhtr > div > div > div > div.col-sm-9 > div:nth-child(1) > div > div.ing-result > div:nth-child(2) > div.fs-ing-details > table > tbody > tr')


result = OrderedDict()

result['triggers_cnt'] = multi_triggers




for row in rows:
    danger_icon=''
    caution_text=''
    print('d')
    ing_title = row.find_element(By.CLASS_NAME,'ing-title')
    # try:
    #     danger_icon = row.find_element(By.CLASS_NAME, 'danger_icon')
    # except:
    #     danger_icon=''
   
    # lis=row.find_elements(By.CSS_SELECTOR,'td:nth-child(1) > ul > li')
    # for li in lis:
    #     print(li.find_element(By.CLASS_NAME, 'caution').text)
    [ewg_score,cir_findings] = row.find_elements(By.CSS_SELECTOR,'td:nth-child(2) > span')
    cosmetic_roles = row.find_element(By.CSS_SELECTOR,'td:nth-child(2) > div')
    # print(cosmetic_roles.text)
   



