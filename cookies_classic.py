from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
options=webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

chrome_driver_path = "D:\Development\ChromeDriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cps= driver.find_element(By.ID,"cps").text

production = driver.find_elements(By.CSS_SELECTOR,"#store div") #find items from store
item_ids = [item.get_attribute('id') for item in production] #sort the id's of the items from the store

timeout = time.time()+1
ten_secs= time.time()+10
fifty_secs=time.time()+50
five_mins = time.time()+300

ratios= [.2,.8,4,10,20,100,1332,24691.2]
while (True):
    button = driver.find_element(By.ID,"cookie")
    button.click()

    if time.time() > timeout: # if higher than timeout(5 secs) check for the buyable stuff and see your current cps

        #get the prices that has been coded inside b
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices = []

        for prices in all_prices:#carry the prices into a new list
            element_text = prices.text
            if element_text != '':
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
    #once you get the price list, make a dictionary with their ids, also claim their production ratios
    #divide the ratio over the price, the biggest term is subjected to be a higher buying priority

        #1- form the dictionary:
        cookie_upgrades= {}
        effective_cost=[]
#this elder pledge element was appearing out of thin air, had to get rid of it in the first time and not more than once
        if "buyElder Pledge" in item_ids:
            item_ids.remove("buyElder Pledge")
        print(item_ids)

        for n in range(len(item_prices)):
            effective_cost.append(ratios[n]/item_prices[n]) #calculate the effective cost formula:production/cost
#find a way to end the iteration by the lowest number of item owning list
            cookie_upgrades[item_ids[n]] = effective_cost[n]
    #find the money in hand
        money_element= driver.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",","")
        cookie_count=int(money_element)

        #2-Sort the dictionary and ids from higher to lower, purchase the highest then go outside of the for loop
        sorted_cookie_upgrades=sorted(cookie_upgrades.items(), key=lambda x:x[1], reverse=True)
        for i in sorted_cookie_upgrades:
            if i[1] < cookie_count:
                driver.find_element(By.ID,i[0]).click()
            break
        affordable_upgrades= {}
        print(sorted_cookie_upgrades)

        timeout = time.time()+1
        #found out that timeout works better to be around 1 or 2 seconds in the beginning phase of the game
        if time.time()> ten_secs:
            timeout=time.time()+2
            #we keep incrasing the interval between the item price check timers to control the suitable purchases as the
            #time increases
        if time.time()>fifty_secs:
            timeout=time.time()+4
            #we do the same trick after 10 and 50 seconds and eventually get our results of cps(which is a score indicator)
    if time.time() >five_mins:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(f"***********************************************************************************cookie per second is:{cookie_per_s}")
        break

