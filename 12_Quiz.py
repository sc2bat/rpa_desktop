# 동작을 자동으로 수행하는 프로그램을 작성하시오.

# 1. 그림판 실행 hotkey win+r, 입력값 : mspaint 및 최대화

# 2. 상단의 텍스트 기능을 이용 흰영역 아무 곳에다가 글자 입력
# - 입력 글자 : "Good Game"

# 3. 5초 대기 후 그림판 종료
# 이 때 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui

pyautogui.hotkey("win", "r")

pyautogui.sleep(1)

pyautogui.write("mspaint")

pyautogui.sleep(1)

pyautogui.press("enter")

pyautogui.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False :
    w.activate() 

if w.isMaximized == False: 
    w.maximize() 

pyautogui.sleep(1)

text = pyautogui.locateOnScreen("msp_text.png")
pyautogui.click(text)

pyautogui.sleep(1)

# pyautogui.mouseInfo()
# # 18,165 0,0,0 #000000
pyautogui.click(100, 200)

pyautogui.sleep(1)

pyautogui.write("Good Game")

pyautogui.sleep(1)

pyautogui.countdown(5)

w.close()

pyautogui.sleep(1)

pyautogui.press("n")

# pyautogui.sleep(1)