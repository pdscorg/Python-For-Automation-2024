import pyautogui
import time

time.sleep(5)

pyautogui.click(100, 200)  # Adjust coordinates as necessary
time.sleep(1)

pyautogui.write('John Doe', interval=0.1)
pyautogui.press('tab')
time.sleep(1)

pyautogui.write('johndoe@example.com', interval=0.1)
pyautogui.press('tab')
time.sleep(1)

pyautogui.write('1234567890', interval=0.1)
pyautogui.press('tab')
time.sleep(1)

pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(150, 400)  # Adjust coordinates as necessary
