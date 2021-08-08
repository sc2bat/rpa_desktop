# 마우스 정보

import pyautogui
# pyautogui.FAILSAFE = False
# pyautogui.mouseInfo()
pyautogui.PAUSE = 1 # 동적에 1초 부여

# 위치 1010,14 색 179,179,179 #B3B3B3

# 매크로 돌리다 실패하면 멈춰어야함

for i in range(5):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)
