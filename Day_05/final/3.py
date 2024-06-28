from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

inp = input("Search for an video:")

driver = webdriver.Firefox()
driver.get(f"https://www.youtube.com/results?search_query={inp}")
driver.find_element("id", "video-title").click()

action = ActionChains(driver)
action.send_keys("f").perform()