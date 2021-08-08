import pyperclip 
import sys
import pyautogui

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

btn_text = pyautogui.locateOnScreen("msp_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("Failed")
    sys.exit()

pyautogui.click(200, 200, duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("한글")

pyautogui.sleep(5)

window.close()

pyautogui.sleep(1)

pyautogui.press("n")