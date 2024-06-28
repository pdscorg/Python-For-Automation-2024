from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

EMAIL = os.environ.get('EMAIL')
PASS = os.environ.get('PASS')
inp = input("Search for a course:")

driver = webdriver.Firefox()
driver.get("https://www.coursera.org/?authMode=login")

action = ActionChains(driver)
action.send_keys(EMAIL)
action.send_keys(Keys.TAB)
action.send_keys(PASS)
action.send_keys(Keys.ENTER)
action.perform()

time.sleep(20)

driver.switch_to.new_window("tab")
driver.get(f"https://www.coursera.org/search?query={inp}")
driver.find_element(By.CLASS_NAME, "cds-ProductCard-gridCard").click()

