import pyautogui

# List of names
names = ["John", "Jane", "Alice", "Bob"]

# Loop through the names and enter them
for name in names:
    pyautogui.typewrite(name)
    pyautogui.press("enter")