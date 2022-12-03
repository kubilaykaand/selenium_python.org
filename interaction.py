from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By





chrome_driver_path = "D:\Development\ChromeDriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
#most_viewed_pages.click()


search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
while(True):
    pass
# top_view = {}

# top_viewed_views = driver.find_element(By.XPATH, '//*[@id="topview-entry-1"]/td[5]/a')
# print(top_viewed_views.text)
# for view in top_viewed_views:
#     print(view.text)
# for n in range(len(top_viewed_views)):
#     top_view[n] = {
#         "views": top_viewed_views[n].text,
#     }
# print(top_view)
