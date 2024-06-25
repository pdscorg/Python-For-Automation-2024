import pyautogui
import time 


tab_links = ['https://www.discord.com', 'https://chatgpt.com/', 'https://www.notion.so', 'https://www.google.com', 'https://www.medium.com', 'https://www.linkedin.com']

def launch_site_in_new_tab(url):
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write(url)
    pyautogui.press("enter")

def open_browser(browser_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write(browser_name, interval=0.5)
    pyautogui.press("enter")


open_browser('brave')

time.sleep(5)

for link in tab_links:
    launch_site_in_new_tab(link)


pyautogui.alert("All tabs opened successfully.")



