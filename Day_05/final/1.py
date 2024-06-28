from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.google.com")

time.sleep(10)

driver.quit()