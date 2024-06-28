from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.google.com")

actions = ActionChains(driver)
actions.send_keys("Hello Selenium").key_down(Keys.ENTER).perform()
