import pyautogui

w = pyautogui.getWindowsWithTitle("NT")[0]
w.activate()

# pyautogui.write("1,2,3", interval=0.25)
# pyautogui.write("Just do it")
# pyautogui.write("가나다") # 한글처리 안됨

# pyautogui.write(["I", "r", "o", "n", "left", "left", "right", "enter"], interval=0.5)

# https://automatetheboringstuff.com/2e/chapter20/
# ctrl f (keyboard Attributes)

# # 특수문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# # Hot key
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간결하게
# pyautogui.hotkey("ctrl", "a")

# 한글 처리
# pip install pyperclip
import pyperclip # 문장을 클립보드에 넣기
# pyperclip.copy("쇼미더머니") # 글자를 클립 보드에 저장
# pyautogui.hotkey("ctrl", "v") 

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("테스트")

# 자동화 종료
# win : ctrl + alt + del, mac : cmd + shift + option + q