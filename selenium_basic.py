from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://incidecoder.com/"

options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new")  
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)

driver.get(url)

driver.implicitly_wait(10)

driver.find_element(By.ID, "query").send_keys('banillla co')

time.sleep(1)

driver.find_element(By.ID, "query").send_keys(Keys.RETURN)


# print(driver.title)

# driver.quit()