import pyautogui

# 마우스 절대좌표로 이동
# pyautogui.moveTo(200, 100) # 지정한 위치로 마우스커서 이동
# pyautogui.moveTo(100, 200, duration=5) # 5초 동안 이동

# pyautogui.moveTo(100, 100, duration=0.5)
# pyautogui.moveTo(200, 200, duration=0.5)
# # pyautogui.moveTo(300, 300, duration=0.5)

# # 상대 좌표로 이동 현재 위치로부터 이동
# pyautogui.moveTo(100, 100, duration=0.5)
# # print(pyautogui.position()) # Point(x,y)
# pyautogui.move(100, 100, duration=0.5)
# # print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.5)
# # print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)