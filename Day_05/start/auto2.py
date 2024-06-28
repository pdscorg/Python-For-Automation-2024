from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


inp = input("Enter video: ")

driver = webdriver.Firefox()
driver.get(f"https://www.youtube.com/results?search_query={inp}")
# time.sleep()
driver.find_element(By.ID, "video-title").click()


actions = ActionChains(driver)
actions.send_keys("f")
actions.perform()

# time.sleep(10)
# driver.quit()