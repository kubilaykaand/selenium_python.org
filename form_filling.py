from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
chrome_driver_path = "D:\Development\ChromeDriver"
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

application_site = driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME,"email")

first_name.send_keys("Kubilay")#,Keys.ENTER)
last_name.send_keys("Kaan")#,Keys.ENTER)
email.send_keys("kubilaykaand@gmail.com")#,Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()
while(True):
    pass

