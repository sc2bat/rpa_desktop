import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창의 정보
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left +10, fw.top +20)

# 활성화된 모든 창 정보
# for w in pyautogui.getAllWindows():
#     print(w)

# # 특정 창 정보
# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False : # 활성화 상태가 아니라면
    w.activate() # 활성화 (맨 앞으로 화면을 가져옴)

if w.isMaximized == False: # 최대화가 아니라면
    w.maximize() # 최대화

pyautogui.sleep(1)

# if w.isMinimized == False:
#     w.minimize()

w.restore() # 화면 원복

pyautogui.sleep(1)

w.close() # 윈도우 닫기