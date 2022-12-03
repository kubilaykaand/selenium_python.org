import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")


chrome_driver_path="D:\Development\ChromeDriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
lang_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang_button.click()
time.sleep(5)
web_cookies_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
web_cookies_button.click()
timeout= time.time()+5
five_min = time.time() + 1*5
my_element_id='bigCookie'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
your_element= WebDriverWait(driver,timeout,ignored_exceptions=ignored_exceptions)\
    .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))






print(driver.title)
time.sleep(5)

button = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

while (True):
    button.click()

    if time.time() > five_min:
        cps = driver.find_element(By.XPATH,'//*[@id="cookiesPerSecond"]').text
        print(cps)
        five_min=time.time()+5


# for i in range(5000):
#
#
#
#     button.click()
    # buttonCount=int(driver.find_element(By.ID,"cookies").text.split('')[0].replace('.',''))

    # if driver.find_element_by_xpath('')
# action = ActionChains(driver)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]'))).click()
#
