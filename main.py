from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("maximized")
chrome_options.add_experimental_option("detach",True)

chrome_driver_path = "D:\Development\ChromeDriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for name in event_names:
    print(name.text)
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)
driver.quit()
