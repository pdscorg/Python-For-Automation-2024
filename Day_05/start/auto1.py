from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.google.com")

action = ActionChains(driver)
action.send_keys("Hello Selenium")
action.send_keys(Keys.ENTER)
action.perform()

time.sleep(10)
driver.quit()