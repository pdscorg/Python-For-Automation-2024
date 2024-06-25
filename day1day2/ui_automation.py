# OPENING MULTIPLE TABS IN BROWSER AT ONCE USING PYTHON

# https://medium.com/@dhritishah1104/pyautogui-automate-anything-in-python-094d503eb2a3
import pyautogui as p
import time 

# p.press('win')

# time.sleep(1)

# p.write('brave')

# p.press('enter')

# time.sleep(3)

# p.write('https://pcampus.edu.np/')
# p.press('enter')

# p.hotkey('ctrl', 't')

# time.sleep(1)

# p.write('https://www.facebook.com/')

# p.press('enter')


# GETTING SCREEN RESOLUTION 
# codescreen_width, screen_height = p.size()

# p.PAUSE = 1

# print(codescreen_width, screen_height)


# MOUSE MOVEMENT 
p.moveTo(400, 100, duration=1)

# MOUSE CLICK 
p.click()

# p.moveTo(1920, 1080, duration=0.5)

p.dragTo(400, 300, duration=2)

p.alert('This is an alert box.')

